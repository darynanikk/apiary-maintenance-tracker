from rest_framework import serializers
from apiaries.models import Apiary


class CreateApiarySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()

    class Meta:
        model = Apiary
        fields = ['name',
                  'isHidden',
                  'status',
                  'location',
                  'user'
                  ]


class ListApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiary
        fields = '__all__'
