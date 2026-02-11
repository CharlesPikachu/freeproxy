# Quick Start

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
  'FreeProxyDBProxiedSession', 'ProxyScrapeProxiedSession', 'SCDNProxiedSession'
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

