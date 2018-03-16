from wechatResponse import WeChatResponse
from wechatResponse import CustomException
class NumberExceed(CustomException):
    pass

def myprint(msg, txt):
    print('hello world')
    print(msg) 

def count(msg, num):
    n =int(num)
    if count.num + n > 8:
        raise NumberExceed('can not sell too much')
    if n > 5:
        msg.sender.send('sorry!')
        raise NumberExceed('can not order too much')
    count.num += n
count.num = 0

options = {
    'print':  myprint,
    'call_before': count
}
wechatResponse = WeChatResponse(options)
wechatResponse.start()