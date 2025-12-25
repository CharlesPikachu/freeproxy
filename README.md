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
    <img src="https://static.pepy.tech/badge/pyfreeproxy" alt="PyPI - Downloads">
  </a>
  <a href="https://pypi.org/project/pyfreeproxy/">
    <img src="https://static.pepy.tech/badge/pyfreeproxy/month" alt="PyPI - Downloads">
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

  <h3>⚡ Live Proxies <span style="font-size:0.9em;">(最新免费高质量代理, 每小时更新一次)</span></h3>
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

- 2025-12-23: Released pyfreeproxy v0.3.2 — Add a new free proxy source, with automatic retrieval of the FineProxy nonce parameter.
- 2025-12-03: Released pyfreeproxy v0.3.1 — Add support for more proxy sources to make a massive proxy pool a reality.
- 2025-12-03: Released pyfreeproxy v0.3.0 — Code refactoring, removal of two low-quality free proxy sources, addition of multiple high-quality free proxy sources, and introduction of more features such as proxy rule filtering, more stable proxy scraping, and so on.
- 2025-11-19: Released pyfreeproxy v0.2.2 — Fix potential in-place modified bugs.


# 📘 Introduction

FreeProxy continuously discovers and updates lists of free proxies. If you find value here, please star the project to keep it on your radar.


# 🌐 Supported Proxy Sources

