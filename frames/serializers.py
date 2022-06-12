from rest_framework import serializers
from .models import Frame


class CreateFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = '__all__'


class ListFrameSerializer(serializers.ModelSerializer):
    hive = serializers.ReadOnlyField(source='hive.number')

    class Meta:
        model = Frame
        fields = ['hive',
                  'type',
                  'status',
                  'weight',
                  'moveHistory'
                  ]


class UpdateDestroyFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ['hive',
                  'type',
                  'status',
                  'weight',
                  'moveHistory'
                  ]

        extra_kwargs = {
            'type': {'required': False},
            'status': {'required': False},
            'hive': {'required': False},
            'weight': {'required': False},
            'moveHistory': {'required': False}
        }
