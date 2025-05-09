from django.shortcuts import get_object_or_404, render

from .models import Norm, Plane


def log_flight(request):
    planes = Plane.objects.all()
    norms = Norm.objects.prefetch_related('exercises').all()
    return render(request, 'flight_log.html', {'planes': planes, 'norms': norms})

