import datetime
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, views
from rest_framework import status
from knox.views import LoginView as KnoxLoginView

from auth_service.utils import Util
from auth_service.serializers import (ResetPasswordEmailRequestSerializer,
                                      SetNewPasswordSerializer)
from users.models import User
from users.serializers import UserSerializer


class CreateUserAPIView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        current_site = get_current_site(request).domain
        knox_obj = AuthToken.objects.create(user, expiry=datetime.timedelta(minutes=3))
        relative_link = reverse('email-verify', kwargs={'token': knox_obj[0].digest})
        abs_url = f'http://{current_site}{relative_link}'
        email_body = f'Hi, {user.first_name}.Use the link below to verify your email \n{abs_url}'
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Registration'}
        Util.send_email(data)
        response_data = {
            'user': user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginAPIView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def get_post_response_data(self, request, token, instance):
        data = super().get_post_response_data(request, token, instance)
        data["user"].pop("password")
        user_email = data["user"]["email"]
        user_instance = User.objects.get(email=user_email)
        data["user"] = {
            "first_name": user_instance.first_name,
            "last_name": user_instance.last_name,
            "email": user_instance.email,
            "phone": str(user_instance.phone),
            "role": user_instance.role
        }
        return data

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)


class VerifyEmail(views.APIView):

    def get(self, request, *args, **kwargs):
        data = AuthToken.objects.filter(digest=kwargs.get('token')).first()
        if data is None:
            return Response("Token is expired.")
        email = data.user
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        return Response({'verify': True})


class ForgotPasswordView(views.APIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        current_site = get_current_site(request=request).domain
        knox_object = AuthToken.objects.create(user, expiry=datetime.timedelta(minutes=3))
        relative_link = reverse('password-reset-confirm', kwargs={'token': knox_object[0].digest})
        absurl = f'http://{current_site}{relative_link}'
        email_body = f'Hi {user.first_name}. Use link below to verify your email.\n{absurl}'
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response({'success': 'We send you a link.Now you can change a password'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def put(self, request, *args, **kwargs):
        data = AuthToken.objects.filter(digest=kwargs.get('token')).first()
        if data is None:
            return Response("Token is expired.")
        user = data.user
        body = request.data
        password = body['password']
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(password)
        user.save()
        return Response(
            {"success": "Password Reset Successfully"},
            status=status.HTTP_200_OK)
