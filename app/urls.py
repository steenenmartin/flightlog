from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name="home"),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('account/', account_dashboard, name='account_dashboard'),
    path('account/logbook/', logbook_view, name='logbook'),
    path('account/lesson-progress/', lesson_progress, name='lesson_progress'),
    path('account/grant-access/', grant_instructor_access, name='grant_access'),

    path("logflight/<str:flight_type>/", log_flight_dispatch, name="log_flight"),
    path("logflight/<str:flight_type>/<int:flight_id>/", log_flight_dispatch, name="edit_flight"),
    path('get_lesson_scores/<int:pilot_id>/', get_lesson_scores, name='get_lesson_scores'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

