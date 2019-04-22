'''
Function:
	ip3366代理爬取
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import re
import requests


'''ip3366代理爬取'''
class ip3366():
	def __init__(self, **kwargs):
		self.info = 'ip3366 proxy: http://www.ip3366.net/free/'
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
					}
		self.url_list = ['http://www.ip3366.net/free/?stype=1&page=']
		self.page_num = 1
	'''获取代理'''
	def get(self):
		proxies = []
		for url in self.url_list:
			for i in range(1, self.page_num+1):
				try:
					page_url = url + str(i)
					res = requests.get(page_url, headers=self.headers)
					proxy = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?<td>(\d{1,5})</td>', res.text.replace('\n', ''))
					proxies += proxy
				except:
					pass
		proxies = list(set(proxies))
		return proxies
	'''return info'''
	def __repr__(self):
		return self.info


# for test
if __name__ == '__main__':
	print(ip3366().get())