# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
from chat.models import Message
from users.models import User
from .serializers import MessageSerializer
from channels.auth import login, logout


class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = Message.last_10_messages()
        serializer = MessageSerializer(instance=messages, many=True)
        content = {
            'messages': serializer.data
        }
        self.send_message(content)

    def new_message(self, data):
        email = self.user.email
        author_user = get_object_or_404(User, email=email)
        message = Message.objects.create(
            author=author_user,
            content=data['message']
        )
        serializer = MessageSerializer(instance=message)
        content = {
            'command': 'new_message',
            'message': serializer.data
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        print(self.scope)
        self.user= self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
