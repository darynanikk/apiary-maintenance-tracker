from django.contrib.auth import authenticate
from rest_framework import serializers

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

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'),
                            email=email, password=password)
        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.", code='authorization')
        if not user.is_verified:
            raise serializers.ValidationError("Incorrect credentials or user email is not verified.",
                                              code='authorization')
        attrs['user'] = user
        return attrs
