import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import base64
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        if(message_type == 'status'):
            
            raw_image = text_data_json['data']['img'] 
            
            # raw_image = '/9j/4AAQSkZJRgABAQAAAQABAAD/
            # save the image
            # change the image to base64
            raw_image = base64.b64decode(raw_image)
            with open('image.png', 'wb') as f:
                f.write(raw_image)
        
        # self.send(text_data=json.dumps({'message':message}))
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type':'chat_message',
        #         'message':message
        #     }
        # )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))