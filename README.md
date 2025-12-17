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

- 2025-12-03: Released pyfreeproxy v0.3.1 — Add support for more proxy sources to make a massive proxy pool a reality.
- 2025-12-03: Released pyfreeproxy v0.3.0 — Code refactoring, removal of two low-quality free proxy sources, addition of multiple high-quality free proxy sources, and introduction of more features such as proxy rule filtering, more stable proxy scraping, and so on.
- 2025-11-19: Released pyfreeproxy v0.2.2 — Fix potential in-place modified bugs.
- 2025-11-16: Released pyfreeproxy v0.2.1 — Add support for ZdayeProxiedSession and FineProxyProxiedSession.
- 2025-11-16: Released pyfreeproxy v0.2.0 — Refactored the code to improve the quality of the retrieved proxies and added support for fetching proxies from seven additional free proxy sources.


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

#### Common Usage Scenarios

After installing freeproxy, you can write a script like this to gather basic statistics about the proxy sources you want to use and save all the retrieved proxies to a specified JSON file:

```python
import json
import random
from tqdm import tqdm
from freeproxy.modules import BaseProxiedSession, ProxyInfo, BuildProxiedSession, printtable, colorize

'''main'''
def main():
    # proxy_sources
    proxy_sources = ['ProxiflyProxiedSession', 'KuaidailiProxiedSession', 'QiyunipProxiedSession', 'ProxylistProxiedSession']
    # iter scraping
    free_proxies = {}
    print_titles, print_items = ['Source', 'Retrieved Examples', 'HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5', 'Chinese IP', 'Elite', 'Total'], []
    for proxy_source in tqdm(proxy_sources):
        try:
            module_cfg = {'max_pages': 1, 'type': proxy_source, 'disable_print': False}
            proxied_session: BaseProxiedSession = BuildProxiedSession(module_cfg=module_cfg)
            candidate_proxies: list[ProxyInfo] = proxied_session.refreshproxies()
        except:
            candidate_proxies = []
        if len(candidate_proxies) > 0:
            example_proxy = random.choice(candidate_proxies).proxy
            count_http = sum([(p.protocol.lower() in ['http']) for p in candidate_proxies])
            count_https = sum([(p.protocol.lower() in ['https']) for p in candidate_proxies])
            count_socks4 = sum([(p.protocol.lower() in ['socks4']) for p in candidate_proxies])
            count_socks5 = sum([(p.protocol.lower() in ['socks5']) for p in candidate_proxies])
            count_cn = sum([p.in_chinese_mainland for p in candidate_proxies])
            count_elite = sum([(p.anonymity.lower() in ['elite']) for p in candidate_proxies])
            print_items.append([
                proxy_source.removesuffix('ProxiedSession'), colorize(example_proxy, 'green'), colorize(count_http, 'number'), colorize(count_https, 'number'), 
                colorize(count_socks4, 'number'), colorize(count_socks5, 'number'), colorize(count_cn, 'number'), colorize(count_elite, 'number'),
                colorize(len(candidate_proxies), 'number'),
            ])
        else:
            print_items.append([
                proxy_source.removesuffix('ProxiedSession'), 'NULL', colorize('0', 'number'), colorize('0', 'number'), 
                colorize('0', 'number'), colorize('0', 'number'), colorize('0', 'number'), colorize('0', 'number'),
                colorize(len(candidate_proxies), 'number'),
            ])
        free_proxies[proxy_source] = [p.todict() for p in candidate_proxies]
    # visualize scraping results
    print("The proxy distribution for each source you specified is as follows:")
    printtable(titles=print_titles, items=print_items, terminal_right_space_len=1)
    # save scraping results
    json.dump(free_proxies, open('free_proxies.json', 'w'), indent=2)

'''tests'''
if __name__ == '__main__':
    main()
```

The terminal output of the above code will look roughly like this:

