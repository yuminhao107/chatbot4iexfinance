from iexfinance import get_available_symbols
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
available_symbols=[]

def load_symbols():
     # load symbos
    global available_symbols
    stocks=get_available_symbols()
    for stock in stocks:
        available_symbols.append(stock['symbol'])
    print('Load symbols success.')


def varify_symbols(symbols):
    valid=[]
    invalid=[]
    for symbol in symbols:
        if symbol in available_symbols:
            valid.append(symbol)
        else:
            invalid.append(symbol)
    return valid, invalid

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
        
        precondition,handler=PROPERTY_OF_ACTION[user_intent]
        #  check invalid symbols
        valid,invalid=varify_symbols(user_stocks)
        if len(invalid)>0:
            if (not self.keys[PENDING]):
                    self.keys[PENDING]=True
                    self.keys[HANDLER]=handler
                    self.keys[PRECONDITION]=precondition
            return "Invalid Stock symbol(s). Please give me the right symbol."
        # check and merge
        if len(valid)>0:
            self.keys[STOCK_LIST]=user_stocks
        # reload the pending handler
        if self.keys[PENDING]:
            precondition=self.keys[PRECONDITION]
            handler=self.keys[HANDLER]
        # check if all slots if filled for the handler 
        for key in precondition:
            if not key in self.keys:
                if (not self.keys[PENDING]):
                    self.keys[PENDING]=True
                    self.keys[HANDLER]=handler
                    self.keys[PRECONDITION]=precondition
                return choice(ASK_FOR_INFORMATION[key])
        
        self.keys[PENDING]=False

        return handler(self.keys)



    def greet():
        return "hello, this is a chatbot for iexfinance. You can ask me something about the stock market. Just try to input 'price of TSLA'"

        
        
        