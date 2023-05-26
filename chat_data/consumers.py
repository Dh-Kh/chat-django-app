import json
from chat_data.models import MessageHistory, ChatNameHistory
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
            )
        await self.accept()
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
            )
    async def receive(self, text_data):
        username = self.scope['user'].username
        text_data_loads = json.loads(text_data)
        message = text_data_loads['message']
        message = (username + ": " + message)
        try:
            room_obj = await database_sync_to_async(
                ChatNameHistory.objects.get)(chat_name=self.room_name)
        except ChatNameHistory.DoesNotExist:
            room_obj = await database_sync_to_async(ChatNameHistory.objects.create)(chat_name=self.room_name)
        chat_data = MessageHistory(
            message=message,  
            chat_name=room_obj
            )
        await database_sync_to_async(chat_data.save)()
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
            )
    async def chat_message(self, event):
        username = self.scope['user'].username
        message = event['message']
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username      
            }))
     
   
    