import json
from collections import defaultdict
from datetime import timedelta, datetime

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db import models
from django.db.models import ExpressionWrapper, DurationField, F, Sum, Max, Prefetch
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.timezone import localtime

from .models import Norm, Aircraft, Exercise, ExerciseResult, FlightResult, CustomUser


@login_required
def account_dashboard(request):
    # You can pass additional context if needed
    return render(request, 'account/dashboard.html')

@login_required
def manage_account(request):
    # Your logic for managing account
    return render(request, 'account/manage_account.html')

def is_instructor(user):
    return user.groups.filter(name="Instructor").exists()

def is_examiner(user):
    return user.groups.filter(name="Examiner").exists()


@login_required
@user_passes_test(is_instructor)
def log_flight_lesson(request):
    return render_log_flight(
        request,
        norm_type="lesson",
        functions=["Dual", "PIC"],
        grading_choices=[1, 2, 3],
        grade_labels={1: "1", 2: "2", 3: "3"}
    )

@login_required
@user_passes_test(is_examiner)
def log_flight_skilltest(request):
    return render_log_flight(
        request,
        norm_type="skilltest",
        functions=["Dual"],
        grading_choices=[1, 2],
        grade_labels={1: "Not Approved", 2: "Approved"}
    )

@login_required
@user_passes_test(is_instructor)
def log_flight_pft(request):
    return render_log_flight(
        request,
        norm_type="pft",
        functions=["Dual"],
        grading_choices=[1, 2],
        grade_labels={1: "Not Approved", 2: "Approved"}
    )

