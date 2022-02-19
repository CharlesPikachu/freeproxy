<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://freeproxy.readthedocs.io/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyfreeproxy)](https://pypi.org/project/pyfreeproxy/)
[![PyPI](https://img.shields.io/pypi/v/pyfreeproxy)](https://pypi.org/project/pyfreeproxy)
[![license](https://img.shields.io/github/license/CharlesPikachu/freeproxy.svg)](https://github.com/CharlesPikachu/freeproxy/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/pyfreeproxy)](https://pypi.org/project/pyfreeproxy/)
[![issue resolution](https://isitmaintained.com/badge/resolution/CharlesPikachu/freeproxy.svg)](https://github.com/CharlesPikachu/freeproxy/issues)
[![open issues](https://isitmaintained.com/badge/open/CharlesPikachu/freeproxy.svg)](https://github.com/CharlesPikachu/freeproxy/issues)

Documents: https://freeproxy.readthedocs.io/


# FreeProxy
```sh
Collecting free proxies from internet.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```


# Support List
| Source                 | Official Website                                                 | Core Code                                              | in Chinese        |
| :----:                 | :----:                                                           | :----:                                                 | :----:            |
| kuaidaili              | [click](https://www.kuaidaili.com/)                              | [click](./freeproxy/modules/proxies/kuaidaili.py)      | 快代理            |
| ip3366                 | [click](http://www.ip3366.net/free/)                             | [click](./freeproxy/modules/proxies/ip3366.py)         | 云代理            |
| jiangxianli            | [click](http://ip.jiangxianli.com/?page=1)                       | [click](./freeproxy/modules/proxies/jiangxianli.py)    | jiangxianli代理   |
| proxylistplus          | [click](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)  | [click](./freeproxy/modules/proxies/proxylistplus.py)  | proxylistplus代理 |


# Install

#### Pip install
```sh
run "pip install pyfreeproxy"
```

#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/freeproxy.git
Step2: cd freeproxy -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/freeproxy.git@master"
```


# Quick Start
```python
from freeproxy import freeproxy

client = freeproxy.FreeProxy()
response = client.get('https://www.baidu.com/')
```


# Projects in Charles_pikachu
- [Games](https://github.com/CharlesPikachu/Games): Create interesting games by pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written by pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written by pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written by pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written by pure python.


# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](./docs/pikachu.jpg)