from django.urls import path, include
from .views import CreateUserAPIView

urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='user_signup'),
    path('api/token/', include('auth_service.urls'))
]
