<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://freeproxy.readthedocs.io/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyfreeproxy)](https://pypi.org/project/pyfreeproxy/)
[![PyPI](https://img.shields.io/pypi/v/pyfreeproxy)](https://pypi.org/project/pyfreeproxy)
[![license](https://img.shields.io/github/license/CharlesPikachu/freeproxy.svg)](https://github.com/CharlesPikachu/freeproxy/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/pyfreeproxy)](https://pypi.org/project/pyfreeproxy/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyfreeproxy?style=flat-square)](https://pypi.org/project/pyfreeproxy/)
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
| daili66                | [click](http://www.66ip.cn/index.html)                           | [click](./freeproxy/modules/proxies/daili66.py)        | 代理66            |
| fatezero               | [click](http://proxylist.fatezero.org/proxy.list)                | [click](./freeproxy/modules/proxies/fatezero.py)       | fatezero代理      |
| ip89                   | [click](http://api.89ip.cn/)                                     | [click](./freeproxy/modules/proxies/ip89.py)           | IP89代理          |
| seofangfa              | [click](https://proxy.seofangfa.com/)                            | [click](./freeproxy/modules/proxies/seofangfa.py)      | seofangfa代理     |
| zdaye                  | [click](https://www.zdaye.com/dayProxy/1.html)                   | [click](./freeproxy/modules/proxies/zdaye.py)          | 站大爷代理        |
| yqie                   | [click](http://ip.yqie.com/ipproxy.htm)                          | [click](./freeproxy/modules/proxies/yqie.py)           | yqie代理          |
| taiyanghttp            | [click](http://www.taiyanghttp.com/free/page1/)                  | [click](./freeproxy/modules/proxies/taiyanghttp.py)    | 太阳HTTP代理      |


# Practice with FreeProxy
| Project                | Introduction                                                | Core Code                                              | in Chinese                                    |
| :----:                 | :----:                                                      | :----:                                                 | :----:                                        |
| ICU996                 | [click](https://mp.weixin.qq.com/s/58AHrbp0jfFltYqZsJPu5Q)  | [click](./examples/ICU996)                             | 用数万条数据带大家看看到底是哪些人在反对996~  |


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

proxy_sources = ['proxylistplus', 'kuaidaili']
fp_client = freeproxy.FreeProxy(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
response = fp_client.get('https://space.bilibili.com/406756145', headers=headers)
print(response.text)
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
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.
- [NovelDL](https://github.com/CharlesPikachu/noveldl): Search and download novels from some specific websites.


# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](./docs/pikachu.jpg)