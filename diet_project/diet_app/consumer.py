import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import Messages,Room
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.core import serializers

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )





    def save_message(self):
        room = Room.objects.get(id=self.room_id)

        msg = Messages(text=self.message, sender=self.sender, room_id=room)
        msg.save()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['code'] == 'new_message':
            message = text_data_json['message']
            name = text_data_json['name']
            room_id = text_data_json['room']

            self.room_id = room_id
            self.message = message
            self.sender = name
            await database_sync_to_async(self.save_message)()
            # print(room)

            # await database_sync_to_async (self.save_message)()

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'name': name,
                    'room': room_id,
                    'code': text_data_json['code'],
                }
            )
        elif text_data_json['code'] == 'fetch_old':
            self.room_id_filter=text_data_json['room']
            self.code = text_data_json['code']
            self.name=text_data_json['name']
            await database_sync_to_async(self.fetch_messages)()

    def fetch_messages(self):
        code=self.code
        messages = []
        msgs = Messages.objects.filter(room_id=self.room_id_filter)
        self.response=None
        for m in msgs:
            messages.append({'name': m.sender, 'content': m.text})
            self.response = json.dumps({"messages": messages}, default=str)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'messages': self.response,
                'code': code,
                's_name':self.name
            }
        )
    # Receive message from room group
    async def chat_message(self, event):
        if event['code'] == "new_message":
            message = event['message']
            name=event['name']
            room_id=event['room']
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'name':name,
                'room': room_id,
                'code':event['code']
            }))
        else:
           await self.send(text_data=json.dumps({
                'message': self.response,
                's_name':event['s_name'],
                'code': event['code']
            }))