from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'test_room'
        self.room_group_name = 'test_room_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status":"woh channels working"}))

    def receive(self,text_data):
        print("user received data--",text_data)
        self.send(text_data=json.dumps({"status":"we got your data"}))

    def disconnect(self,*args, **kwargs):
        print("channels disconnected")
