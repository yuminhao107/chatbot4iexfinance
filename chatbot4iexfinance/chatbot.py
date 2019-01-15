from data.state import *
import re

# key for nlp output
INTENT='intent'
NAME='name'
CONFIDENCE='confidence'
ENTITIES='entities'
ENTITY='entity'
VALUE='value'
PENDING='pending'
HANDLER='handler'
PRECONDITION='precondition'

class Chatbot:
    
    def __init__(self,interpreter):
        print('Create a new chatbot.')
        self.interpreter=interpreter
        self.state=STATE_INIT
        self.keys={
            # STOCK_LIST:None,
            # START_TIME:None,
            # END_TIME:None,
            # USER:None
            PENDING:False
            }

    def respond(self,msg):
        print('User: {}'.format(msg))
        reply_msg=self.normal_nlp(msg)
        print('Bot : {}'.format(reply_msg))
        return reply_msg

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

    def process(self,msg):
        self.normal_nlp(msg)


    def normal_nlp(self,msg):
        nlp_result=self.interpreter.parse(msg)
        
        user_intent=nlp_result[INTENT][NAME]
        
        user_stocks=[]
        for enti in  nlp_result[ENTITIES]:
            if enti[ENTITY]==ENTITY_STOCK:
                user_stocks.append(enti[VALUE])
            else:
                self.keys[enti[ENTITY]]=str(enti[VALUE])
        
        re_stock=re.findall("[-|A-Z]{2,8}",msg)
        user_stocks.extend(re_stock)
        if len(user_stocks)>0:
            self.keys[STOCK_LIST]=user_stocks

        precondition,handler=PROPERTY_OF_ACTION[user_intent]
        if self.keys[PENDING]:
            precondition=self.keys[PRECONDITION]
            handler=self.keys[HANDLER]
        for key in precondition:
            if not key in self.keys:
                if (not self.keys[PENDING]):
                    self.keys[PENDING]=True
                    self.keys[HANDLER]=handler
                    self.keys[PRECONDITION]=precondition
                    return choice(ASK_FOR_INFORMATION[key])

        return handler(self.keys)



    def greet():
        return "hello, this is a chatbot for iexfinance. You can ask me something about the stock market. Just try to input 'price of TSLA'"

        
        
        