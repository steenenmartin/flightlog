from django.urls import path
from .views import log_flight


urlpatterns = [
    path('log-flight/', log_flight, name='flight_log'),
]

