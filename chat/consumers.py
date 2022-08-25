from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.session = None

    
    def connect(self):
        print('------------- CONNECT FUNCTION --------------------')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = f"chat_{self.room_name}"


        # Joining room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'user_has_joined',
            }
        )


    def disconnect(self, close_code):
        print('------------- DISCONNECT FUNCTION --------------------')

        # Closing the group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'user_has_leaved',
            }
        )
            

    def receive(self, text_data):
        print('------------- RECEIVE FUNCTION --------------------')
        data = json.loads(text_data)
        message = data['message']
        user = data['user']

        # Initializing the current user
        self.user = user

        print('data: ', data)
        print('msg: ', message)
        print('user: ', user)

        async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': self.user,
                }
            )

            
    def chat_message(self, event):
        print('------------- CHAT MESSAGE FUNCTION --------------------')
        message = event['message'].strip()
        user = event['user']

        print('EVENT ', event)
        print('MESSAGE ', message)
        print('USER ', user)

        # Sending message to WebSocket again
        self.send(text_data=json.dumps({
            'dj-message': 'this is sent by the chat message function',
            'message': message,
            'user': user,
        }))
            

    def user_has_joined(self, event):
        print('------- USER HAS JOINED FUNCTION -----------')
        print('USER JOINED')


    def user_has_leaved(self, event):
        print('------- USER HAS LEAVED FUNCTION -----------')
        print('USER LEAVED')