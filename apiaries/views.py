from django.shortcuts import render
from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apiaries.models import Apiary
from apiaries.serializers import ListApiarySerializer, CreateUpdateDestroyApiarySerializer

# Create your views here.
from users.models import User


class CreateApiaryAPIView(generics.CreateAPIView):
    serializer_class = CreateUpdateDestroyApiarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        apiary = serializer.save(user=self.request.user, status="test", location={
            'latitude': '123.0.3',
            'longitude': '123.566', 'address': 'Kyiv'})
        data = {
            "name": apiary.name,
            "status": apiary.status,
            "location": apiary.location
        }
        return Response(data, status=status.HTTP_201_CREATED)


class ListApiaryAPIView(generics.ListAPIView):
    serializer_class = ListApiarySerializer
    queryset = Apiary.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super(ListApiaryAPIView, self).list(request, *args, **kwargs)


class UpdateApiaryAPIView(generics.UpdateAPIView):
    serializer_class = CreateUpdateDestroyApiarySerializer
    queryset = Apiary.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return super(UpdateApiaryAPIView, self).put(request, *args, **kwargs)


class DeleteApiaryAPIView(generics.DestroyAPIView):
    serializer_class = CreateUpdateDestroyApiarySerializer
    queryset = Apiary.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
