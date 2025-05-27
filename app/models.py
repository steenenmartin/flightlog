from datetime import timedelta

from django.contrib.auth.base_user import BaseUserManager
from django.db.models import ExpressionWrapper, F, Sum, DurationField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.db import models

from app.utils import format_hhmm

UL_CLASS_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
]

PILOT_FUNCTIONS = [
    ('Dual', 'Dual'),
    ('PIC', 'PIC'),
]

NORM_TYPES = [
    ('lesson', 'lesson'),
    ('skilltest', 'skilltest'),
    ('pft', 'pft'),
]

class Aircraft(models.Model):
    registration = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.registration


class Norm(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    longdescription = models.TextField(blank=True)

    ul_class = models.CharField(
        max_length=1,
        choices=UL_CLASS_CHOICES,
        default='B'
    )

    norm_type = models.CharField(max_length=100, choices=NORM_TYPES)

    def __str__(self):
        return f"{self.title} ({self.norm_type})"

class Exercise(models.Model):
    norm = models.ForeignKey(Norm, related_name='exercises', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    longdescription = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)  # 👈 Add this

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email (make it case-insensitive)
        email = self.normalize_email(email)

        # Create the user instance
        user = self.model(email=email, **extra_fields)

        # Set the password for the user (make sure it’s hashed)
        user.set_password(password)

        # Save the user instance
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    full_name = models.CharField(_("full name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"),
        unique=True,
        db_collation="und-x-icu",  # Make email case-insensitive
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    club = models.CharField(max_length=255)

    ul_class = models.CharField(
        max_length=1,
        choices=UL_CLASS_CHOICES,
        default='B'
    )

    # Grant specific instructors access to this pilot
    allowed_instructors = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='pilots_who_granted_access',
        blank=True,
        limit_choices_to={'is_instructor': True}
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # Define manager (you already have this, presumably)
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def is_student(self):
        return self.groups.filter(name='Student').exists()

    @property
    def is_pilot(self):
        return self.groups.filter(name='Pilot').exists()

    @property
    def is_instructor(self):
        return self.groups.filter(name='Instructor').exists()

    @property
    def is_examiner(self):
        return self.groups.filter(name='Examiner').exists()

    @property
    def is_uddannelseschef(self):
        return self.groups.filter(name='Uddannelseschef').exists()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_flight_summary(self, pilot=None):
        if not pilot:
            pilot = self

        if self.is_uddannelseschef:
            flights = FlightResult.objects.filter(pilot=pilot)
        elif self.is_instructor:
            flights = FlightResult.objects.filter(instructor=self, pilot=pilot)
        else:
            flights = FlightResult.objects.filter(pilot=pilot)

        flights = flights.select_related('instructor', 'aircraft').order_by('-off_blocks')

        total_time = dual_time = pic_time = 0
        total_landings = dual_landings = pic_landings = 0

        for flight in flights:
            duration_seconds = (flight.on_blocks - flight.off_blocks).total_seconds()
            duration_hours = duration_seconds / 3600
            total_time += duration_hours
            total_landings += flight.n_landings

            if flight.norm_type == "lesson":
                if flight.pilot_function == "PIC":
                    pic_time += duration_hours
                    pic_landings += flight.n_landings
                else:
                    dual_time += duration_hours
                    dual_landings += flight.n_landings
            elif flight.norm_type in ("skilltest", "pft"):
                dual_time += duration_hours
                dual_landings += flight.n_landings
            else:
                # Treat other types as dual unless you want something different
                dual_time += duration_hours
                dual_landings += flight.n_landings

        return {
            "total_hours": format_hhmm(total_time),
            "dual_hours": format_hhmm(dual_time),
            "pic_hours": format_hhmm(pic_time),
            "total_landings": total_landings,
            "dual_landings": dual_landings,
            "pic_landings": pic_landings,
        }


class FlightResult(models.Model):
    pilot = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="flight_pilot")
    instructor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="flight_instructor")
    pilot_function = models.CharField(max_length=100, choices=PILOT_FUNCTIONS)
    norm_type = models.CharField(max_length=100, choices=NORM_TYPES)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.DO_NOTHING)
    departure_airfield = models.CharField(max_length=255)
    arrival_airfield = models.CharField(max_length=255)
    off_blocks = models.DateTimeField()
    on_blocks = models.DateTimeField()
    n_landings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ExerciseResult(models.Model):
    flight_result = models.ForeignKey(FlightResult, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    grade = models.IntegerField(choices=[(1, "1"), (2, "2"), (3, "3")])
    comment = models.TextField(blank=True)
