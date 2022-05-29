from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, views, permissions
from rest_framework import status
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from auth_service.utils import Util
from auth_service.serializers import (ResetPasswordEmailRequestSerializer,
                                      SetNewPasswordSerializer, LoginUserSerializer)
from users.models import User
from users.serializers import UserSerializer


class CreateUserAPIView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        knox_object = AuthToken.objects.create(user)
        access_token = knox_object[1]
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify', args=[knox_object[0].digest])
        abs_url = f'http://{current_site}{relative_link}'
        email_body = f'Hi, {user.first_name}.Use the link below to verify your email \n{abs_url}'
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Registration'}
        Util.send_email(data)
        response_data = {
            'access_token': access_token,
            'expiry': knox_object[0].expiry,
            'user': user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": str(user.phone),
            "role": user.role
        }
        return Response({"user": data})


class VerifyEmail(views.APIView):

    def get(self, request, *args, **kwargs):
        data = AuthToken.objects.filter(digest=kwargs.get('token')).first()
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
        relative_link = reverse('password-reset-confirm')
        absurl = f'http://{current_site}{relative_link}'
        email_body = f'Hi {user.first_name}. Use link below to verify your email.\n{absurl}'
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response({'success': 'We send you a link.Now you can change a password'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        body = request.data
        user = self.request.user
        password = body['password']
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(password)
        user.save()
        return Response({"success": "Password Reset Successfully"}, status=status.HTTP_200_OK)
