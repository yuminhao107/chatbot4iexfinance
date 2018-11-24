class Chatbot:
    def __init__(self,interpreter):
        print('Create a new chatbot.')
        self.interpreter=interpreter

    def respond(self,msg):
        return self.simple_nlp(msg)

    def simple_repeat(self,msg):
        template='You just said:"{}"'
        return template.format(msg)
        
    def simple_nlp(self,msg):
        result=self.interpreter.parse(msg)
        return result['intent']['name']+'__'+str(result['intent']['confidence'])