# Quick Start

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