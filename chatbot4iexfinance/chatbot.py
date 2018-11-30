from data.state import *

INTENT='intent'
NAME='name'
CONFIDENCE='confidence'

class Chatbot:
    
    def __init__(self,interpreter):
        print('Create a new chatbot.')
        self.interpreter=interpreter
        self.state=STATE_INIT

    def respond(self,msg):
        return self.simple_nlp(msg)

    def simple_repeat(self,msg):
        template='You just said:"{}"'
        return template.format(msg)
        
    def simple_nlp(self,msg):
        result=self.interpreter.parse(msg)
        return result[INTENT][NAME]+'__'+str(result[INTENT][CONFIDENCE])

    def get_state(self):
        self.state