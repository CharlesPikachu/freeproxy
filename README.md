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

<div align="center">

  <h3>📚 Documentation</h3>
  <p>
    <a href="https://freeproxy.readthedocs.io/">
      https://freeproxy.readthedocs.io/
    </a>
  </p>

  <h3>⚡ Live Proxies <span style="font-size:0.9em;">(24小时内最新代理)</span></h3>
  <p>
    <a href="https://charlespikachu.github.io/freeproxy/">
      <code>https://charlespikachu.github.io/freeproxy/</code>
    </a>
  </p>
  <p>
    <a href="https://charlespikachu.github.io/freeproxy/">
      <img
        alt="demo"
        src="https://img.shields.io/badge/demo-online-brightgreen?style=for-the-badge"
      />
    </a>
  </p>

</div>


# ✨ What's New

- 2025-11-19: Released pyfreeproxy v0.2.2 — Fix potential in-place modified bugs.
- 2025-11-16: Released pyfreeproxy v0.2.1 — Add support for ZdayeProxiedSession and FineProxyProxiedSession.
- 2025-11-16: Released pyfreeproxy v0.2.0 — Refactored the code to improve the quality of the retrieved proxies and added support for fetching proxies from seven additional free proxy sources.
- 2025-10-20: Released pyfreeproxy v0.1.8 — Replace `user_agent` as `fake-useragent`.
- 2025-10-20: Released pyfreeproxy v0.1.7 — Auto remove invalid proxied sessions in `ProxiedSessionClient`.
- 2025-10-18: Released pyfreeproxy v0.1.6 — New sources `QiyunipProxiedSession`, `ProxyhubProxiedSession` and `ProxydbProxiedSession` added.
- 2025-10-17: Released pyfreeproxy v0.1.5 — Code cleanup, deprecated/invalid proxy sources removed, new sources added.


# 📘 Introduction

FreeProxy continuously discovers and updates lists of free proxies. If you find value here, please star the project to keep it on your radar.


# 🌐 Supported Proxy Sources

| ProxiedSession                       | Official Website                                                                  | Code Snippet                                                                                                            |
| :----:                               | :----:                                                                            | :----:                                                                                                                  |
| KuaidailiProxiedSession              | [Kuaidaili](https://www.kuaidaili.com/free/inha/1/)                               | [kuaidaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kuaidaili.py)          |
| IP3366ProxiedSession                 | [IP3366](http://www.ip3366.net/free/?stype=1&page=1)                              | [ip3366.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip3366.py)                |
| ProxylistplusProxiedSession          | [Proxylistplus](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)           | [proxylistplus.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylistplus.py)  |
| IP89ProxiedSession                   | [IP89](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)           | [ip89.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip89.py)                    |
| QiyunipProxiedSession                | [Qiyunip](https://www.qiyunip.com/freeProxy/1.html)                               | [qiyunip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/qiyunip.py)              |
| ProxyhubProxiedSession               | [Proxyhub](https://proxyhub.me/)                                                  | [proxyhub.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyhub.py)            |
| ProxydbProxiedSession                | [Proxydb](https://proxydb.net/?offset=0)                                          | [proxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydb.py)              |
| Tomcat1235ProxiedSession             | [Tomcat1235](https://tomcat1235.nyc.mn/proxy_list?page=1)                         | [tomcat1235.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/tomcat1235.py)        |
| ProxydailyProxiedSession             | [Proxydaily](https://proxy-daily.com/)                                            | [proxydaily.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydaily.py)        |
| SpysoneProxiedSession                | [Spysone](https://spys.one/en/free-proxy-list/)                                   | [spysone.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/spysone.py)              |
| FreeproxylistProxiedSession          | [Freeproxylist](https://free-proxy-list.net/)                                     | [freeproxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/freeproxylist.py)  |
| KxdailiProxiedSession                | [Kxdaili](http://www.kxdaili.com/dailiip.html)                                    | [kxdaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kxdaili.py)              |
| ProxylistProxiedSession              | [Proxylist](https://www.proxy-list.download/HTTP/)                                | [proxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylist.py)          |
| IhuanProxiedSession                  | [Ihuan](https://ip.ihuan.me/?page=4ce63706)                                       | [ihuan.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ihuan.py)                  |
| ZdayeProxiedSession                  | [Zdaye](https://www.zdaye.com/free/1/)                                            | [zdaye.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/zdaye.py)                  |
| FineProxyProxiedSession              | [FineProxy](https://fineproxy.org/cn/free-proxy/)                                 | [fineproxy.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/fineproxy.py)          |


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
+---------------+---------------+------------------------------+-------+
|     Source    | Effectiveness |      Retrieved Examples      | Total |
+---------------+---------------+------------------------------+-------+
|      IP89     |      True     | http://103.187.117.163:8080  |  199  |
|     IP3366    |      True     | https://117.71.154.249:8089  |   30  |
|   Kuaidaili   |      True     |  http://121.43.150.231:3128  |   37  |
| Proxylistplus |      True     |  http://110.77.134.112:8080  |   50  |
|    Qiyunip    |      True     |  https://36.6.144.125:8089   |   15  |
|   Proxydaily  |      True     |  http://35.159.15.107:9006   |   4   |
|    Proxyhub   |      True     | socks4://51.68.134.253:30204 |   20  |
|    Proxydb    |      True     |   http://45.186.6.104:3128   |   30  |
|   Tomcat1235  |      True     | socks5://188.235.21.247:2080 |   30  |
|    Spysone    |      True     |   http://160.22.221.2:8080   |   30  |
| Freeproxylist |      True     | http://176.162.240.186:8081  |  300  |
|   Proxylist   |      True     |  http://188.166.30.17:8888   |  2082 |
|    Kxdaili    |      True     |  http://116.63.160.98:8899   |   40  |
|     Ihuan     |      True     |    http://111.1.27.85:80     |  2607 |
|     Zdaye     |      True     |  http://153.0.171.163:8085   |   20  |
|   FineProxy   |      True     |  http://8.220.136.174:8443   |   20  |
+---------------+---------------+------------------------------+-------+
```

Then, you can use code like this to automatically set a free proxy found online and send a GET / POST request to a website,

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


# 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=CharlesPikachu/freeproxy&type=date&legend=top-left)](https://www.star-history.com/#CharlesPikachu/freeproxy&type=date&legend=top-left)


# ☕ Appreciation (赞赏 / 打赏)

| WeChat Appreciation QR Code (微信赞赏码)                                                                                       | Alipay Appreciation QR Code (支付宝赞赏码)                                                                                     |
| :--------:                                                                                                                     | :----------:                                                                                                                   |
| <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/.github/pictures/wechat_reward.jpg" width="260" /> | <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/.github/pictures/alipay_reward.png" width="260" /> |


# 📱 WeChat Official Account (微信公众号):

Charles的皮卡丘 (*Charles_pikachu*)  
![img](https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/docs/pikachu.jpg)