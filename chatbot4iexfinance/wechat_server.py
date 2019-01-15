from wxpy import *
from chatbot import Chatbot
chatbots={}

def start_wechat_server(interpreter):
    bot=Bot()
    
    @bot.register()
    def reply_messages(msg):
        print(msg)
        sender=msg.sender
        if sender in chatbots:
            sender.send(chatbots[sender].respond(msg.text))
        else:
            chatbot=Chatbot(interpreter)
            chatbots[sender]=chatbot
            sender.send(chatbot.greet())
        
    @bot.register(msg_types=FRIENDS)
    def auto_accept_friends(msg):
        # accept apply
        new_friend = msg.card.accept()
        # send new message
        new_friend.send('This is a chatbot. You can ask me questions about stock.')

    embed()


if __name__ == '__main__':
    start_wechat_server(None)