```bash
C:\Users\xxxx\Desktop>python naive_scraping_proxies.py
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:37<00:00,  9.38s/it]
The proxy distribution for each source you specified is as follows:
+-----------+------------------------------+------+-------+--------+--------+------------+-------+-------+
|   Source  |      Retrieved Examples      | HTTP | HTTPS | SOCKS4 | SOCKS5 | Chinese IP | Elite | Total |
+-----------+------------------------------+------+-------+--------+--------+------------+-------+-------+
|  Proxifly | socks4://69.61.200.104:36181 | 5975 |   0   |  706   |  365   |     21     |  4052 |  7046 |
| Kuaidaili | https://118.175.131.176:3128 |  20  |   13  |   0    |   0    |     18     |   33  |   33  |
|  Qiyunip  | http://112.244.231.189:9000  |  6   |   9   |   0    |   0    |     15     |   12  |   15  |
| Proxylist |  http://185.88.177.197:8936  | 287  |   8   |  114   |   83   |     33     |  368  |  492  |
+-----------+------------------------------+------+-------+--------+--------+------------+-------+-------+
```

All proxies will be saved to `free_proxies.json` in the current directory, in a format similar to this:

```
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
    },
    ...
  ],
  "ProxiflyProxiedSession": [...],
  "QiyunipProxiedSession": [...],
  "ProxylistProxiedSession": [...],
}
```

In the above code, you can also set the `max_pages` argument to a larger value to obtain a larger number of high-quality proxies.

You can also enter the following command in the terminal to list all proxy sources supported by your current version of freeproxy:

```bash
python -c "from freeproxy.modules import ProxiedSessionBuilder; print(ProxiedSessionBuilder.REGISTERED_MODULES.keys())"
```

Sample output is as follows:

```python
dict_keys([
  'ProxiflyProxiedSession', 'FreeproxylistProxiedSession', 'IhuanProxiedSession', 'IP89ProxiedSession', 'IP3366ProxiedSession', 
  'KuaidailiProxiedSession', 'KxdailiProxiedSession', 'ProxydailyProxiedSession', 'ProxydbProxiedSession', 'ProxyhubProxiedSession', 
  'ProxylistProxiedSession', 'QiyunipProxiedSession', 'SpysoneProxiedSession', 'Tomcat1235ProxiedSession'
])
```

#### Stricter Proxy Filtering Strategy

By default, freeproxy fetches all proxies provided by the specified free proxy sources, only validating their format and performing simple de-duplication.
If you want to further filter the crawled proxies to obtain a higher-quality proxy pool, you can do so by setting the `filter_rule` argument.

For example, if you want to ensure that the proxy IPs are located in mainland China, you can do the following:

```python
from freeproxy.modules.proxies import IP3366ProxiedSession

ip3366_session = IP3366ProxiedSession(filter_rule={'country_code': ['CN']})
# all obtained proxies can be accessed by `ip3366_session.candidate_proxies`
print(ip3366_session.getrandomproxy(proxy_format='freeproxy'))
```

Sample output is as follows:

```python
ProxyInfo(
  source='IP3366ProxiedSession', 
  protocol='https', 
  ip='114.231.82.145', 
  port='8888', 
  country_code='CN', 
  in_chinese_mainland=True, 
  anonymity='elite', 
  delay=3000, 
  test_timeout=5, 
  test_url='http://www.baidu.com', 
  test_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}, 
  failed_connection_default_timeout=3600000, 
  created_at=datetime.datetime(2025, 12, 3, 14, 3, 42, 535847), 
  extra={}
)
```

If you want high-anonymity proxies whose addresses are in the United States, you can do the following:

```python
from freeproxy.modules.proxies import SpysoneProxiedSession

spy_session = SpysoneProxiedSession(filter_rule={'anonymity': ['elite'], 'country_code': ['US']})
# all obtained proxies can be accessed by `spy_session.candidate_proxies`
print(spy_session.getrandomproxy(proxy_format='freeproxy'))
```

Sample output is as follows:

```python
ProxyInfo(
  source='SpysoneProxiedSession', 
  protocol='http', 
  ip='88.216.98.209', 
  port=48852, 
  country_code='US',
  in_chinese_mainland=False, 
  anonymity='elite', 
  delay=21515, 
  test_timeout=5, 
  test_url='http://www.baidu.com', 
  test_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}, 
  failed_connection_default_timeout=3600000, 
  created_at=datetime.datetime(2025, 12, 3, 14, 17, 41, 502702), 
  extra={}
)
```

