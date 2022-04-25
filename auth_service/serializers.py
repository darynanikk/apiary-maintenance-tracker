from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers
from auth_service.utils import Util
from users.models import User


class ResetPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=2, required=True)

    class Meta:
        model = User
        fields = ['email']


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True, required=True)
    token = serializers.CharField(min_length=1, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password', 'token']


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

    def validate(self, attrs):
        password = attrs.get('password')
        email = attrs.get('email')
        validated_user = Util.get_validated_user(email, password)
        validated_data = Util.get_access(validated_user)
        return validated_data
