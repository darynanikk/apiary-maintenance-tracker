from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'password',
            'role',
            'date_joined'
        )
    extra_kwargs = {'password': {'write_only': True}}


