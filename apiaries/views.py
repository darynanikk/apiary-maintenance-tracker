from knox.auth import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apiaries.models import Apiary
from apiaries.serializers import ListApiarySerializer, UpdateDestroyApiarySerializer, CreateApiarySerializer

# Create your views here.


class CreateApiaryAPIView(generics.CreateAPIView):
    queryset = Apiary.objects.all().select_related('user')
    serializer_class = CreateApiarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListApiaryAPIView(generics.ListAPIView):
    serializer_class = ListApiarySerializer
    queryset = Apiary.objects.all().select_related('user')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UpdateApiaryAPIView(generics.UpdateAPIView):
    queryset = Apiary.objects.all()
    serializer_class = UpdateDestroyApiarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DeleteApiaryAPIView(generics.DestroyAPIView):
    queryset = Apiary.objects.all()
    serializer_class = UpdateDestroyApiarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
