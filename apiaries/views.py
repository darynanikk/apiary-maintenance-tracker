from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apiaries.models import Apiary
from apiaries.serializers import ListApiarySerializer, UpdateDestroyApiarySerializer, CreateApiarySerializer

# Create your views here.


class CreateApiaryAPIView(generics.CreateAPIView):
    serializer_class = CreateApiarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        apiary = serializer.save(user=self.request.user, status="test", location={})
        data = {
            "name": apiary.name,
            "status": apiary.status,
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
    queryset = Apiary.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UpdateDestroyApiarySerializer(queryset)
        return Response(self.kwargs.get("pk"))


class DeleteApiaryAPIView(generics.DestroyAPIView):
    queryset = Apiary.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UpdateDestroyApiarySerializer(queryset)
        return Response(self.kwargs.get("pk"))
