from chatbot4iexfinance.chatbot import Chatbot

# define parameter
STOCK_LIST='stock_list'
STOCK_NAME='stock_name'
START_TIME='start_time'
END_TIME='end_time'
USER='user'

# define action


# define state
STATE_INIT=0
STATE_USER=1
STATE_GET_PRICE=2
STATE_GET_HISTORY=3
STATE_GET_INTRST=4

# define intent
INTENT_GREET='greet'
INTENT_GOODBYE='goodbye'
INTENT_SEARCH='search'
INTENT_SPECIFY_TIME='specify_time'
INTENT_AFFIRM='affirm'
INTENT_DENY='deny'
INTENT_CANCEL='cancel'
INTENT_ADD_FAVORATE='add_favorate'

def handler_init():
    raise NotImplementedError

def handler_user():
    raise NotImplementedError

def handler_get_intrst():
    raise NotImplementedError

def handler_get_history():
    raise NotImplementedError

def handler_get_price():
    raise NotImplementedError

# precondition,handler
PROPERTY_OF_STATE={
    STATE_INIT:([],handler_init),
    STATE_USER:([USER],handler_init),
    STATE_GET_INTRST:([STOCK_LIST,],handler_init),
    STATE_GET_HISTORY:([STOCK_NAME,START_TIME,END_TIME],handler_init),
    STATE_GET_PRICE:([STOCK_LIST,],handler_init)
}

ASK_FOR_INFORMATION={
    STOCK_LIST:['Which stock do you want to know?'],
    START_TIME:['Start from when?'],
    END_TIME:['End to when?'],
    USER:['You need to input your USERNAME for further operation.']
}


POLICY={
    
}