<div align="center">
  <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/docs/logo.png" width="600"/>
</div>
<br />

<p align="center">
  <a href="https://freeproxy.readthedocs.io/">
    <img alt="Docs" src="https://img.shields.io/badge/docs-latest-blue">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyfreeproxy">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/pyfreeproxy">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/blob/master/LICENSE">
    <img alt="License" src="https://badgen.net/github/license/CharlesPikachu/freeproxy">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Downloads (total)" src="https://static.pepy.tech/badge/pyfreeproxy">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Downloads (month)" src="https://static.pepy.tech/badge/pyfreeproxy/month">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img alt="PyPI - Downloads (week)" src="https://static.pepy.tech/badge/pyfreeproxy/week">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/actions/workflows/update-proxies.yml">
    <img alt="Update Proxies.json" src="https://github.com/CharlesPikachu/freeproxy/actions/workflows/update-proxies.yml/badge.svg">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/issues">
    <img alt="Issue Resolution" src="https://isitmaintained.com/badge/resolution/CharlesPikachu/freeproxy.svg">
  </a>
  <a href="https://github.com/CharlesPikachu/freeproxy/issues">
    <img alt="Open Issues" src="https://isitmaintained.com/badge/open/CharlesPikachu/freeproxy.svg">
  </a>
</p>

<div align="center">

  <h3>📚 Documentation</h3>
  <p>
    <a href="https://freeproxy.readthedocs.io/">
      https://freeproxy.readthedocs.io/
    </a>
  </p>

  <h3>⚡ Live Proxies <span style="font-size:0.9em;">(最新免费高质量代理)</span></h3>
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

<p align="center">
  <strong>学习收获更多有趣的内容, 欢迎关注微信公众号：Charles的皮卡丘</strong>
</p>


# ✨ What's New

- 2026-04-08: Released pyfreeproxy v0.4.3 — Added two new free proxy sources: "proxyfreeonly.com" and "proxiware.com"; optimized the implementation of the ProxyInfo type; optimized the implementation of the logging function.
- 2026-04-04: Released pyfreeproxy v0.4.2 — Added scraping support for two additional free proxy sources, *i.e.*, "sockslist.us" and "roundproxies.com", and optimized the document content.
- 2026-03-30: Released pyfreeproxy v0.4.1 — Added scraping for two new free proxy sources (*i.e.*, "advanced.name" and "iproyal.com"); optimized DrissionPage arguments.


# 📘 Introduction

🌍 FreeProxy continuously discovers, verifies, and updates free proxy lists for HTTP, HTTPS, SOCKS4, and SOCKS5. 
With flexible filtering by geography, anonymity, speed, and more, it helps you quickly find proxies that match your needs. 
If you find this project useful, please consider giving it a ⭐ to support development and stay updated.


# 🌐 Supported Proxy Sources

