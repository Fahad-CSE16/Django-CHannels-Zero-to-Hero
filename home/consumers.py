from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json
class TestConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope['user'])
        self.room_name="test_room"
        self.group_room_name="test_group_room"
        async_to_sync(self.channel_layer.group_add)(
            self.group_room_name,  self.channel_name
        )
        
        self.accept()
        self.send(text_data=json.dumps({'status':'connected'}))

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=text_data)
        
    def disconnect(self, *args, **kwargs):
        print('disconnected')
        
    def send_notification(self,event):
        print(event)
        data=event.get('value')
        self.send(text_data=data)
        
class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("from consumer",self.scope['user'])
        self.room_name="new consumer"
        self.group_room_name="new_group_room"
        await(self.channel_layer.group_add)(
            self.group_room_name,  self.channel_name
        )
        
        await self.accept()
        await self.send(text_data=json.dumps({'status':'connected from sync consumer'}))

    async def receive(self,text_data):
        print(text_data)
        await self.send(text_data=text_data)
        
    async def disconnect(self, *args, **kwargs):
        print('disconnected')
        
    async def send_notification(self,event):
        # print(event)
        data=event.get('value')
        await self.send(text_data=data)