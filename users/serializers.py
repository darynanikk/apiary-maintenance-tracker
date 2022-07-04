from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'password',
            'role',
            'created_at'
        )

    extra_kwargs = {
        'password': {'write_only': True},
        'created': {'read_only': True}
    }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
