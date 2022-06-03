from rest_framework import serializers
from apiaries.models import Apiary


class CreateApiarySerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Apiary
        fields = ['name',
                  'is_hidden',
                  'status',
                  'location',
                  'user'
                  ]


class UpdateDestroyApiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Apiary
        fields = [
                  'pk',
                  'name',
                  'is_hidden',
                  'status',
                  'location',
                  ]

        extra_kwargs = {
            'name': {'required': False},
            'is_hidden': {'required': False},
            'status': {'required': False},
            'location': {'required': False}
        }


class ListApiarySerializer(serializers.ModelSerializer):
    #user_email = serializers.EmailField(source='user.email')

    class Meta:
        model = Apiary
        fields = [
                  'pk',
                  'name',
                  'is_hidden',
                  'status',
                  'location',
                  'user',
                  ]
