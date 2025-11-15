# Quick Start

## Example Usage

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
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('True', 'green'), ','.join([f'{k.upper()}: {v}' for k, v in candidate_proxies[0].items()])])
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

- `proxy_sources` (`list`, default: `['KuaidailiProxiedSession', 'IP3366ProxiedSession']`): The proxy sources to use. Currently supported `['IP89ProxiedSession', 'ZdayeProxiedSession', 'IP3366ProxiedSession', 'KuaidailiProxiedSession', 'ProxylistplusProxiedSession', 'QiyunipProxiedSession', 'ProxyhubProxiedSession', 'ProxydbProxiedSession']`.
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
{'http': 'http://103.158.62.186:8088', 'https': 'http://103.158.62.186:8088'}
```

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
