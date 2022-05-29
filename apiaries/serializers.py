from rest_framework import serializers
from apiaries.models import Apiary


class CreateUpdateDestroyApiarySerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()

    class Meta:
        model = Apiary
        fields = ['name',
                  'isHidden',
                  'status',
                  'location',
                  ]


class ListApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiary
        fields = '__all__'
