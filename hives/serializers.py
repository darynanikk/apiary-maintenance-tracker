from rest_framework import serializers
from .models import Hive


class CreateHiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hive
        fields = ['color',
                  'apiary',
                  'type',
                  'status',
                  'bees_family',
                  'number',
                  ]

        extra_kwargs = {
            'type': {'required': True},
            'number': {'required': True},
            'color': {'required': False},
            'apiary': {'required': True},
            'bees_family': {'required': False}
        }


class ListHiveSerializer(serializers.ModelSerializer):
    apiary = serializers.ReadOnlyField(source='apiary.name')

    class Meta:
        model = Hive
        fields = ['pk',
                  'color',
                  'apiary',
                  'type',
                  'status',
                  'bees_family',
                  'number',
                  ]


class UpdateDestroyHiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hive
        fields = ['color',
                  'apiary',
                  'type',
                  'status',
                  'bees_family',
                  'number',
                  ]

        extra_kwargs = {
            'type': {'required': False},
            'number': {'required': False},
            'color': {'required': False},
            'apiary': {'required': False},
            'bees_family': {'required': False}
        }