def render_log_flight(request, norm_type, functions, grading_choices, grade_labels):
    # 1) Aircraft & pilot list
    aircrafts = Aircraft.objects.all()
    if norm_type == "lesson":
        pilots = CustomUser.objects.filter(
            models.Q(club=request.user.club) | models.Q(allowed_instructors=request.user),
            groups__name='Student'
        ).distinct()
    if norm_type == "skilltest":
        # Step 1: Filter students in club or allowed list
        candidates = CustomUser.objects.filter(
            models.Q(club=request.user.club) | models.Q(allowed_instructors=request.user),
            groups__name='Student'
        ).distinct()

        qualified_pilot_ids = []

        # Step 2: Process each candidate pilot
        for pilot in candidates:
            passed_all = True

            # Step 2a: Get only relevant exercises for this pilot's ul_class and 'lesson' norm_type
            relevant_exercises = Exercise.objects.filter(
                norm__norm_type='lesson',
                norm__ul_class=pilot.ul_class
            ).select_related('norm')

            # Group exercises by ID for lookup
            required_exercise_ids = {exercise.id for exercise in relevant_exercises}

            # Step 2b: Get pilot's recent exercise results (prefetched by flight)
            flight_results = (
                FlightResult.objects.filter(pilot=pilot)
                .prefetch_related(
                    Prefetch('exerciseresult_set', queryset=ExerciseResult.objects.select_related('exercise'))
                )
                .order_by('-off_blocks')  # latest first
            )

            # Map of {exercise_id: list of most recent grades}
            grades_by_exercise = defaultdict(list)

            for flight in flight_results:
                for result in flight.exerciseresult_set.all():
                    if result.exercise_id in required_exercise_ids:
                        grades_by_exercise[result.exercise_id].append(result.grade)

            # Step 2c: Check each relevant exercise for 3 most recent grades == 3
            for eid in required_exercise_ids:
                last_grades = grades_by_exercise.get(eid, [])
                if len(last_grades) < 3 or any(g != 3 for g in last_grades[:3]):
                    passed_all = False
                    break

            if passed_all:
                qualified_pilot_ids.append(pilot.id)

        # Step 3: Final queryset of qualifying pilots
        pilots = candidates.filter(id__in=qualified_pilot_ids)
    elif norm_type == "pft":
        pilots = CustomUser.objects.filter(
            models.Q(club=request.user.club) | models.Q(allowed_instructors=request.user),
            groups__name='Pilot'
        ).distinct()

    # 2) Selected pilot from GET
    pilot_id = request.GET.get('pilot_id')
    selected_pilot = None
    if pilot_id:
        selected_pilot = get_object_or_404(CustomUser, id=pilot_id)

    # 3) Filter norms by pilot's norm_type
    if selected_pilot and selected_pilot.ul_class:
        norms = Norm.objects.filter(ul_class=selected_pilot.ul_class, norm_type=norm_type).prefetch_related('exercises').order_by('id')
    else:
        norms = Norm.objects.none()

    # 4) Handle POST for saving the flight
    form_errors = {}
    if request.method == "POST":
        pid = request.POST.get('pilot_id')
        pilot = get_object_or_404(CustomUser, id=pid)
        pilot_function = "Dual"

        # Parse form fields
        try:
            off_blocks = datetime.fromisoformat(request.POST['off_blocks'])
            on_blocks = datetime.fromisoformat(request.POST['on_blocks'])
        except ValueError:
            form_errors["blocks"] = "Invalid datetime format."
        else:
            if on_blocks < off_blocks:
                form_errors["blocks"] = "On blocks must be after or equal to off blocks."

        grades = json.loads(request.POST.get('grades', '{}'))

        if norm_type == "lesson":
            # Comment requirement for 1 or 2 grades
            for ex_id_str, grade in grades.items():
                if grade in (1, 2):
                    comment = request.POST.get(f"comment_{ex_id_str}", "").strip()
                    if not comment:
                        form_errors[f"comment_{ex_id_str}"] = f"Comment required for exercises graded 1 or 2."
                        break

        if norm_type == "lesson":
            exercise_ids = [int(eid) for eid in grades.keys()]
            selected_norms = Norm.objects.filter(exercises__id__in=exercise_ids).values_list("title", flat=True).distinct()
            g_norms = any(t.startswith("G") for t in selected_norms)
            v_norms = any(t.startswith("V") for t in selected_norms)
            if g_norms and v_norms:
                form_errors["norm_conflict"] = "Cannot log both G and V type norms in the same flight."

            pilot_function = "PIC" if v_norms else "Dual"

        if form_errors:
            return render(request, "logflight.html", {
                "aircrafts": aircrafts,
                "pilots": pilots,
                "functions": functions,
                "norms": norms,
                "scores": grading_choices,
                "grade_labels": grade_labels,
                "norm_type": norm_type,
                "selected_pilot": selected_pilot,
                "form_errors": form_errors,
                "form_data": {k: v for k, v in request.POST.items()},
                "form_grades_json": request.POST.get("grades", "{}"),
            })

        # Save result
        flight_result = FlightResult.objects.create(
            pilot=pilot,
            instructor=request.user,
            pilot_function=pilot_function,
            aircraft=Aircraft.objects.get(registration=request.POST['aircraft_id']),
            departure_airfield=request.POST['departure_airfield'],
            arrival_airfield=request.POST['arrival_airfield'],
            off_blocks=request.POST['off_blocks'],
            on_blocks=request.POST['on_blocks'],
            n_landings=request.POST['landings'],
            norm_type=norm_type
        )

        for exercise_id, grade in grades.items():
            ex = Exercise.objects.get(id=exercise_id)
            comment = request.POST.get(f'comment_{exercise_id}', '')
            ExerciseResult.objects.create(
                flight_result=flight_result,
                exercise=ex,
                grade=grade,
                comment=comment if comment else ""
            )
        return redirect('/')  # success

    return render(request, "logflight.html", {
        "aircrafts": aircrafts,
        "pilots": pilots,
        "functions": functions,
        "norms": norms,
        "scores": grading_choices,
        "grade_labels": grade_labels,
        "norm_type": norm_type,
        "selected_pilot": selected_pilot,
        "form_data": {},
        "form_grades_json": "{}",  # Also helpful
    })


