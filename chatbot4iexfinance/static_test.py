from chatbot import Chatbot

messages=[
    'hi',
    'i want to know something about the market',
    'what about AAPL today',
    'volume',
    'the open price of TSLA and GOOG, please.',
    'the interest of ABCDEF',
    'MSFT',
    'end'
]

def static_test(interpreter):
    chatbot=Chatbot(interpreter)
    for msg in messages:
        chatbot.respond(msg)