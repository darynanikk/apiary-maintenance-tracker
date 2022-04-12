from .serializers import UserSerializer
from .models import User
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class CreateUserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



