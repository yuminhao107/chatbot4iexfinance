from data.state import *

# key for nlp output
INTENT='intent'
NAME='name'
CONFIDENCE='confidence'


class Chatbot:
    
    def __init__(self,interpreter):
        print('Create a new chatbot.')
        self.interpreter=interpreter
        self.state=STATE_INIT
        self.keys={
            STOCK_LIST:[],
            START_TIME:None,
            END_TIME:None,
            USER:None
            }

    def respond(self,msg):
        return self.simple_nlp(msg)

    # only for test
    def simple_repeat(self,msg):
        template='You just said:"{}"'
        return template.format(msg)
        
    # only for test
    def simple_nlp(self,msg):
        result=self.interpreter.parse(msg)
        return result[INTENT][NAME]+'__'+str(result[INTENT][CONFIDENCE])

    def get_state(self):
        self.state

    def normal_nlp(self,msg):
        nlp_result=self.interpreter.parse(msg)
        user_intent=nlp_result[INTENT][NAME]

    def greet():
        return "hello"

        
        
        