# Quick Start

#### Example Usage

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
+---------------+---------------+-------------------------------+-------+
|     Source    | Effectiveness |       Retrieved Examples      | Total |
+---------------+---------------+-------------------------------+-------+
|      IP89     |      True     |   http://113.223.214.73:8089  |  199  |
|     IP3366    |      True     |    http://36.6.145.198:8089   |   30  |
|   Kuaidaili   |      True     |    http://103.85.53.62:8080   |   36  |
| Proxylistplus |      True     |   http://110.77.134.112:8080  |   50  |
|    Qiyunip    |      True     |  https://183.164.243.79:8089  |   15  |
|   Proxydaily  |      True     |   http://3.122.235.189:55607  |   7   |
|    Proxyhub   |      True     | socks4://165.22.220.151:36362 |   20  |
|    Proxydb    |      True     |    http://45.186.6.104:3128   |   30  |
|   Tomcat1235  |      True     |  socks5://188.235.21.247:2080 |   30  |
|    Spysone    |      True     |  http://201.238.248.136:9229  |   30  |
| Freeproxylist |      True     |  https://128.140.113.110:3128 |  300  |
|   Proxylist   |      True     |   http://188.166.30.17:8888   |  2082 |
|    Kxdaili    |      True     |   http://116.63.160.98:8899   |   40  |
|     Ihuan     |      True     |   http://189.90.255.208:3128  |  2607 |
+---------------+---------------+-------------------------------+-------+
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

#### Making requests with a proxy-enabled session

Use the following code to make a request to any website with a randomly selected proxy by default,

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

Supported arguments for `ProxiedSessionClient`:

- `proxy_sources` (`list`, default: `['KuaidailiProxiedSession', 'IP3366ProxiedSession', 'QiyunipProxiedSession', 'Tomcat1235ProxiedSession', 'ProxydailyProxiedSession', 'SpysoneProxiedSession']`): The proxy sources to use. Currently supported proxies see [Supported Proxy Sources](https://github.com/CharlesPikachu/freeproxy?tab=readme-ov-file#-supported-proxy-sources) or call `from freeproxy.modules import ProxiedSessionBuilder; ProxiedSessionBuilder.REGISTERED_MODULES.keys()`.
- `init_proxied_session_cfg` (`dict`, default: `{'max_pages': 1}`): Accepts the same options as `requests.Session`, plus an extra `max_pages` field that specifies how many pages of proxies to fetch from each free source.
- `disable_print` (`bool`, default: `False`): Whether to suppress proxy usage logs in the terminal.

Supported arguments for `proxied_session_client.get` is the same as [requests.Session.get](https://requests.readthedocs.io/en/latest/).

Supported arguments for `proxied_session_client.post` is the same as [requests.Session.post](https://requests.readthedocs.io/en/latest/).

#### Retrieve a random free proxy

The following snippet selects a random proxy from the pool,

```python
from freeproxy import freeproxy

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = freeproxy.ProxiedSessionClient(proxy_sources=proxy_sources)
proxy = proxied_session_client.getrandomproxy()
print(proxy)
```

Example output,

```
{'http': 'http://103.158.62.186:8088', 'https': 'socks5://103.158.62.186:8088'}
```

You should note that our proxy output format follows the `proxies` format used by the `requests` module. 
In other words, for `'https': 'socks5://103.158.62.186:8088'`, the proxy protocol is `socks5`, not `https`.

#### Retrieve a random proxied session

The following snippet initializes a `proxied_session` restricted to one proxy source (randomly sampled):

```python
from freeproxy import freeproxy

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = freeproxy.ProxiedSessionClient(proxy_sources=proxy_sources)
proxied_session_name, proxied_session = proxied_session_client.getrandomproxiedsession()
print(proxied_session_name, proxied_session)
```

Example output,

```
('KuaidailiProxiedSession', <modules.proxies.kuaidaili.KuaidailiProxiedSession object at 0x000002CE2D137220>)
```
