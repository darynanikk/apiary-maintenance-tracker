from django.urls import path
from .views import ForgotPasswordView, SetNewPasswordAPIView, VerifyEmail, \
    CreateUserAPIView, LoginAPIView

urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='user_signup'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', ForgotPasswordView.as_view(), name='request-reset-email'),
    path('password-reset/', SetNewPasswordAPIView.as_view(), name='password-reset-confirm')
]