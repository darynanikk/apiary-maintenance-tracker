from rest_framework import serializers
from apiaries.models import Apiary


class CreateApiarySerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()

    class Meta:
        model = Apiary
        fields = ['name',
                  'isHidden',
                  'status',
                  'location',
                  ]


class UpdateDestroyApiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Apiary
        fields = ['name',
                  'isHidden',
                  'status',
                  'location',
                  ]

        extra_kwargs = {
            'name': {'required': False},
            'isHidden': {'required': False},
            'status': {'required': False},
            'location': {'required': False}
        }


class ListApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiary
        fields = '__all__'
