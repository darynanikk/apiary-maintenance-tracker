from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CreateHiveSerializer, ListHiveSerializer, \
    UpdateDestroyHiveSerializer

from .models import Hive


# Create your views here.
class CreateHiveAPIView(generics.CreateAPIView):
    queryset = Hive.objects.all().select_related("apiary")
    serializer_class = CreateHiveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ListHiveAPIView(generics.ListAPIView):
    queryset = Hive.objects.all().select_related("apiary")
    serializer_class = ListHiveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UpdateHiveAPIView(generics.UpdateAPIView):
    queryset = Hive.objects.all()
    serializer_class = UpdateDestroyHiveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DeleteHiveAPIView(generics.DestroyAPIView):
    queryset = Hive.objects.all()
    serializer_class = UpdateDestroyHiveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(kwargs.get("pk"), status=status.HTTP_204_NO_CONTENT)
