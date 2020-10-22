from django.urls import path, include
from .views import UserCreateView, home
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('accounts/signup/', UserCreateView.as_view(template_name="Task/signup.html"), name='signup'),
    path('accounts/login/', LoginView.as_view(template_name="Task/login.html"), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home, name='home'),
    path('password-reset/', PasswordResetView.as_view(template_name="Task/password_reset_form.html",
                                                      email_template_name="Task/password_reset_email.html"),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="Task/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="Task/password_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="Task/password_reset_complete.html"),
         name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(template_name='Task/password_change.html'),
         name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='Task/password_change_done.html'),
         name='password_change_done'),

]