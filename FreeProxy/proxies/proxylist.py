'''
Function:
	proxy-list代理爬取
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import re
import base64
import requests


'''proxy-list代理爬取'''
class proxylist():
	def __init__(self, **kwargs):
		self.info = 'proxylist proxy: https://proxy-list.org/english/index.php'
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
					}
		self.url_list = ['https://proxy-list.org/english/index.php?p=']
		self.page_num = 1
	'''获取代理'''
	def get(self):
		proxies = []
		for url in self.url_list:
			for i in range(1, self.page_num+1):
				try:
					page_url = url + str(i)
					res = requests.get(page_url, headers=self.headers)
					proxy = re.findall(r"Proxy\('(.*?)'\)", res.text)
					for each in proxy:
						p = base64.b64decode(each).decode()
						p = p.split(':')
						proxies += [(p[0], p[1])]
				except:
					pass
		proxies = list(set(proxies))
		return proxies
	'''return info'''
	def __repr__(self):
		return self.info


# for test
if __name__ == '__main__':
	print(proxylist().get())