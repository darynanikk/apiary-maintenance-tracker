from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView, ForgotPasswordView, PasswordTokenCheckAPI, SetNewPasswordAPIView, VerifyEmail, \
    CreateUserAPIView, LoginAPIView

urlpatterns = [
    path('', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUserAPIView.as_view(), name='user_signup'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', ForgotPasswordView.as_view(), name='request-reset-email'),
    path('password-reset/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete')
]