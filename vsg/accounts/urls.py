from django.urls import path
import django.contrib.auth.views as auth_views

from . import views



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('profile', views.profile_view, name='profile'),

    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
