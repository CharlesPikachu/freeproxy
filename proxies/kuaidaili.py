# 作者: Charles
# 公众号: Charles的皮卡丘
# 快代理爬取: https://www.kuaidaili.com
import re
import time
import requests


'''
Function:
	快代理类
Input:
	-page: 抓取的页码
	-proxy_type: 代理类型, 可选项为'all', 'http', 'https'
	-quality: 高(普)代理/普通代理, 可选项为'all', 'anonymous', 'common'
Return:
	-proxyList: 该页所有满足条件的代理列表[(ip, port), (ip, port), ...]
Tips:
	可选项输入错误不raise error, 而是返回空列表, 增强鲁棒性
'''
class kuaidaili():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
						}
		# 高匿和普通(依次)
		self.urls = [
					 'https://www.kuaidaili.com/free/inha/{}/',
					 'https://www.kuaidaili.com/free/intr/{}/'
					 ]
	# 外部调用
	def get(self, page=1, proxy_type='all', quality='all'):
		ip_list = []
		urls = self.__get_urls_by_quality(quality)
		i = 0
		for url in urls:
			res = requests.get(url.format(page), headers=self.headers)
			if (proxy_type == 'http') or (proxy_type == 'https'):
				ip_port_type = re.findall(r'\<td.*?\>(\d+\.\d+.\d+.\d+)\</td\>.*?\>(\d+)\<.*?\>([HTPShtps]+)\<', res.text.replace(' ', '').replace('\n', ''))
				for ipt in ip_port_type:
					if ipt[2].lower() == proxy_type:
						ip_list.append(ipt[:-1])
			elif proxy_type == 'all':
				ip_port = re.findall(r'\<td.*?\>(\d+\.\d+.\d+.\d+)\</td\>.*?\>(\d+)\<', res.text.replace(' ', '').replace('\n', ''))
				ip_list += ip_port
			else:
				continue
			if i == 0:
				time.sleep(0.8)
			i += 1
		return ip_list
	# 根据quality选项获取urls
	def __get_urls_by_quality(self, quality):
		if quality == 'all':
			urls = self.urls
		elif quality == 'anonymous':
			urls = [self.urls[0]]
		elif quality == 'common':
			urls = [self.urls[1]]
		else:
			urls = []
		return urls
	# 方便查看类
	def __repr__(self):
		return '快代理类'
	def __str__(self):
		return '快代理类'


# for test
if __name__ == '__main__':
	print(kuaidaili().get())