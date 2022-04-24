from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage

from users.models import User


class Util:
    @classmethod
    def send_email(cls, data):
        subject = data['email_subject']
        receiver = data['to_email']
        message = data['email_body']
        msg = EmailMessage(
            subject=subject,
            body=message,
            from_email='daryna-admin@example.com',
            to=[receiver],
            reply_to=['daryna-admin@example.com'],
            headers={'Message-ID': 'foo'},
        )
        msg.send()

    @classmethod
    def get_access(cls, user):
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }
            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError('Credentials are incorrect.Check password or email.', 401)

    @classmethod
    def get_validated_user(cls, email, password):
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Credentials are invalid.', 401)
        return user

    @classmethod
    def confirm_token(cls, token):
        jwt_authenticator = JWTAuthentication()
        try:
            validated_token = jwt_authenticator.get_validated_token(token)
            email = jwt_authenticator.get_user(validated_token)
            user = User.objects.get(email=email)
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return user
        except InvalidToken:
            raise
        except AuthenticationFailed:
            raise
