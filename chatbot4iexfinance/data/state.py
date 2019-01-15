from iexfinance import Stock
from random import choice

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
STATE_SEARCH=2
STATE_FINISHED=3

# define intent
INTENT_GREET='greet'
INTENT_GOODBYE='goodbye'
INTENT_SEARCH='search'
INTENT_SEARCH_VOLUME='search_volume'
INTENT_SEARCH_OPEN_PRICE='search_open'
INTENT_SEARCH_CLOSE_PRICE='search_close'
INTENT_SEARCH_INTEREST='search_interest'
INTENT_SEARCH_HISTORY='search_capitalization'
INTENT_SPECIFY_TIME='specify_time'
INTENT_AFFIRM='affirm'
INTENT_DENY='deny'
INTENT_CANCEL='cancel'
INTENT_ADD_FAVORATE='add_favorate'
INTENT_GET_FAVORATE='get_favorate'
INTENT_LOGIN='login'
INTENT_LOGOUT='logout'

# define entity name
ENTITY_COMPANY='company'
ENTITY_STOCK='stock'

def handler_init():
    templates=[]

def handler_login():
    raise NotImplementedError

def handler_get_intrst():
    raise NotImplementedError

def handler_get_history():
    raise NotImplementedError

def handler_get_price(keys):
    template=['The price of {0} is {1}. ',
    '{0} is {1}. ',
    '{0}\'price is {1}. '
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{0}.')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_open()
        text+=choice(template).format(stock_name,value)
    text+='You can also ask me for other information. Such as volume, open price, capitalization.'
    return text

def handler_get_volume(keys):
    template=['The volume of {0} is {1}. ',
    '{0} is {1}. ',
    '{0}\'volume is {1}. '
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{0}.')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_open()
        text+=choice(template).format(stock_name,value)
    return text

def handler_get_open_price(keys):
    template=['The open price of {0} is {1}. ',
    'Today\'s open price of {0} is {1}. ',
    '{0}\'open price is {1}. ',
    'Today is {1}. '
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{0}.')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_open()
        text+=choice(template).format(stock_name,value)
    return text
    

def handler_get_interest():
    raise NotImplementedError

def handler_get_close_price():
    raise NotImplementedError



# precondition,handler
PROPERTY_OF_INTENT={
    INTENT_LOGIN:([USER],handler_login),
    INTENT_GET_FAVORATE:([STOCK_LIST,],handler_get_intrst),
    INTENT_SEARCH_HISTORY:([STOCK_LIST,START_TIME,END_TIME],handler_get_history),
    INTENT_SEARCH:([STOCK_LIST,],handler_get_price),
    INTENT_SEARCH_VOLUME:([STOCK_LIST,],handler_get_volume),
    INTENT_SEARCH_OPEN_PRICE:([STOCK_LIST,],handler_get_open_price),
    INTENT_SEARCH_CLOSE_PRICE:([STOCK_LIST,],handler_get_close_price),
    INTENT_SEARCH_INTEREST:([STOCK_LIST,],handler_get_interest)
}

ASK_FOR_INFORMATION={
    STOCK_LIST:['Which stock do you want to know?'],
    START_TIME:['Start from when?'],
    END_TIME:['End to when?'],
    USER:['You need to input your USERNAME for further operation.']
}


POLICY={
    (STATE_INIT,INTENT_GREET):STATE_INIT,
    (STATE_INIT,INTENT_LOGIN):STATE_USER,
    (STATE_INIT,INTENT_LOGIN):STATE_USER,
    (STATE_USER,INTENT_SEARCH):STATE_SEARCH

}