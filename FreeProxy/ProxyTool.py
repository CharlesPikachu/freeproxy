'''
Function:
	免费代理获取工具
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import os
import time
import random
try:
	from .proxies import *
	from .utils import *
except:
	from proxies import *
	from utils import *


'''
Function:
	免费代理获取工具
Args:
	--host: 验证代理是否可以请求host(默认为http://www.baidu.com/)
	--headers: 验证host时的请求头
	--method: 验证host时的请求类型(GET/POST)
	--post_data: POST验证时提交的data
	--timeout: 代理最大延迟
	--proxy_type: http/https, 代理类型
'''
class ProxyTool():
	def __init__(self, host='http://www.baidu.com/', headers=None, method='GET', post_data={}, timeout=1, proxy_type='http', **kwargs):
		self.info = 'ProxyTool(v0.1.1) -- Collecting free proxies from internet.'
		self.author = 'Charles'
		self.host = host
		self.headers = headers
		self.method = method.upper()
		self.post_data = post_data
		self.timeout = timeout
		self.proxy_type = proxy_type.lower()
		self.__verifyInitial(kwargs.get('verify_host'))
		self.free_proxy_sources = [xici.xici(), gatherproxy.gatherproxy(), jiangxianli.jiangxianli(), cnproxy.cnproxy(),
								   ip3366.ip3366(), iphai.iphai(), proxylist.proxylist(), proxylistplus.proxylistplus()]
		self.checker = ProxyChecker()
	'''获取代理'''
	def getProxy(self, num_proxies=1, max_tries=5):
		proxies = []
		num_tries = 0
		while len(proxies) != num_proxies:
			num_tries += 1
			free_proxy_source = random.choice(self.free_proxy_sources)
			for ip_port in free_proxy_source.get():
				if self.checker.check(ip_port, host=self.host, headers=self.headers, method=self.method, timeout=self.timeout, post_data=self.post_data, proxy_type=self.proxy_type):
					proxies.append(ip_port)
				if len(proxies) == num_proxies:
					break
			if num_tries == max_tries:
				break
		return proxies
	'''初始化校验'''
	def __verifyInitial(self, verify_host):
		if self.method != 'GET' and self.method != 'POST':
			raise ValueError('Argument<method> in class ProxyTool expect <GET> or <POST>, but get <%s>...' % self.method)
		if self.proxy_type != 'http' and self.proxy_type != 'https':
			raise ValueError('Argument<proxy_type> in class ProxyTool expect <http> or <https>, but get <%s>...' % self.proxy_type)
		if not (isinstance(self.timeout, int) or isinstance(self.timeout, float)):
			try:
				self.timeout = float(self.timeout)
			except:
				raise ValueError('Argument<timeout> in class ProxyTool expect <int> or <float> type, but get <%s> type...' % type(self.proxy_type))
		if verify_host:
			host = self.host.replace('http://', '').replace('https://', '')
			if host[-1] == '/':
				host = host[:-1]
			if os.system('ping %s' % host) == 1:
				raise ValueError('Argument<host> in class ProxyTool is an invalid host...')
	'''return info'''
	def __repr__(self):
		return '[Author]: %s, [Introduction]: %s' % (self.author, self.info)


# for test
if __name__ == '__main__':
	pt = ProxyTool()
	print(pt.getProxy(num_proxies=1))