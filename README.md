<div align="center">
  <img src="https://github.com/CharlesPikachu/freeproxy/blob/160bb08f8919027ec2abd022aab6b1276fd4d307/docs/logo.png" width="600"/>
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


# What's New

- 2025-10-17: Released pyfreeproxy v0.1.5 — code cleanup, deprecated/invalid proxy sources removed, new sources added.


# Introduction

FreeProxy continuously discovers and updates lists of free proxies. If you find value here, please star the project to keep it on your radar.


# Support Proxy Sources

| ProxiedSession                       | Official Website                                                             | Code Snippet                                                                                                 |
| :----:                               | :----:                                                                       | :----:                                                                                                       |
| KuaidailiProxiedSession              | [click](https://www.kuaidaili.com/free/inha/1/)                              | [click](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kuaidaili.py)      |
| IP3366ProxiedSession                 | [click](http://www.ip3366.net/free/?stype=1&page=1)                          | [click](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip3366.py)         |
| ProxylistplusProxiedSession          | [click](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)              | [click](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylistplus.py)  |
| IP89ProxiedSession                   | [click](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)     | [click](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip89.py)           |
| ZdayeProxiedSession                  | [click](https://www.zdaye.com/free/1/)                                       | [click](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/zdaye.py)          |


# Playground

| Project                | Introduction                                                                                       | Code Snippet                                                                                                 |
| :----:                 | :----:                                                                                             | :----:                                                                                                       |
| ICU996                 | [用数万条数据带大家看看到底是哪些人在反对996~](https://mp.weixin.qq.com/s/58AHrbp0jfFltYqZsJPu5Q)  | [click](https://github.com/CharlesPikachu/freeproxy/tree/master/examples/ICU996)                             |


# Install

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


# Quick Start

```python
from freeproxy import ProxiedSessionClient

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
resp = proxied_session_client.get('https://space.bilibili.com/406756145', headers=headers)
print(resp.text)
```


# Recommended Projects

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


# WeChat Official Account (微信公众号):

Charles的皮卡丘 (*Charles_pikachu*)  
![img](https://github.com/CharlesPikachu/freeproxy/blob/160bb08f8919027ec2abd022aab6b1276fd4d307/docs/pikachu.jpg)