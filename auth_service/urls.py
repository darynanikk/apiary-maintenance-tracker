from django.urls import path, include
from knox.views import LogoutView

from .views import ForgotPasswordView, SetNewPasswordAPIView, VerifyEmail, \
    CreateUserAPIView, LoginAPIView

urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='user-signup'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('verify-email/<str:token>', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', ForgotPasswordView.as_view(), name='request-reset-email'),
    path('password-reset/<str:token>', SetNewPasswordAPIView.as_view(), name='password-reset-confirm'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
]