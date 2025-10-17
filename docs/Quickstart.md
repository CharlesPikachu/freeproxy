# Quick Start

#### Making requests with a proxy-enabled session

Use the following code to make a request to any website with a randomly selected proxy by default,

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

Supported arguments for `ProxiedSessionClient`:

- `proxy_sources` (Default: `['KuaidailiProxiedSession', 'IP3366ProxiedSession']`): The proxy sources to use. Currently supported `['IP89ProxiedSession', 'ZdayeProxiedSession', 'IP3366ProxiedSession', 'KuaidailiProxiedSession', 'ProxylistplusProxiedSession']`.
- `init_proxied_session_cfg` (Default: `{'max_pages': 1}`): Accepts the same options as `requests.Session`, plus an extra `max_pages` field that specifies how many pages of proxies to fetch from each free source.
- `disable_print` (Default: `False`): Whether to suppress proxy usage logs in the terminal.

Supported arguments for `proxied_session_client.get` is the same as [requests.Session.get](https://requests.readthedocs.io/en/latest/).

Supported arguments for `proxied_session_client.post` is the same as [requests.Session.post](https://requests.readthedocs.io/en/latest/).

#### Retrieve a random free proxy

The following snippet selects a random proxy from the pool,

```python
from freeproxy import ProxiedSessionClient

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources)
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
from freeproxy import ProxiedSessionClient

proxy_sources = ['KuaidailiProxiedSession']
proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources)
proxied_session_name, proxied_session = proxied_session_client.getrandomproxiedsession()
print(proxied_session_name, proxied_session)
```

Example output,

```
('KuaidailiProxiedSession', <modules.proxies.kuaidaili.KuaidailiProxiedSession object at 0x000002CE2D137220>)
```
