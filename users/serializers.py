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
            'email',
            'password',
            'role',
            'date_joined'
        )

    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
