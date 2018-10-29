# 作者: Charles
# 公众号: Charles的皮卡丘
# 免费代理获取工具
'''
目前支持的平台:
	-西刺代理爬取: xici.xici()
	-秘密代理爬取: mimiip.mimiip()
	-快代理爬取: kuaidaili.kuaidaili()
	-66ip代理爬取: ip66.ip66()
	-无忧代理爬取: data5u.data5u()
	-云代理爬取: ip3366.ip3366()
	-ip海代理爬取: iphai.iphai()
	-免费代理IP库代理爬取: jiangxianli.jiangxianli()
'''
import time
import random
if __name__ == '__main__':
	from proxies import *
	from utils.utils import *
else:
	from .proxies import *
	from .utils.utils import *


# 代理获取工具
class proxytool():
	def __init__(self):
		self.proxynames = ['xici', '66ip', 'kuaidaili', 'mimiip', 'data5u', 'ip3366', 'iphai', 'jiangxianli']
		# avoid using the same api while retry
		self.usedapi = []
		self.author = '作者: Charles'
		self.info = '公众号: Charles的皮卡丘'
		self.version = '0.1.0'
		self.usage = '''
Callable function:
	get(num, api, **kwargs): 获取并检测代理有效性
		Input:
			-num(默认为1): 需要的代理数量
			-api(默认为random): 指定抓取的网站, 可选项为'xici', '66ip', 'kuaidaili', 'data5u', 'mimiip', 'ip3366', 'iphai', 'jiangxianli', 'random'
			-retry(默认为5): 若无法获得足量代理, 重新搜索次数 
			-page(默认抓第一页,一般第一页是最新的): 抓取的页码
			-proxy_type(默认为all): 代理类型, 可选项为'all', 'http', 'https'
			-quality(默认为all): 高(普)匿代理/普通代理, 可选项为'all', 'anonymous', 'common'
			-headers(User-agent), method(GET), host(baidu.com)
		Return:
			-proxy_list: [(ip, port), ...]
	get_proxy(page, proxy_type, quality, api): 获取代理
	check_proxy(ip_port, host, headers, method): 检测代理有效性
	print_help(): 打印使用帮助
	print_about(): 关于作者
'''
	# 获取并检测代理有效性
	def get(self, num=1, api='random', retry=5, **kwargs):
		validproxy_list = []
		page = kwargs.get('page')
		while True:
			retry -= 1
			if retry < 2 and api != 'random':
				page += 1
			proxiesGot = self.get_proxy(page=page, 
										proxy_type=kwargs.get('proxy_type'), 
										quality=kwargs.get('quality'),
										api=api)
			for proxy in proxiesGot:
				res = self.check_proxy(proxy, 
									   host=kwargs.get('host'), 
									   headers=kwargs.get('headers'), 
									   method=kwargs.get('method'))
				if res and proxy not in validproxy_list:
					validproxy_list.append(proxy)
				if len(validproxy_list) == num:
					break
			if (len(validproxy_list) == num) or retry < 0:
				break
			time.sleep(1)
		return validproxy_list
	# 获取代理
	def get_proxy(self, page, proxy_type, quality, api):
		if proxy_type is None:
			proxy_type = 'all'
		if page is None:
			page = 1
		if quality is None:
			quality = 'all'
		if api is None:
			api = 'random'
		if (api == 'random') or (api not in self.proxynames):
			while True:
				api = random.choice(self.proxynames)
				if api not in self.usedapi:
					self.usedapi.append(api)
				break
		apiClass = self.__get_api_by_classname(classname=api)
		proxiesGot = apiClass.get(page=page, proxy_type=proxy_type, quality=quality)
		return proxiesGot
	# 检测代理有效性
	def check_proxy(self, ip_port, host, headers, method):
		if host is None:
			host = 'http://www.baidu.com/'
		if method is None:
			method = 'GET'
		res = checker(ip_port, host='http://www.baidu.com/', headers=None, method='GET')
		return res
	# 使用帮助
	def print_help(self):
		print(self.usage)
		return self.usage
	# 关于作者
	def print_about(self):
		print(self.author + '\n' + self.info + '\n' + self.version)
		return self.author, self.info
	# 根据类名返回实例化的类
	def __get_api_by_classname(self, classname):
		if classname == 'xici':
			return xici.xici()
		elif classname == '66ip':
			return ip66.ip66()
		elif classname == 'kuaidaili':
			return kuaidaili.kuaidaili()
		elif classname == 'mimiip':
			return mimiip.mimiip()
		elif classname == 'data5u':
			return data5u.data5u()
		elif classname == 'ip3366':
			return ip3366.ip3366()
		elif classname == 'iphai':
			return iphai.iphai()
		elif classname == 'jiangxianli':
			return jiangxianli.jiangxianli()
		else:
			return None
	# 方便查看类
	def __repr__(self):
		return '代理获取类'
	def __str__(self):
		return '代理获取类'


# for test
if __name__ == '__main__':
	print(proxytool().get())