# FreeProxy
```sh
ProxyTool--Collecting free proxies from internet.
Open an issues to get helps if you have any problems or suggestions.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Introduction in Chinese
https://mp.weixin.qq.com/s/OdBr2KhBDzmBI1GPFQteGQ

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
			--headers: Used to add HTTP headers to a request for host.(use user-agent of chrome by default)
			--method: Request method, expect GET(by default)/POST.
			--post_data: The post data if method is POST.({} by default)
			--timeout: Connection timeouts.(1s by default)
			--proxy_type: http/https, the type of proxy.(http by default)
		getProxy:
			--num_proxies: The number of proxies you need.(1 by default)
			--max_tries: Return the proxies if try to get enough proxies more max_tries times.(5 by default)
Return:
	[(ip_1, port_1), ..., (ip_n, port_n]
```
#### Example1 - Singlethreading
```python
from FreeProxy import ProxyTool
pt = ProxyTool.ProxyTool()
proxies = pt.getProxy(num_proxies=2, max_tries=5)
print(proxies)
```
#### Example2 - Multithreading
```python
import time
import threading
from FreeProxy import ProxyTool


PROXIES = []
pt = ProxyTool.ProxyTool()
num_threadings = 3


def getProxy(num, max_tries):
	global PROXIES
	PROXIES += pt.getProxy(num, max_tries)


for i in range(num_threadings):
	t = threading.Thread(target=getProxy, args=(1, 5))
	time.sleep(0.1)
	t.start()
	t.join()
print(PROXIES)
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](pikachu.jpg)