| Proxy Source (EN)                                                                      | Proxy Source (CN)                                                           | HTTP         | HTTPS      | SOCKS4     | SOCKS5     | Code Snippet                                                                                                            |
| :----:                                                                                 | :----:                                                                      | :----:       | :----:     | :----:     | :----:     | :----:                                                                                                                  |
| [KuaidailiProxiedSession](https://www.kuaidaili.com/free/inha/1/)                      | [快代理](https://www.kuaidaili.com/free/inha/1/)                            | ✔           | ✔         | ❌         | ❌         | [kuaidaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kuaidaili.py)          |
| [IP3366ProxiedSession](http://www.ip3366.net/free/?stype=1&page=1)                     | [云代理](http://www.ip3366.net/free/?stype=1&page=1)                        | ✔           | ✔         | ❌         | ❌         | [ip3366.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip3366.py)                |
| [IP89ProxiedSession](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)  | [IP89](http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp=)     | ✔           | ❌         | ❌         | ❌         | [ip89.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ip89.py)                    |
| [QiyunipProxiedSession](https://www.qiyunip.com/freeProxy/1.html)                      | [齐云代理](https://www.qiyunip.com/freeProxy/1.html)                        | ✔           | ✔         | ❌         | ❌         | [qiyunip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/qiyunip.py)              |
| [ProxyhubProxiedSession](https://proxyhub.me/)                                         | [ProxyHub](https://proxyhub.me/)                                            | ✔           | ✔         | ✔         | ✔         | [proxyhub.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyhub.py)            |
| [ProxydbProxiedSession](https://proxydb.net/?offset=0)                                 | [ProxyDB](https://proxydb.net/?offset=0)                                    | ✔           | ✔         | ❌         | ✔         | [proxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydb.py)              |
| [Tomcat1235ProxiedSession](https://tomcat1235.nyc.mn/proxy_list?page=1)                | [北极光代理](https://tomcat1235.nyc.mn/proxy_list?page=1)                   | ❌           | ❌         | ❌         | ✔         | [tomcat1235.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/tomcat1235.py)        |
| [ProxydailyProxiedSession](https://proxy-daily.com/)                                   | [ProxyDaily](https://proxy-daily.com/)                                      | ✔           | ✔         | ✔         | ✔         | [proxydaily.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxydaily.py)        |
| [SpysoneProxiedSession](https://spys.one/en/free-proxy-list/)                          | [SPYS.ONE](https://spys.one/en/free-proxy-list/)                            | ✔           | ❌         | ❌         | ✔         | [spysone.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/spysone.py)              |
| [FreeproxylistProxiedSession](https://free-proxy-list.net/)                            | [FreeProxyList](https://free-proxy-list.net/)                               | ✔           | ✔         | ❌         | ❌         | [freeproxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/freeproxylist.py)  |
| [KxdailiProxiedSession](http://www.kxdaili.com/dailiip.html)                           | [开心代理](http://www.kxdaili.com/dailiip.html)                             | ✔           | ✔         | ❌         | ❌         | [kxdaili.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/kxdaili.py)              |
| [ProxylistProxiedSession](https://www.proxy-list.download/HTTP/)                       | [ProxyList](https://www.proxy-list.download/HTTP/)                          | ✔           | ✔         | ✔         | ✔         | [proxylist.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxylist.py)          |
| [IhuanProxiedSession](https://ip.ihuan.me/?page=4ce63706)                              | [小幻代理](https://ip.ihuan.me/?page=4ce63706)                              | ✔           | ✔         | ❌         | ❌         | [ihuan.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/ihuan.py)                  |
| [ProxiflyProxiedSession](https://proxifly.dev/)                                        | [Proxifly](https://proxifly.dev/)                                           | ✔           | ✔         | ✔         | ✔         | [proxifly.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxifly.py)            |
| [FineProxyProxiedSession](https://fineproxy.org/cn/free-proxy/)                        | [FineProxy](https://fineproxy.org/cn/free-proxy/)                           | ✔           | ✔         | ✔         | ✔         | [fineproxy.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/fineproxy.py)          |
| [DatabayProxiedSession](https://databay.com/free-proxy-list)                           | [Databay](https://databay.com/free-proxy-list)                              | ✔           | ✔         | ❌         | ✔         | [databay.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/databay.py)              |
| [IPLocateProxiedSession](https://www.iplocate.io/)                                     | [IPLocate](https://www.iplocate.io/)                                        | ✔           | ✔         | ✔         | ✔         | [iplocate.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/iplocate.py)            |
| [JiliuipProxiedSession](https://www.jiliuip.com/free/page-1/)                          | [积流代理](https://www.jiliuip.com/free/page-1/)                            | ✔           | ❌         | ❌         | ❌         | [jiliuip.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/jiliuip.py)              |
| [TheSpeedXProxiedSession](https://github.com/TheSpeedX)                                | [TheSpeedX](https://github.com/TheSpeedX)                                   | ✔           | ❌         | ✔         | ✔         | [thespeedx.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/thespeedx.py)          |
| [GeonodeProxiedSession](https://geonode.com/free-proxy-list)                           | [Geonode](https://geonode.com/free-proxy-list)                              | ✔           | ✔         | ✔         | ✔         | [geonode.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/geonode.py)              |
| [FreeProxyDBProxiedSession](https://freeproxydb.com/)                                  | [FreeProxyDB](https://freeproxydb.com/)                                     | ✔           | ❌         | ✔         | ✔         | [freeproxydb.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/freeproxydb.py)      |
| [ProxyScrapeProxiedSession](https://proxyscrape.com/free-proxy-list)                   | [ProxyScrape](https://proxyscrape.com/free-proxy-list)                      | ✔           | ❌         | ✔         | ✔         | [proxyscrape.py](https://github.com/CharlesPikachu/freeproxy/blob/master/freeproxy/modules/proxies/proxyscrape.py)      |


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

Please note that some proxy sources need to be crawled using [Playwright](https://playwright.dev/). 
Playwright will automatically download and configure the browser drivers, so there is no need to worry — it is not malware. 
For more details, you can refer to the [official Playwright documentation](https://playwright.dev/docs/intro).


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

All proxies are saved to `free_proxies.json` in the current directory, e.g.:

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
dict_keys([
  'ProxiflyProxiedSession', 'FreeproxylistProxiedSession', 'IhuanProxiedSession', 'IP89ProxiedSession', 
  'IP3366ProxiedSession', 'KuaidailiProxiedSession', 'KxdailiProxiedSession', 'ProxydailyProxiedSession', 
  'ProxydbProxiedSession', 'ProxyhubProxiedSession', 'ProxylistProxiedSession', 'QiyunipProxiedSession', 
  'SpysoneProxiedSession', 'Tomcat1235ProxiedSession', 'DatabayProxiedSession', 'FineProxyProxiedSession', 
  'IPLocateProxiedSession', 'JiliuipProxiedSession', 'TheSpeedXProxiedSession', 'GeonodeProxiedSession', 
  'FreeProxyDBProxiedSession', 'ProxyScrapeProxiedSession'
])
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
    proxy_sources=["KuaidailiProxiedSession"],
    init_proxied_session_cfg={
        "max_pages": 2,
        "filter_rule": {
            "country_code": ["US"],
            "anonymity": ["elite"],
            "protocol": ["http", "https"],
        },
    },
    disable_print=False,
    max_tries=3,
)
resp = client.get("https://httpbin.org/ip", timeout=10)
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