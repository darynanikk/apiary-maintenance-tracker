from django.contrib.auth import authenticate
from knox.models import AuthToken
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from users.models import User


class ResetPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=2, required=True)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, data):
        user = User.objects.get(email=data['email'])
        if user:
            user.is_verified = True
            return user
        raise serializers.ValidationError("User with entered email does not exist. Check your inputs")


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password']


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=40, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True}
        }

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_verified:
            return user
        raise serializers.ValidationError("Incorrect credentials or user email is not verified.")
