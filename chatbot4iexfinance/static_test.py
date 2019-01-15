from chatbot import Chatbot

messages=[
    'hi',
    'i want to know something about the market',
    'what about TSLA today',
    'open price',
    'what about TSLA'
]

def static_test(interpreter):
    chatbot=Chatbot(interpreter)
    for msg in messages:
        chatbot.respond(msg)