from chatbot import Chatbot

messages=[
    'hi',
    'i want to know something about the market',
    'what about AAPL today',
    'volume',
    'the price of TSLA and GOOG, please.'
]

def static_test(interpreter):
    chatbot=Chatbot(interpreter)
    for msg in messages:
        chatbot.respond(msg)