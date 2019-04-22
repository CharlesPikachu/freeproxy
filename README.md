# FreeProxy
```sh
ProxyTool--Collecting free proxies from internet.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Introduction in Chinese


# Proxy sources
- [xici](http://www.xicidaili.com/)
- [iphai](http://www.iphai.com/free/ng)
- [ip3366](http://www.ip3366.net/free/)
- [cn-proxy](https://cn-proxy.com/)
- [proxylist](https://proxy-list.org/english/index.php)
- [jiangxianli](http://ip.jiangxianli.com/?page=1)
- [gatherproxy](http://www.gatherproxy.com/zh/)
- [proxylistplus](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)

# Install
### Use setup.py
#### Step1
```sh
git clone https://github.com/CharlesPikachu/FreeProxy.git
```
#### Step2
```sh
cd FreeProxy -> run "python setup.py install"
```
### Use pip
```sh
pip install git+https://github.com/CharlesPikachu/FreeProxy.git@master
```

# Usage
#### Arguments
```sh
Input:
	ProxyTool:
		initial:
			--host: Host used to verify the validity of the proxies.(http://www.baidu.com/ by default)
			--headers: Used to add HTTP headers to a request for host.
			--method: Request method, expect GET(default)/POST.
			--post_data: The post data if method is POST.
			--timeout: Connection timeouts.
			--proxy_type: http/https, the type of proxy.
		getProxy:
			--num_proxies: The number of proxies you need.
			--max_tries: Return the proxies if try to get enough proxies more max_tries times.
Return:
	[(ip_1, port_1), ..., (ip_n, port_n]
```
#### Example
```python
from FreeProxy import ProxyTool
pt = ProxyTool()
proxies = pt.getProxy(num_proxies=2, max_tries=5)
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](pikachu.jpg)