The `anonymity` argument can be either a single string or a list. 
The available options include `elite` (high anonymity proxies), `anonymous` (standard anonymous proxies), and `transparent` (transparent proxies).

If you have specific requirements for the proxy type, you can set the `protocol` argument. 
If you care about server response speed, you can set the `max_tcp_ms` or `max_http_ms` arguments.
An example code snippet can be written as follows:

```python
from freeproxy.modules.proxies import FreeproxylistProxiedSession

fpl_session = FreeproxylistProxiedSession(filter_rule={'protocol': ['http', 'https'], 'max_tcp_ms': 10000, 'max_http_ms': 10000})
# all obtained proxies can be accessed by `fpl_session.candidate_proxies`
print(fpl_session.getrandomproxy(proxy_format='freeproxy'))
```

The above code means that it only retrieves HTTP and HTTPS proxies, 
requires the TCP connection latency between your machine and the proxy server to be no more than 10,000 ms, 
and also requires the proxy server’s response time when requesting the `test_url` (which defaults to http://www.baidu.com) to be no more than 10,000 ms.

The `protocol` argument can be either a single string or a list. 
The available options include `http`, `https`, `socks4` and `socks5`.

Currently, the implementation of freeproxy does not use asynchronous operations or spawn a large number of threads for parallel testing. 
Therefore, when too many proxies are scraped, setting `max_tcp_ms` or `max_http_ms` can cause the program to freeze for a long time. 
In general, it is not recommended to use these two speed-test arguments during crawling; if needed, you can run a separate script to test the proxies after the crawl is finished.

#### `freeproxy.freeproxy.ProxiedSessionClient`

`ProxiedSessionClient` provides a unified interface for all supported proxy sources. You can call it as shown in the following example:

```python
from freeproxy.freeproxy import ProxiedSessionClient

proxy_sources = ['KuaidailiProxiedSession']
init_proxied_session_cfg = {'filter_rule': {'country_code': ['CN', 'US']}}
proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources, init_proxied_session_cfg=init_proxied_session_cfg)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
resp = proxied_session_client.get('https://space.bilibili.com/406756145', headers=headers)
print(resp.text)
```

When using freeproxy as a third-party package, if you don’t want it to print too much extra information, you can set `disable_print=True`, for example:`

```python
from freeproxy import freeproxy

proxy_sources = ['ProxydbProxiedSession']
proxied_session_client = freeproxy.ProxiedSessionClient(proxy_sources=proxy_sources, disable_print=True)
```

`ProxiedSessionClient` automatically maintains a proxy pool in which all proxies satisfy the `filter_rule` criteria. 
Each time you call the `.get` or `.post` method, it will consume at least one proxy from the pool, and when the pool is running low, 
it will automatically fetch and replenish more proxies. 
The usage of `.get` and `.post` is exactly the same as `requests.get` and `requests.post`.

The arguments supported when initializing the `ProxiedSessionClient` class are as follows:

- `proxy_sources` (`list`): The proxy sources to use. Currently supported proxies see [Supported Proxy Sources](https://github.com/CharlesPikachu/freeproxy?tab=readme-ov-file#-supported-proxy-sources) or call `from freeproxy.modules import ProxiedSessionBuilder; print(ProxiedSessionBuilder.REGISTERED_MODULES.keys())`.
- `init_proxied_session_cfg` (`dict`): Accepts the same options as `requests.Session`, plus an extra `max_pages` field and an extra `filter_rule` field that specifies how many pages of proxies to fetch from each free source and the rules to filter fetched proxies.
- `disable_print` (`bool`): Whether to suppress proxy usage logs in the terminal.
- `max_tries` (`int`): The maximum number of attempts for each `.get` and `.post` call.

You can refer to freeproxy’s source code to unlock more features. The overall codebase is not very large.


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