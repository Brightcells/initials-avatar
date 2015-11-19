# initials-avatar
Initials Avatar for Python

Generate an avatar image from a user's initials. Image background color depends on name hashes(consistent hashing).

Inspired by [holys](https://github.com/holys)'s https://github.com/holys/initials-avatar

#### Installation

```
    pip install initials_avatar
```

#### Usage
```
    Python 2.7.5 (default, Mar  9 2014, 22:15:05)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: import initials_avatar as avatar

    In [2]: avatar.avatar('Python')
    Out[2]: u'/tmp/1447834587.17.png'

    In [3]: avatar.bytes('Python')
    Out[3]: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x01vIDATx\xda\xed\xd7\xcbJ\x82A\x14\xc0\xf1\xff\xa7f\x99&\xa6)\x04\x1aE-\xbaH\xab^\xa0\x0bB\xef\xd0\x13D\xd1\xaa\x97h\xd1\xa6Um\xeb\x19\x82VI\xf5\x04)\x94\x14\x85aX\x96\xe6%\xfc\xbc~_\x0b\xc9EP\x1bE\x1c:g5003\xbfa\x0e\xe7\x8cv\x1c\xdb2Q8,(\x1e\x02\x10\x80\x00\x04 \x00\x01\x08@\x00\x02P8l\x9d.\xb0\x11>\xf8u\xce4\rj\x86N\xa1\x92&U\x8as\x97\xbb\xa2nT\xbb\n\xd0\xba\xf1\x1f\xf09&X\x9f\xde\x05\xe0\xeca\x9f\xb7\xf2c\xebv,v\x86\x07<\x8c\xbbf\t\xfb#\x18\xa6A4y\xc8G\xe5\xb9\xbf\x9ePV\x7fj\x8f\xbf\x0f\x0f\xd00j\x14\xab\x19\x12\xd9\x0bN\xef\xf7\xb0h\x16V&7\x19\xb4\xba\xd4\xcb\x01\xbdQ$\x969\xc3as3\xef_U3\x89\xd3\x9f7\x00\x84F\x16\xd5\x04\x94\xeby\x00\x9c\xf6Q5\x01\x9a\xd6\xda\xce0\x9bj\x02\\\x03>\x00J\xb5w5\x01Aw\xeb\xed\xa7\x8a1\xf5\x00^G\x88\x05\xff\x1a\xe5z\x9e\xdb\xecy\xffT\xe2?oG\xb3\xe2\xb6\x07\x98\xf4,17\xb6\x8c^/\x10M\x1eQk\xea\xfd\x0b\xf8\xd9Z4\x8c*\x85\xea\x0b\xd7\xaf\xa7$r\x974\xba\xdcJt\x1dp\x12\xdf\x96nT\x00\x02\x10\x80\x00\xfe\x19\xc0;\x14l\x8f\x03\xce\x19\xb5?\xf5\x91\xa9\x9d\x9e\x16\xb4\x8e\x01\xbd\xae\xbc\x92\x03\x02\x10\x80\x00\x04 \x00\x01\xf4S|\x01Tfs0[{>\xf8\x00\x00\x00\x00IEND\xaeB`\x82'

    In [4]:
```

#### Method

```
    def avatar(self, text, size=48, circle=False, radius=0, font='simsun.ttc', fmt='png', quality=100, color=None, background=None, path=None, name=None):

    def bytes(self, text, size=48, circle=False, radius=0, font='simsun.ttc', fmt='png', quality=100, color=None, background=None):
    
    def svg(self, text, size=48, circle=False, radius=0, font_family='simsun', font_size=None, color=None, background=None, path=None, name=None):
```

#### Font
```
    simsun.ttc —— has already packaged in the source code
```

#### SVG vs PNG
* SVG: Small in Size
* PNG: Multi Plat Support


# server.sh 使用
#### Permission
```
    chmod 755 server.sh
```
#### Exec
```
    ./server.sh
```
#### Visit in Browser
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
