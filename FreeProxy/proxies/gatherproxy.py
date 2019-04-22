'''
Function:
	gatherproxy代理爬取(国内无法访问)
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import re
import requests
try:
	from ..utils import *
except:
	from utils import *


'''gatherproxy代理爬取(国内无法访问)'''
class gatherproxy():
	def __init__(self, **kwargs):
		self.info = 'gatherproxy proxy: http://www.gatherproxy.com/zh/'
		self.headers = {
						'Host': 'www.gatherproxy.com',
						'Proxy-Connection': 'keep-alive',
						'Referer': 'http://www.gatherproxy.com/zh/',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
					}
		self.url_list = ['http://www.gatherproxy.com/zh/']
	'''获取代理'''
	def get(self):
		proxies = []
		for url in self.url_list:
			try:
				res = requests.get(url, headers=self.headers)
				proxy = re.findall(r'"PROXY_IP":"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})".*?"PROXY_PORT":"(.*?)"', res.text)
				for each in proxy:
					proxy_format = (each[0], hex2Decimal(each[1]))
					proxies += [proxy_format]
			except:
				pass
		proxies = list(set(proxies))
		return proxies
	'''return info'''
	def __repr__(self):
		return self.info


# for test
if __name__ == '__main__':
	print(gatherproxy().get())