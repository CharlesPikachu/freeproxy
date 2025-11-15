<div align="center">
  <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/docs/logo.png" width="600"/>
</div>
<br />

<p align="center">
  <a href="https://freeproxy.readthedocs.io/">
    <img alt="docs" src="https://img.shields.io/badge/docs-latest-blue">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyfreeproxy">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/pyfreeproxy">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/blob/master/LICENSE">
    <img alt="license" src="https://img.shields.io/github/license/CharlesPikachu/freeproxy.svg">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Downloads (pepy mirror)" src="https://pepy.tech/badge/pyfreeproxy">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/pyfreeproxy?style=flat-square">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/issues">
    <img alt="issue resolution" src="https://isitmaintained.com/badge/resolution/CharlesPikachu/freeproxy.svg">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/issues">
    <img alt="open issues" src="https://isitmaintained.com/badge/open/CharlesPikachu/freeproxy.svg">
  </a>
</p>

<p align="center">
  Documents: <a href="https://freeproxy.readthedocs.io/">https://freeproxy.readthedocs.io/</a>
</p>


# ✨ What's New

- 2025-10-20: Released pyfreeproxy v0.1.8 — Replace `user_agent` as `fake-useragent`.
- 2025-10-20: Released pyfreeproxy v0.1.7 — Auto remove invalid proxied sessions in `ProxiedSessionClient`.
- 2025-10-18: Released pyfreeproxy v0.1.6 — New sources `QiyunipProxiedSession`, `ProxyhubProxiedSession` and `ProxydbProxiedSession` added.
- 2025-10-17: Released pyfreeproxy v0.1.5 — Code cleanup, deprecated/invalid proxy sources removed, new sources added.


# 📘 Introduction

FreeProxy continuously discovers and updates lists of free proxies. If you find value here, please star the project to keep it on your radar.


# 🌐 Supported Proxy Sources

| ProxiedSession                       | Official Website                                                             | Code Snippet                                                                                                            |
| :----:                               | :----:                                                                       | :----:                                                                                                                  |
| KuaidailiProxiedSession              | [click](https://www.kuaidaili.com/free/inha/1/)                              | [kuaidaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kuaidaili.py)          |
| IP3366ProxiedSession                 | [click](http://www.ip3366.net/free/?stype=1&page=1)                          | [ip3366.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip3366.py)                |
| ProxylistplusProxiedSession          | [click](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)              | [proxylistplus.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylistplus.py)  |
| IP89ProxiedSession                   | [click](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)     | [ip89.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip89.py)                    |
| ZdayeProxiedSession                  | [click](https://www.zdaye.com/free/1/)                                       | [zdaye.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/zdaye.py)                  |
| QiyunipProxiedSession                | [click](https://www.qiyunip.com/freeProxy/1.html)                            | [qiyunip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/qiyunip.py)              |
| ProxyhubProxiedSession               | [click](https://proxyhub.me/)                                                | [proxyhub.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyhub.py)            |
| ProxydbProxiedSession                | [click](https://proxydb.net/?offset=0)                                       | [proxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydb.py)              |


# 🎮 Playground

Here are some projects built on top of pyfreeproxy,

| Project                | WeChat Article	                                                                                  | Project Location                                                                                             |
| :----:                 | :----:                                                                                             | :----:                                                                                                       |
| ICU996                 | [用数万条数据带大家看看到底是哪些人在反对996~](https://mp.weixin.qq.com/s/58AHrbp0jfFltYqZsJPu5Q)  | [click](https://github.com/CharlesPikachu/freeproxy/tree/master/examples/ICU996)                             |


# 📦 Install

You have three installation methods to choose from,

```sh
# from pip
pip install pyfreeproxy
# from github repo method-1
pip install git+https://github.com/CharlesPikachu/freeproxy.git@master
# from github repo method-2
git clone https://github.com/CharlesPikachu/freeproxy.git
cd freeproxy
python setup.py install
```


# 🚀 Quick Start

After a successful installation, you can use code like this to automatically set a free proxy found online and send a GET / POST request to a website,

```python
from freeproxy import freeproxy

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = freeproxy.ProxiedSessionClient(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
resp = proxied_session_client.get('https://space.bilibili.com/406756145', headers=headers)
print(resp.text)
```

When using pyfreeproxy as a third-party package, if you don’t want it to print too much extra information, you can set `disable_print=True`, for example:`

```python
from freeproxy import freeproxy

proxy_sources = ['ProxydbProxiedSession']
proxied_session_client = freeproxy.ProxiedSessionClient(proxy_sources=proxy_sources, disable_print=True)
```

After installing pyfreeproxy, you can use the following code to quickly test the effectiveness of each proxy source,

```python
from tqdm import tqdm
from freeproxy.modules import ProxiedSessionBuilder, BuildProxiedSession, printtable, colorize


'''main'''
def main():
    # proxy_sources
    proxy_sources = ProxiedSessionBuilder.REGISTERED_MODULES.keys()
    # iter to test
    print_titles, print_items = ['Source', 'Effectiveness', 'Retrieved Examples'], []
    for proxy_source in tqdm(proxy_sources):
        try:
            module_cfg = {'max_pages': 1, 'type': proxy_source}
            proxied_session = BuildProxiedSession(module_cfg=module_cfg)
            candidate_proxies = proxied_session.refreshproxies()
        except:
            candidate_proxies = []
        if len(candidate_proxies) > 0:
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('True', 'green'), ', '.join([f'{k.upper()}: {v}' for k, v in candidate_proxies[0].items()])])
        else:
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('False', 'red'), 'NULL'])
    # visualize test results
    print('The effectiveness test results of each proxy are as follows:')
    printtable(titles=print_titles, items=print_items)


'''tests'''
if __name__ == '__main__':
    main()
```

The sample output of the above code is:

```
The effectiveness test results of each proxy are as follows:
+---------------+---------------+--------------------------------------------------------------------+
|     Source    | Effectiveness |                         Retrieved Examples                         |
+---------------+---------------+--------------------------------------------------------------------+
|      IP89     |     False     |                                NULL                                |
|     Zdaye     |     False     |                                NULL                                |
|     IP3366    |     False     |                                NULL                                |
|   Kuaidaili   |      True     |  HTTP: http://119.3.113.150:9094,HTTPS: http://119.3.113.150:9094  |
| Proxylistplus |      True     | HTTP: http://110.77.134.112:8080,HTTPS: http://110.77.134.112:8080 |
|    Qiyunip    |      True     | HTTP: https://123.182.58.59:8089,HTTPS: https://123.182.58.59:8089 |
|    Proxyhub   |      True     | HTTP: socks4://183.88.2.244:4145,HTTPS: socks4://183.88.2.244:4145 |
|    Proxydb    |      True     |   HTTP: http://45.186.6.104:3128,HTTPS: http://45.186.6.104:3128   |
+---------------+---------------+--------------------------------------------------------------------+
```


# ⭐ Recommended Projects

- [Games](https://github.com/CharlesPikachu/Games): Create interesting games in pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written in pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written in pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written in pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written in pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.
- [NovelDL](https://github.com/CharlesPikachu/noveldl): Search and download novels from some specific websites.


# 📱 WeChat Official Account (微信公众号):

Charles的皮卡丘 (*Charles_pikachu*)  
![img](https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/docs/pikachu.jpg)