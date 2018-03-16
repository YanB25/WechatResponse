import copy
from wxpy import *
import json
toolkit = {}
class CommandNotMatch(Exception):
    pass

class CustomException(Exception):
    pass

global config

def readJson():
    with open('config.json', 'r') as config_file:
        js = json.loads(config_file.read())
        return js

def initConfig(js):
    for obj in js:
        obj['length'] = len(obj['commands'])


def cb():
    print('leaving...')
def succesfullyConnectPromt():
    print('successfully connect to the server')

bot = Bot(cache_path='cache/wxpy.pkl', 
    logout_callback=cb,
    login_callback=succesfullyConnectPromt)
# bot.enable_puid('cache/wxpy_puid.pkl')

def checkValid(obj, text):
    texts = text.split(obj['join'])

    commands = obj['commands']
    length = len(texts)

    if (length != obj['length']):
        raise CommandNotMatch('length not match after split,\n{}\n{}'
            .format(length, obj['length']))
    for text, pattern in zip(texts, commands):
        if pattern['type'] == 'constant' and text != pattern['value']:
            raise CommandNotMatch('constant not match, expexted {}, get {}'
                .format(pattern['value'], text))

        if pattern.get('before') and not toolkit.get(pattern['before']):
            raise CommandNotMatch('expected before {} in option'
                .format(pattern['before']))
        if pattern.get('after') and not toolkit.get(pattern['after']):
            raise CommandNotMatch('expected after {} in option'
                .format(pattern['after']))

    if obj.get('before') and not toolkit.get(obj['before']):
        raise CommandNotMatch('expected before in toolkit')
    if obj.get('after') and not toolkit.get(obj['after']):
        raise CommandNotMatch('expected after in toolkit')

        
        
    



@bot.register(msg_types=TEXT, except_self=False)
def printMsg(msg):
    print(msg)

    record = {}
    for obj in config:
        commands = obj['commands']
        try:
            checkValid(obj, msg.text)
            for command, text in zip(commands, msg.text.split(obj['join'])):
                if command.get('before'):
                    func = toolkit[command['before']]
                    func(msg, text)

                if command['type'] == 'place_holder':
                    record[command['value']] = text
                
                if command.get('after'):
                    func = toolkit[command['after']]
                    func(msg, text)

            record['user'] = msg.sender.name
            if obj.get('timestamp') and obj['timestamp'] == True:
                record['user'] = 'time' #TODO: not finished
            
            break
        except CommandNotMatch as e:
            # print(e)
            record = {}
            continue
        except CustomException as e:
            print(e)
            record = {}
            continue

    if record:
        msg.sender.send('收到您的订单。 时间：{}, 地点{}, {}杯奶茶.'
            .format(record['time'], record['address'], record['num']))
        print(record)



class WeChatResponse():
    def __init__(self, obj = {}):
        global toolkit
        for key in obj:
            toolkit[key] = obj[key]

    def start(self):
        bot.start()



config = readJson()
initConfig(config)