@login_required
def get_lesson_scores(request, pilot_id):
    # 1) grab all results for this pilot, newest‐first
    results = ExerciseResult.objects.filter(
        flight_result__pilot_id=pilot_id
    ).order_by('-flight_result__on_blocks')  # or '-id'

    # 2) collect up to the last three grades per exercise
    last_three_map = defaultdict(list)
    latest_comments = {}

    for er in results:
        ex_id = er.exercise_id
        if len(last_three_map[ex_id]) < 3:
            last_three_map[ex_id].append(er.grade)
        if er.grade <= 2 and ex_id not in latest_comments and er.comment:
            latest_comments[ex_id] = er.comment

    # 3) build pilot_scores
    lesson_scores = {}
    for ex_id, last_three in last_three_map.items():
        last_three = list(reversed(last_three))  # now newest is first

        highest = ExerciseResult.objects.filter(
            flight_result__pilot_id=pilot_id,
            exercise_id=ex_id
        ).aggregate(max_grade=Max('grade'))['max_grade'] or 0

        lesson_scores[str(ex_id)] = {
            'highest_score': highest,
            'last_score': last_three[0],  # now correct: most recent
            'last_three': last_three,
            'latest_comment': latest_comments.get(ex_id, "")
        }

    return JsonResponse(lesson_scores)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('account_dashboard'))
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def home(request):
    return render(request, 'home.html')


class GrantAccessForm(forms.ModelForm):
    allowed_instructors = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(groups__name='Instructor'),
        widget=forms.Select,
        required=False,
        label="Select instructors who can access your account"
    )

    class Meta:
        model = CustomUser
        fields = ['allowed_instructors']


@login_required
def grant_instructor_access(request):
    pilot = request.user
    # Instructors not in the same club
    instructors = CustomUser.objects.filter(
        groups__name='Instructor'
    ).exclude(club=pilot.club)

    if request.method == 'POST':
        instructor_id = request.POST.get('allowed_instructor')
        if instructor_id:
            instructor = get_object_or_404(CustomUser, pk=instructor_id)
            pilot.allowed_instructors.add(instructor)
        return redirect('/account')

    return render(request, 'dashboard/grant_access.html', {
        'instructors': instructors,
    })


def compute_lesson_scores(pilot):
    # Mirror your existing get_lesson_scores logic (but return dict)
    qs = ExerciseResult.objects.filter(flight_result__pilot=pilot)
    scores = {}
    for er in qs:
        ex_id = er.exercise.id
        if ex_id not in scores:
            scores[ex_id] = {'highest_score': er.grade, 'last_score': er.grade}
        else:
            scores[ex_id]['highest_score'] = max(scores[ex_id]['highest_score'], er.grade)
            scores[ex_id]['last_score'] = er.grade
    return scores


@login_required
def lesson_progress(request):
    user = request.user

    # — select current pilot —
    pilot = None
    allowed_pilots = None
    if user.is_instructor:
        student_group = Group.objects.get(name="Student")

        club_qs = CustomUser.objects.filter(
            club=user.club,
            groups=student_group
        ).exclude(pk=user.pk)

        granted_qs = CustomUser.objects.filter(
            allowed_instructors=user,
            groups=student_group
        )

        allowed_pilots = (club_qs | granted_qs).distinct()

        pid = request.GET.get("pilot_id")
        if pid:
            pilot = get_object_or_404(CustomUser, pk=pid, groups=student_group)
    else:
        pilot = user

    # — helper: sum block-time —
    def sum_block_time(qs):
        return (
            qs.annotate(
                block_duration=ExpressionWrapper(
                    F('on_blocks') - F('off_blocks'),
                    output_field=DurationField()
                )
            )
            .aggregate(total=Sum('block_duration'))['total']
            or timedelta()
        )

    # — compute stats & exercise-scores with last_three —
    if pilot:
        base_qs = pilot.flight_pilot.all()

        # block-time and landings totals
        total_bt = sum_block_time(base_qs)
        dual_bt  = sum_block_time(base_qs.filter(pilot_function='Dual'))
        pic_bt   = sum_block_time(base_qs.filter(pilot_function='PIC'))

        total_ld = base_qs.aggregate(total=Sum('n_landings'))['total'] or 0
        dual_ld  = base_qs.filter(pilot_function='Dual').aggregate(total=Sum('n_landings'))['total'] or 0
        pic_ld   = base_qs.filter(pilot_function='PIC').aggregate(total=Sum('n_landings'))['total'] or 0

        # build per-exercise last_three + highest_score
        last_three_map = defaultdict(list)
        results = ExerciseResult.objects.filter(
            flight_result__pilot=pilot
        ).order_by('-flight_result__on_blocks')  # newest first

        for er in results:
            ex = er.exercise_id
            if len(last_three_map[ex]) < 3:
                last_three_map[ex].append(er.grade)

        scores = {}
        for ex_id, last_three in last_three_map.items():
            highest = ExerciseResult.objects.filter(
                flight_result__pilot=pilot,
                exercise_id=ex_id
            ).aggregate(max_grade=Max('grade'))['max_grade'] or 0

            last_three = list(reversed(last_three))  # make newest first!

            scores[ex_id] = {
                'highest_score': highest,
                'last_score': last_three[0],
                'last_three': last_three,
            }
    else:
        total_bt = dual_bt = pic_bt = timedelta()
        total_ld = dual_ld = pic_ld = 0
        scores = {}

    # format hh:mm
    def fmt(td: timedelta) -> str:
        secs = int(td.total_seconds())
        h, rem = divmod(secs, 3600)
        m = rem // 60
        return f"{h:02}:{m:02}"

    pilot_data = {
        'full_name':        pilot.full_name if pilot else '',
        'total_block_time': fmt(total_bt),
        'dual_block_time':  fmt(dual_bt),
        'pic_block_time':   fmt(pic_bt),
        'total_landings':   total_ld,
        'dual_landings':    dual_ld,
        'pic_landings':     pic_ld,
    }

    # AJAX JSON response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'pilot': pilot_data,
            'scores':  scores,
        })

    # initial page render
    norms = Norm.objects.prefetch_related('exercises').filter(norm_type="lesson").order_by('id')
    return render(request, "account/lesson_progress.html", {
        'allowed_pilots':    allowed_pilots,
        'selected_pilot_id': pilot.pk if pilot and user.is_instructor else None,
        'initial_pilot':     pilot_data,
        'initial_scores':      scores,
        'norms':               norms,
        'scores':              [1, 2, 3],
    })