| Proxy Source (EN)                                                                      | Proxy Source (CN)                                                           | HTTP         | HTTPS      | SOCKS4     | SOCKS5     | Code Snippet                                                                                                            |
| :----                                                                                  | :----                                                                       | :----:       | :----:     | :----:     | :----:     | :----                                                                                                                   |
| [ADVFPProxiedSession](https://advanced.name/freeproxy)                                 | [Advanced.Name](https://advanced.name/freeproxy)                            | ✔           | ✔         | ✔         | ✔         | [advfp.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/advfp.py)                  |
| [DatabayProxiedSession](https://databay.com/free-proxy-list)                           | [Databay](https://databay.com/free-proxy-list)                              | ✔           | ✔         | ❌         | ✔         | [databay.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/databay.py)              |
| [DpangestuwProxiedSession](https://github.com/dpangestuw/Free-Proxy)                   | [Dpangestuw](https://github.com/dpangestuw/Free-Proxy)                      | ✔           | ✔         | ✔         | ✔         | [dpangestuw.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/dpangestuw.py)        |
| [FreeproxylistProxiedSession](https://free-proxy-list.net/)                            | [FreeProxyList](https://free-proxy-list.net/)                               | ✔           | ✔         | ✔         | ❌         | [freeproxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/freeproxylist.py)  |
| [FineProxyProxiedSession](https://fineproxy.org/cn/free-proxy/)                        | [FineProxy](https://fineproxy.org/cn/free-proxy/)                           | ✔           | ✔         | ✔         | ✔         | [fineproxy.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/fineproxy.py)          |
| [FreeProxyDBProxiedSession](https://freeproxydb.com/)                                  | [FreeProxyDB](https://freeproxydb.com/)                                     | ✔           | ❌         | ✔         | ✔         | [freeproxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/freeproxydb.py)      |
| [GeonodeProxiedSession](https://geonode.com/free-proxy-list)                           | [Geonode](https://geonode.com/free-proxy-list)                              | ✔           | ✔         | ✔         | ✔         | [geonode.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/geonode.py)              |
| [GoodIPSProxiedSession](https://www.goodips.com/)                                      | [谷德免费代理](https://www.goodips.com/)                                    | ✔           | ✔         | ✔         | ✔         | [goodips.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/goodips.py)              |
| [IPLocateProxiedSession](https://www.iplocate.io/)                                     | [IPLocate](https://www.iplocate.io/)                                        | ✔           | ✔         | ✔         | ✔         | [iplocate.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/iplocate.py)            |
| [IP3366ProxiedSession](http://www.ip3366.net/free/?stype=1&page=1)                     | [云代理](http://www.ip3366.net/free/?stype=1&page=1)                        | ✔           | ✔         | ❌         | ❌         | [ip3366.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip3366.py)                |
| [IP89ProxiedSession](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)  | [IP89](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)     | ✔           | ❌         | ❌         | ❌         | [ip89.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip89.py)                    |
| [IPRoyalProxiedSession](https://iproyal.com/free-proxy-list/)                          | [IPRoyal](https://iproyal.com/free-proxy-list/)                             | ❌           | ✔         | ❌         | ❌         | [iproyal.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/iproyal.py)              |
| [JiliuipProxiedSession](https://www.jiliuip.com/free/page-1/)                          | [积流代理](https://www.jiliuip.com/free/page-1/)                            | ✔           | ❌         | ❌         | ❌         | [jiliuip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/jiliuip.py)              |
| [KuaidailiProxiedSession](https://www.kuaidaili.com/free/inha/1/)                      | [快代理](https://www.kuaidaili.com/free/inha/1/)                            | ✔           | ✔         | ❌         | ❌         | [kuaidaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kuaidaili.py)          |
| [KxdailiProxiedSession](http://www.kxdaili.com/dailiip.html)                           | [开心代理](http://www.kxdaili.com/dailiip.html)                             | ✔           | ✔         | ❌         | ❌         | [kxdaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kxdaili.py)              |
| [OpenProxyListProxiedSession](https://api.openproxylist.xyz/)                          | [OpenProxyList](https://api.openproxylist.xyz/)                             | ✔           | ✔         | ✔         | ✔         | [openproxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/openproxylist.py)  |
| [ProxyhubProxiedSession](https://proxyhub.me/)                                         | [ProxyHub](https://proxyhub.me/)                                            | ✔           | ✔         | ✔         | ✔         | [proxyhub.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyhub.py)            |
| [ProxydbProxiedSession](https://proxydb.net/?offset=0)                                 | [ProxyDB](https://proxydb.net/?offset=0)                                    | ✔           | ✔         | ❌         | ✔         | [proxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydb.py)              |
| [ProxylistProxiedSession](https://www.proxy-list.download/HTTP/)                       | [ProxyList](https://www.proxy-list.download/HTTP/)                          | ✔           | ✔         | ✔         | ✔         | [proxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylist.py)          |
| [ProxiflyProxiedSession](https://proxifly.dev/)                                        | [Proxifly](https://proxifly.dev/)                                           | ✔           | ✔         | ✔         | ✔         | [proxifly.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxifly.py)            |
| [ProxydailyProxiedSession](https://proxy-daily.com/)                                   | [ProxyDaily](https://proxy-daily.com/)                                      | ✔           | ✔         | ✔         | ✔         | [proxydaily.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydaily.py)        |
| [ProxyScrapeProxiedSession](https://proxyscrape.com/free-proxy-list)                   | [ProxyScrape](https://proxyscrape.com/free-proxy-list)                      | ✔           | ❌         | ✔         | ✔         | [proxyscrape.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyscrape.py)      |
| [ProxyEliteProxiedSession](https://proxyelite.info/cn/free/asia/china/)                | [ProxyElite](https://proxyelite.info/cn/free/asia/china/)                   | ✔           | ❌         | ✔         | ✔         | [proxyelite.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyelite.py)        |
| [ProxyNovaProxiedSession](https://www.proxynova.com/proxy-server-list/)                | [ProxyNova](https://www.proxynova.com/proxy-server-list/)                   | ✔           | ❌         | ❌         | ❌         | [proxynova.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxynova.py)          |
| [ProxyShareProxiedSession](https://www.proxyshare.com/zh/free-proxy/)                  | [ProxyShare](https://www.proxyshare.com/zh/free-proxy/)                     | ✔           | ✔         | ✔         | ✔         | [proxyshare.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyshare.py)        |
| [ProxiwareProxiedSession](https://proxiware.com/free-proxy-list)                       | [Proxiware](https://proxiware.com/free-proxy-list)                          | ✔           | ✔         | ✔         | ✔         | [proxiware.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxiware.py)          |
| [ProxyFreeOnlyProxiedSession](https://proxyfreeonly.com/free-proxy-list)               | [ProxyFreeOnly](https://proxyfreeonly.com/free-proxy-list)                  | ✔           | ✔         | ✔         | ✔         | [proxyfreeonly.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyfreeonly.py)  |
| [QiyunipProxiedSession](https://www.qiyunip.com/freeProxy/1.html)                      | [齐云代理](https://www.qiyunip.com/freeProxy/1.html)                        | ✔           | ✔         | ❌         | ❌         | [qiyunip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/qiyunip.py)              |
| [RoundProxiesProxiedSession](https://roundproxies.com/free-proxy-list/)                | [Roundproxies](https://roundproxies.com/free-proxy-list/)                   | ✔           | ✔         | ✔         | ✔         | [roundproxies.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/roundproxies.py)    |
| [SpysoneProxiedSession](https://spys.one/en/free-proxy-list/)                          | [SPYS.ONE](https://spys.one/en/free-proxy-list/)                            | ✔           | ❌         | ❌         | ✔         | [spysone.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/spysone.py)              |
| [SCDNProxiedSession](https://proxy.scdn.io/)                                           | [公共代理池](https://proxy.scdn.io/)                                        | ✔           | ✔         | ✔         | ✔         | [scdn.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/scdn.py)                    |
| [SixSixDailiProxiedSession](https://www.66daili.com/)                                  | [66免费代理](https://www.66daili.com/)                                      | ✔           | ✔         | ✔         | ✔         | [sixsixdaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/sixsixdaili.py)      |
| [SocksListProxiedSession](https://sockslist.us/)                                       | [FreeSocks5Proxy](https://sockslist.us/)                                    | ❌           | ❌         | ❌         | ✔         | [sockslist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/sockslist.py)          |
| [Tomcat1235ProxiedSession](https://tomcat1235.nyc.mn/proxy_list?page=1)                | [北极光代理](https://tomcat1235.nyc.mn/proxy_list?page=1)                   | ❌           | ❌         | ❌         | ✔         | [tomcat1235.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/tomcat1235.py)        |
| [TheSpeedXProxiedSession](https://github.com/TheSpeedX)                                | [TheSpeedX](https://github.com/TheSpeedX)                                   | ✔           | ❌         | ✔         | ✔         | [thespeedx.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/thespeedx.py)          |


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

Please note that some proxy sources need to be crawled using [DrissionPage](https://www.drissionpage.cn/), such as `IP3366ProxiedSession`. 
If DrissionPage cannot find a suitable browser in the current environment, it will automatically download the latest compatible beta version of Google Chrome for the current system. 
So if you notice that the program is downloading a browser, there is no need to be overly concerned.


# 🚀 Quick Start

#### Scrape proxies from multiple sources

After installing freeproxy, you can run a script to:

- scrape proxies from multiple sources,
- print basic statistics for each source,
- save all retrieved proxies into a JSON file.

Example code (scrape + summarize + save):

```python
import json, random
from tqdm import tqdm
from freeproxy.modules import BaseProxiedSession, ProxyInfo, BuildProxiedSession, printtable, colorize

'''settings'''
SOURCES = ["ProxiflyProxiedSession", "KuaidailiProxiedSession", "QiyunipProxiedSession", "ProxylistProxiedSession"]
TITLES = ["Source", "Retrieved Example", "HTTP", "HTTPS", "SOCKS4", "SOCKS5", "Chinese IP", "Elite", "Total"]

'''scrape'''
def scrape(src: str) -> list[ProxyInfo]:
    try:
        sess: BaseProxiedSession = BuildProxiedSession({"max_pages": 1, "type": src, "disable_print": False})
        return sess.refreshproxies()
    except Exception:
        return []

'''stats'''
def stats(proxies: list[ProxyInfo]) -> dict:
    return {
        "http":   sum(p.protocol.lower() == "http"   for p in proxies),
        "https":  sum(p.protocol.lower() == "https"  for p in proxies),
        "socks4": sum(p.protocol.lower() == "socks4" for p in proxies),
        "socks5": sum(p.protocol.lower() == "socks5" for p in proxies),
        "cn":     sum(bool(p.in_chinese_mainland) for p in proxies),
        "elite":  sum(p.anonymity.lower() == "elite" for p in proxies),
        "total":  len(proxies),
        "ex":     (random.choice(proxies).proxy if proxies else "NULL"),
    }

'''row'''
def row(src: str, s: dict) -> list:
    ex = colorize(s["ex"], "green") if s["total"] else "NULL"
    return [
        src.removesuffix("ProxiedSession"),
        ex,
        colorize(s["http"], "number"),
        colorize(s["https"], "number"),
        colorize(s["socks4"], "number"),
        colorize(s["socks5"], "number"),
        colorize(s["cn"], "number"),
        colorize(s["elite"], "number"),
        colorize(s["total"], "number"),
    ]

'''main'''
def main():
    free_proxies, items = {}, []
    for src in tqdm(SOURCES):
        proxies = scrape(src)
        items.append(row(src, stats(proxies)))
        free_proxies[src] = [p.todict() for p in proxies]
    print("The proxy distribution for each source you specified is as follows:")
    printtable(titles=TITLES, items=items, terminal_right_space_len=1)
    json.dump(free_proxies, open("free_proxies.json", "w"), indent=2)

'''tests'''
if __name__ == "__main__":
    main()
```

Example output (terminal):

```bash
C:\Users\Charles\Desktop>python test.py
KuaidailiProxiedSession >>> adding country_code: 37it [00:05,  6.57it/s]                 | 1/4 [00:18<00:56, 18.95s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:28<00:00,  7.17s/it]
The proxy distribution for each source you specified is as follows:
+-----------+-------------------------------+------+-------+--------+--------+------------+-------+-------+
|   Source  |       Retrieved Example       | HTTP | HTTPS | SOCKS4 | SOCKS5 | Chinese IP | Elite | Total |
+-----------+-------------------------------+------+-------+--------+--------+------------+-------+-------+
|  Proxifly |   http://195.231.69.203:443   | 5112 |   0   |  1043  |  477   |     48     |  2157 |  6632 |
| Kuaidaili |   http://113.45.158.25:3128   |  20  |   13  |   0    |   0    |     19     |   33  |   33  |
|  Qiyunip  |   https://114.103.88.18:8089  |  6   |   9   |   0    |   0    |     15     |   14  |   15  |
| Proxylist | socks4://184.181.217.206:4145 | 420  |   59  |  182   |  156   |     54     |  699  |  817  |
+-----------+-------------------------------+------+-------+--------+--------+------------+-------+-------+
```

All proxies are saved to `free_proxies.json` in the current directory, *e.g.*:

```python
{
  "KuaidailiProxiedSession": [
    {
      "source": "KuaidailiProxiedSession",
      "protocol": "http",
      "ip": "58.216.109.17",
      "port": "800",
      "country_code": "CN",
      "in_chinese_mainland": true,
      "anonymity": "elite",
      "delay": 124,
      "test_timeout": 5,
      "test_url": "http://www.baidu.com",
      "test_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
      },
      "failed_connection_default_timeout": 3600000,
      "created_at": "2025-12-03T12:43:25.018208",
      "extra": {}
    }
  ],
  "ProxiflyProxiedSession": [],
  "QiyunipProxiedSession": [],
  "ProxylistProxiedSession": []
}
```

*Tip: Increase `max_pages` to fetch more proxies from each source.*

#### List supported proxy sources

To list all proxy sources supported by your current freeproxy version:

```bash
python -c "from freeproxy.modules import ProxiedSessionBuilder; print(ProxiedSessionBuilder.REGISTERED_MODULES.keys())"
```

Example output:

```bash
{
  'ProxiflyProxiedSession':      ProxiflyProxiedSession,      'FreeproxylistProxiedSession': FreeproxylistProxiedSession,
  'IP89ProxiedSession':          IP89ProxiedSession,          'ProxyEliteProxiedSession':    ProxyEliteProxiedSession,
  'IP3366ProxiedSession':        IP3366ProxiedSession,        'KuaidailiProxiedSession':     KuaidailiProxiedSession,
  'KxdailiProxiedSession':       KxdailiProxiedSession,       'ProxydailyProxiedSession':    ProxydailyProxiedSession,
  'ProxydbProxiedSession':       ProxydbProxiedSession,       'ProxyhubProxiedSession':      ProxyhubProxiedSession,
  'ProxylistProxiedSession':     ProxylistProxiedSession,     'QiyunipProxiedSession':       QiyunipProxiedSession,
  'SpysoneProxiedSession':       SpysoneProxiedSession,       'Tomcat1235ProxiedSession':    Tomcat1235ProxiedSession,
  'DatabayProxiedSession':       DatabayProxiedSession,       'FineProxyProxiedSession':     FineProxyProxiedSession,
  'IPLocateProxiedSession':      IPLocateProxiedSession,      'JiliuipProxiedSession':       JiliuipProxiedSession,
  'TheSpeedXProxiedSession':     TheSpeedXProxiedSession,     'GeonodeProxiedSession':       GeonodeProxiedSession,
  'FreeProxyDBProxiedSession':   FreeProxyDBProxiedSession,   'ProxyScrapeProxiedSession':   ProxyScrapeProxiedSession,
  'SCDNProxiedSession':          SCDNProxiedSession,          'GoodIPSProxiedSession':       GoodIPSProxiedSession,
  'SixSixDailiProxiedSession':   SixSixDailiProxiedSession,   'DpangestuwProxiedSession':    DpangestuwProxiedSession,
  'ProxyNovaProxiedSession':     ProxyNovaProxiedSession,     'ProxyShareProxiedSession':    ProxyShareProxiedSession,
  'OpenProxyListProxiedSession': OpenProxyListProxiedSession, 'IPRoyalProxiedSession':       IPRoyalProxiedSession,
  'ADVFPProxiedSession':         ADVFPProxiedSession,         'RoundProxiesProxiedSession':  RoundProxiesProxiedSession,
  'SocksListProxiedSession':     SocksListProxiedSession,     'ProxiwareProxiedSession':     ProxiwareProxiedSession,
  'ProxyFreeOnlyProxiedSession': ProxyFreeOnlyProxiedSession,
}
```

#### Apply stricter filtering

By default, freeproxy:

- validates proxy format,
- de-duplicates results,
- does not aggressively filter by geography/anonymity/speed unless you specify rules.

You can enforce stricter filtering by passing `filter_rule`.

Common fields in filter_rule:

- `country_code`: *e.g.*, `['CN']`, `['US']`
- `anonymity`: `elite`, `anonymous`, `transparent` (string or list)
- `protocol`: `http`, `https`, `socks4`, `socks5` (string or list)
- `max_tcp_ms`: maximum TCP connect latency (ms)
- `max_http_ms`: maximum HTTP request latency to `test_url` (ms)

Example A: only mainland China proxies

```python
from freeproxy.modules.proxies import IP3366ProxiedSession

sess = IP3366ProxiedSession(filter_rule={"country_code": ["CN"]})
sess.refreshproxies()
print(sess.getrandomproxy(proxy_format="freeproxy"))
```

Example B: US + elite anonymity

```python
from freeproxy.modules.proxies import SpysoneProxiedSession

sess = SpysoneProxiedSession(filter_rule={"anonymity": ["elite"], "country_code": ["US"]})
sess.refreshproxies()
print(sess.getrandomproxy(proxy_format="freeproxy"))
```

Example C: constrain protocol + speed

```python
from freeproxy.modules.proxies import FreeproxylistProxiedSession

sess = FreeproxylistProxiedSession(
    filter_rule={
        "protocol": ["http", "https"],
        "max_tcp_ms": 10000,
        "max_http_ms": 10000,
    }
)
sess.refreshproxies()
print(sess.getrandomproxy(proxy_format="freeproxy"))
```

*Note (performance): `max_tcp_ms` / `max_http_ms` may significantly slow down crawling when too many proxies are scraped, because each proxy requires additional testing.*
*In general, it’s better to crawl first, then run a separate post-test script if you need strict speed constraints.*

#### Unified client: `ProxiedSessionClient`

`ProxiedSessionClient` provides a unified interface across proxy sources and behaves like a `requests.Session` with an automatically maintained proxy pool.

- It keeps a proxy pool where all proxies satisfy your `filter_rule`.
- Each `.get()` / `.post()` consumes at least one proxy.
- When the pool is low, it automatically replenishes proxies by scraping again.

Minimal example:

```python
from freeproxy.freeproxy import ProxiedSessionClient

proxy_sources = ["KuaidailiProxiedSession"]
init_proxied_session_cfg = {"filter_rule": {"country_code": ["CN", "US"]}}
client = ProxiedSessionClient(
    proxy_sources=proxy_sources, init_proxied_session_cfg=init_proxied_session_cfg,
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = client.get("https://space.bilibili.com/406756145", headers=headers)
print(resp.text)
```

Quiet mode (suppress logs):

```python
from freeproxy import freeproxy

client = freeproxy.ProxiedSessionClient(
    proxy_sources=["ProxydbProxiedSession"], disable_print=True,
)
```

Init arguments:

- `proxy_sources (list[str])`: proxy sources to use.
- `init_proxied_session_cfg (dict)`: session config; supports:
  - `max_pages`: pages to fetch per source
  - `filter_rule`: filtering rules described above
  - plus standard `requests.Session` options
- `disable_print (bool)`: suppress proxy usage logs.
- `max_tries (int)`: max attempts per `.get()` / `.post()` call.

Example: filter scraped proxies via the unified client

```python
from freeproxy.freeproxy import ProxiedSessionClient

client = ProxiedSessionClient(
    proxy_sources=["ProxyScrapeProxiedSession", "ProxylistProxiedSession"],
    init_proxied_session_cfg={
        "max_pages": 2,
        "filter_rule": {
            "country_code": ["CN"],
            "anonymity": ["elite"],
            "protocol": ["http", "https"],
        },
    },
    disable_print=False,
    max_tries=20,
)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}
resp = client.get("https://www.baidu.com/", timeout=10, headers=headers)
print(resp.text)
resp = client.get("https://httpbin.org/ip", timeout=5)
print(resp.json())
resp = client.get("https://httpbin.org/anything", timeout=15)
print(resp.json())
print("origin:", resp.json().get("origin"))
print("X-Forwarded-For:", resp.json()["headers"].get("X-Forwarded-For"))
print("Forwarded:", resp.json()["headers"].get("Forwarded"))
```

*Final note: you can refer to freeproxy’s source code to unlock more features, the overall codebase is small and easy to navigate.*


# ⭐ Recommended Projects

| Project                                                    | ⭐ Stars                                                                                                                                               | 📦 Version                                                                                                 | ⏱ Last Update                                                                                                                                                                   | 🛠 Repository                                                        |
| -------------                                              | ---------                                                                                                                                             | -----------                                                                                                | ----------------                                                                                                                                                                 | --------                                                             |
| 🎵 **Musicdl**<br/>轻量级无损音乐下载器                    | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/musicdl?style=flat-square)](https://github.com/CharlesPikachu/musicdl)                   | [![Version](https://img.shields.io/pypi/v/musicdl)](https://pypi.org/project/musicdl)                      | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/musicdl?style=flat-square)](https://github.com/CharlesPikachu/musicdl/commits/master)                   | [🛠 Repository](https://github.com/CharlesPikachu/musicdl)           |
| 🎬 **Videodl**<br/>轻量级高清无水印视频下载器              | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/videodl?style=flat-square)](https://github.com/CharlesPikachu/videodl)                   | [![Version](https://img.shields.io/pypi/v/videofetch)](https://pypi.org/project/videofetch)                | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/videodl?style=flat-square)](https://github.com/CharlesPikachu/videodl/commits/master)                   | [🛠 Repository](https://github.com/CharlesPikachu/videodl)           |
| 🖼️ **Imagedl**<br/>轻量级海量图片搜索下载器                | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/imagedl?style=flat-square)](https://github.com/CharlesPikachu/imagedl)                   | [![Version](https://img.shields.io/pypi/v/pyimagedl)](https://pypi.org/project/pyimagedl)                  | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/imagedl?style=flat-square)](https://github.com/CharlesPikachu/imagedl/commits/main)                     | [🛠 Repository](https://github.com/CharlesPikachu/imagedl)           |
| 🌐 **FreeProxy**<br/>全球海量高质量免费代理采集器          | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/freeproxy?style=flat-square)](https://github.com/CharlesPikachu/freeproxy)               | [![Version](https://img.shields.io/pypi/v/pyfreeproxy)](https://pypi.org/project/pyfreeproxy)              | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/freeproxy?style=flat-square)](https://github.com/CharlesPikachu/freeproxy/commits/master)               | [🛠 Repository](https://github.com/CharlesPikachu/freeproxy)         |
| 🌐 **MusicSquare**<br/>简易音乐搜索下载和播放网页          | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/musicsquare?style=flat-square)](https://github.com/CharlesPikachu/musicsquare)           | [![Version](https://img.shields.io/pypi/v/musicdl)](https://pypi.org/project/musicdl)                      | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/musicsquare?style=flat-square)](https://github.com/CharlesPikachu/musicsquare/commits/main)             | [🛠 Repository](https://github.com/CharlesPikachu/musicsquare)       |
| 🌐 **FreeGPTHub**<br/>真正免费的GPT统一接口                | [![Stars](https://img.shields.io/github/stars/CharlesPikachu/FreeGPTHub?style=flat-square)](https://github.com/CharlesPikachu/FreeGPTHub)             | [![Version](https://img.shields.io/pypi/v/freegpthub)](https://pypi.org/project/freegpthub)                | [![Last Commit](https://img.shields.io/github/last-commit/CharlesPikachu/FreeGPTHub?style=flat-square)](https://github.com/CharlesPikachu/FreeGPTHub/commits/main)               | [🛠 Repository](https://github.com/CharlesPikachu/FreeGPTHub)        |


# 📚 Citation

If you use this project in your research, please cite the repository.

```
@misc{freeproxy2022,
    author = {Zhenchao Jin},
    title = {FreeProxy: Collecting free proxies from internet},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/CharlesPikachu/freeproxy}},
}
```


# 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=CharlesPikachu/freeproxy&type=date&legend=top-left)](https://www.star-history.com/#CharlesPikachu/freeproxy&type=date&legend=top-left)


# ☕ Appreciation (赞赏 / 打赏)

| WeChat Appreciation QR Code (微信赞赏码)                                                                                       | Alipay Appreciation QR Code (支付宝赞赏码)                                                                                     |
| :--------:                                                                                                                     | :----------:                                                                                                                   |
| <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/.github/pictures/wechat_reward.jpg" width="260" /> | <img src="https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/.github/pictures/alipay_reward.png" width="260" /> |


# 📱 WeChat Official Account (微信公众号):

Charles的皮卡丘 (*Charles_pikachu*)  
![img](https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/docs/pikachu.jpg)