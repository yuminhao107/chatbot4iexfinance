from rasa_nlu.model import Interpreter
from web_server import start_web_server
from wechat_server import start_wechat_server
import sys
WECHAT='wechat'
WEB='web'
modes=[WECHAT,WEB]

def main():
    mode = sys.argv[1]
    if not mode in modes:
        print('invalid args. You should use (python main.py [web|wechat]).')
        return

    interpreter = Interpreter.load("./models/current/nlu")
    print('Load model success.')

    if mode==WEB:
        start_web_server(interpreter)
    if mode==WECHAT:
        start_wechat_server(interpreter)


if __name__ == '__main__':
    main()
    