@login_required
def skilltest_form(request):
    return render(request, "skilltest_form.html")


@login_required
def logbook_view(request):
    flights = FlightResult.objects.filter(pilot=request.user).select_related('instructor', 'aircraft').order_by('-off_blocks')
    logs = []
    total_time = training_time = solo_time = 0

    for flight in flights:
        duration_seconds = (flight.on_blocks - flight.off_blocks).total_seconds()
        duration_hours = duration_seconds / 3600
        total_time += duration_hours

        # Time classification
        if flight.pilot_function == "PIC":
            tag = "Solo"
            solo_time += duration_hours
        elif flight.pilot_function == "Skill Test":
            tag = "Skill Test"
        elif flight.pilot_function == "PFT":
            tag = "PFT"
        else:
            tag = "Flying Lesson"
            training_time += duration_hours

        # Norms & Exercises with comments
        exercises = ExerciseResult.objects.filter(flight_result=flight).select_related('exercise__norm')
        norm_entries = [
            {
                "title": f"{e.exercise.norm.title}: {e.exercise.title}",
                "grade": e.grade,
                "comment": e.comment if e.comment else ""
            }
            for e in exercises
        ]

        logs.append({
            "date": localtime(flight.off_blocks).strftime("%B %d, %Y"),
            "aircraft": flight.aircraft.registration,
            "aircraft_type": flight.aircraft.type,
            "duration": f"{int(duration_seconds // 3600):02}:{int((duration_seconds % 3600) // 60):02}",
            "instructor": flight.instructor.full_name if flight.instructor else "N/A",
            "departure_time": localtime(flight.off_blocks).strftime("%H:%M"),
            "departure_airfield": flight.departure_airfield,
            "arrival_time": localtime(flight.on_blocks).strftime("%H:%M"),
            "arrival_airfield": flight.arrival_airfield,
            "notes": f"{flight.n_landings} landings",
            "tag": tag,
            "norms": norm_entries,
        })

    context = {
        "total_hours": f"{int(total_time):02}:{int((total_time * 60) % 60):02}",
        "solo_hours": f"{int(solo_time):02}:{int((solo_time * 60) % 60):02}",
        "training_hours": f"{int(training_time):02}:{int((training_time * 60) % 60):02}",
        "flight_logs": logs,
    }
    return render(request, "account/logbook.html", context)

