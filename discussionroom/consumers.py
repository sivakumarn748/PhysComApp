import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer) :

    async def connect(self) :
        self.roomid = self.scope['url_route']['kwargs']['roomid']
        self.room_group_id = f"chat_{self.roomid}"
        sessid = self.scope['subprotocols'][0]
        user = await self.get_user(sessid)
        hasroom = await self.has_room()

        if (hasroom and user) : 
            # Join Room Group
            await self.channel_layer.group_add(self.room_group_id, self.channel_name)
            await self.accept()
        else : 
            self.close(404)
    
    async def close(self, close_code) :
        # Leave Room Group
        print(user, sessid)
        await self.channel_layer.group_discard(self.room_group_id, self.channel_name)        
        await self.disconnect(close_code)

    async def receive(self, text_data=None, bytes_data=None) :
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Verify Logged In
        user = await self.get_user(text_data_json['sessid'])
        if not user :
            # user = None
            await self.close(404)
        
        if text_data_json['type'] == 'message':
            await self.channel_layer.group_send(
                self.room_group_id, 
                {
                    "type": "chat.message",
                    "message": message
                }
            )
        if text_data_json['type'] == 'alert' :
            await self.channel_layer.group_send(
                self.room_group_id,
                {
                    "type": "chat.alert",
                    "message": message
                }
            )

    async def chat_message(self, event) :
        message = event['message']

        # Send message to Web Socket
        await self.send(text_data=json.dumps({
            "type": "message",
            "message": message
        }))

    async def chat_alert(self, event) :
        message = event['message']

        # Send message to Web Socket
        await self.send(text_data=json.dumps({
            "type": "alert",
            "message": message
        }))

    @database_sync_to_async
    def has_room(self) : 
        try:
            room = Room.objects.get(roomid=self.roomid)
            return True
        except Room.DoesNotExist:
            return False

    @database_sync_to_async
    def get_user(self, sessid) :
        try:
            user = User.objects.get(sessid=sessid)
            return user
        except User.DoesNotExist :
            return None
        except :
            return False