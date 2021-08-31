from chatapp.models import Message, RoomName
import json
from asgiref.sync import async_to_sync
from channels.exceptions import DenyConnection
from channels.generic.websocket import WebsocketConsumer
from .serializers import MessageSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

from django.shortcuts import  get_object_or_404
class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        print("from consumer",self.scope['user'])
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        room = get_object_or_404(RoomName, room_name=self.room_name)
        queryset=room.room.all().order_by('-created_at')[:10]
        queryset2=sorted(queryset, key=lambda x: x.created_at)
        messages = MessageSerializer(queryset2, many=True)
        self.send(text_data=json.dumps(messages.data))

    def receive(self,text_data):
        data=json.loads(text_data)
        user=self.scope['user']
        room=RoomName.objects.get(room_name=self.room_name)
        msg=Message.objects.create(group=room,from_user=user,msg=data['msg'])
        room = get_object_or_404(RoomName, room_name=self.room_name)
        queryset=room.room.all()[:1]
        messages = MessageSerializer(queryset, many=True)
        # self.send(text_data=json.dumps(messages.data))
        return self.send_chat_message(messages.data)
        
    def disconnect(self, *args, **kwargs):
        print('disconnected')
    
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
    