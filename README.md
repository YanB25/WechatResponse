# WechatResponse
## TL;DR
An incredibly user-friendly framework for autoreply in WeChat. The framework is based on `wxpy`.  
一个极其容易配置，可拓展的微信自动回复框架。基于`wxpy`开发。
## Getting Start
### 配置方法
按下图方式设置`config.json`
``` json
// in file config.json
[{
    "name": "greet",
    "join": " ",
    "commands": [{
        "value": "hello",
        "type": "constant"
    }, {
        "value": "name",
        "type": "place_holder"
    }]
}]
```
创建一个`python`文件
``` python
# bar.py
from wechatResponse import WeChatResponse
wcr = WeChatResponse()
wcr.start()
```
使用`Python3`运行上述文件
``` sh
$ python bar.py
```
That's all you need!
### 运行效果
当你的朋友在微信你对你说`hello yanbin`时，你可以看到命令行的log处出现  
``` python
{'name': 'yanbin'}
```
框架将`name`部分提取到一个`object`里，并自动打印到终端。  

### 理解配置文件
`config.json`是一个大数组，其中中包括了若干`object`。  
每一个`object`都将作为一个模板，尝试匹配和提取你的微信好友对你的留言。  

`name`:该模板的名字。在代码中，这一项会被忽略  
`join`:用何种分隔符将`commands`里的匹配内容分割开。  
`commands type`:
从`constant`和`place_holder`中选择一个。若为`constant`，好友的留言必须“完全匹配”`commands value`中的值，否则该模板匹配失败。  
若为`place_holder`,好友留言中对应位置的内容将被提取出来，以`commands value`为`key`存放到一个`object`中。

## Advanced Used
hook机制实现custom行为
见`main.py`作为例子

README待更新