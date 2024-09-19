import json

from channels.generic.websocket import AsyncWebsocketConsumer

messages_list = []
'''class WSConsumerChat(AsyncWebsocketConsumer):
    print('Sono in consumers')
    async def connect(self):
        await self.accept()
        await self.send("SERVER: Eccoti connesso!")

    async def receive(self, text_data=None, bytes_data=None):
        if text_data == "UPDATE":
            stot = ""
            for m in messages_list:
                stot += m["user"] + ": " + m["msg"] + "\n"
            await self.send(stot)
        else:
            if text_data is not None:
                messages_list.append(json.loads(text_data))

        if len(messages_list) > 20:
            messages_list.clear()'''

class WSConsumerChat(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']
        await self.send(text_data=json.dumps({
            'msg': message
        }))