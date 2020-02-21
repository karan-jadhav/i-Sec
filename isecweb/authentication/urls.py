from django.urls import path
from . import views as view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', view.login_request, name='auth-login'),
    path('logout/', view.logout_request, name='auth-logout'),
    path('register/', view.signup_request, name='auth-register'),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), name='password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    #path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),
]
