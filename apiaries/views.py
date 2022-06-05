from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(kwargs.get("pk"), status=status.HTTP_204_NO_CONTENT)
