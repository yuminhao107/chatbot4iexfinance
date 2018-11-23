import asyncio
import websockets
import json
import time
from chatbot import Chatbot
from rasa_nlu.model import Interpreter

ALLSOKETS = {}
SEVER_PORT=8765
interpreter=None

def add_connection(ws_id, ws):
    global ALLSOKETS
    ALLSOKETS[ws_id] = ws
    print(ALLSOKETS)


def filter_handle(ws_id):
    return ALLSOKETS.get(ws_id)

# def respond(msg):
#     template='You just said:"{}"'
#     return template.format(msg)

async def handler(websocket, path):
    chatbot=Chatbot(interpreter)
    while True:
        message = await websocket.recv()
        message = json.loads(message)
        new_message=chatbot.respond(message['msg'])
        await websocket.send(new_message)
        print('recv: ', message)
        print(time.time())

def main():
    global interpreter
    interpreter = Interpreter.load("./models/current/nlu")
    print('Load model success.')
    start_server = websockets.serve(
        handler,
        'localhost',
        SEVER_PORT,
        klass=websockets.WebSocketServerProtocol)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()