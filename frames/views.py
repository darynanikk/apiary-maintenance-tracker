from django.shortcuts import render
from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Frame
from .serializers import CreateFrameSerializer, ListFrameSerializer, UpdateDestroyFrameSerializer


# Create your views here.
class CreateFrameAPIView(generics.CreateAPIView):
    queryset = Frame.objects.all().select_related("hive")
    serializer_class = CreateFrameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ListFrameAPIView(generics.ListAPIView):
    queryset = Frame.objects.all().select_related("hive")
    serializer_class = ListFrameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ListUserFramesByHiveAPIView(generics.RetrieveAPIView):
    lookup_field = 'hive_id'
    serializer_class = ListFrameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Frame.objects.filter(hive=self.kwargs.get('hive_id'))


class UpdateFrameAPIView(generics.UpdateAPIView):
    queryset = Frame.objects.all()
    serializer_class = UpdateDestroyFrameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DeleteFrameAPIView(generics.DestroyAPIView):
    queryset = Frame.objects.all()
    serializer_class = UpdateDestroyFrameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(kwargs.get("pk"), status=status.HTTP_204_NO_CONTENT)
