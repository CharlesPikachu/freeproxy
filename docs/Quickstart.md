# 快速开始

## FreeProxy类

实例化FreeProxy类的示例代码如下：

```python
from freeproxy import freeproxy

proxy_sources = ['proxylistplus', 'kuaidaili']
proxy_session = freeproxy.FreeProxy(proxy_sources=proxy_sources)
```

FreeProxy支持的参数如下：

- proxy_type: 代理类型, 支持"https", "http"和"all", 默认值为"all";
- proxy_sources: 代理获取源, 支持"kuaidaili", "ip3366", "jiangxianli", "proxylistplus", "daili66", "fatezero", "ip89", "seofangfa", "zdaye", "yqie", "taiyanghttp", 默认值为None, 即使用所有代理源;
- init_session_cfg: 初始化session的参数, 支持的变量同[requests.Session](https://docs.python-requests.org/en/latest/), 默认值为{};
- logfilepath: 日志文件, 如果是None, 则不打印, 默认值为"freeproxy.log"。


## GET请求

代码示例如下：

```python
from freeproxy import freeproxy

proxy_sources = ['proxylistplus', 'kuaidaili']
proxy_session = freeproxy.FreeProxy(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
response = proxy_session.get('https://space.bilibili.com/406756145', headers=headers)
print(response.text)
```

GET请求支持的参数同[requests.Session.get](https://docs.python-requests.org/en/latest/)


## POST请求

代码示例如下：

```python
from freeproxy import freeproxy

proxy_sources = ['proxylistplus', 'kuaidaili']
proxy_session = freeproxy.FreeProxy(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
response = proxy_session.post('https://space.bilibili.com/406756145', headers=headers)
print(response.text)
```

POST请求支持的参数同[requests.Session.post](https://docs.python-requests.org/en/latest/)