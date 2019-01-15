from rasa_nlu.model import Interpreter
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from web_server import start_web_server
from wechat_server import start_wechat_server
from static_test import static_test
from chatbot import load_symbols
import sys

WECHAT='wechat'
WEB='web'
TEST='test'
modes=[WECHAT,WEB,TEST]

def main():
    if len(sys.argv)<2:
        print('invalid args. You should use (python main.py [web|wechat]).')
        return
    mode = sys.argv[1]
    if not mode in modes:
        print('invalid args. You should use (python main.py [web|wechat]).')
        return

    # interpreter = Interpreter.load("./models/current/nlu")
    # Create a trainer that uses this config
    trainer = Trainer(config.load("./models/config_spacy.yml"))
    # Load the training data
    training_data = load_data('./models/iexfinance.md')
    # Create an interpreter by training the model
    interpreter = trainer.train(training_data)
    print('Load model success.')
    load_symbols()
   

    if mode==WEB:
        start_web_server(interpreter)
    if mode==WECHAT:
        start_wechat_server(interpreter)
    if mode==TEST:
        static_test(interpreter)


if __name__ == '__main__':
    main()
    