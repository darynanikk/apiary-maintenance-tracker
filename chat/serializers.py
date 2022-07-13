from rest_framework import serializers
from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField(source='author.email')

    class Meta:
        model = Message
        fields = (
            'author_email',
            'content',
            'timestamp'
        )
