class Chatbot:

    def __init__(self):
        print('Create a new chatbot.')

    def respond(self,msg):
        return self.simple_repeat(msg)

    def simple_repeat(self,msg):
        template='You just said:"{}"'
        return template.format(msg)
        