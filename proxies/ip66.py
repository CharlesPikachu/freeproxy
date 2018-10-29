# 作者: Charles
# 公众号: Charles的皮卡丘
# 66ip代理爬取: http://www.66ip.cn/
import re
import random
import requests


'''
Function:
	66ip代理类
Input:
	-page: 抓取的页码
	-area: 代理的地区, 为None时随机选择一个地区
	-proxy_type(Invalid here): 代理类型, 可选项为'all', 'http', 'https'
	-quality: 高(普)代理/普通代理, 可选项为'all', 'anonymous', 'common'
Return:
	-proxyList: 该页所有满足条件的代理列表[(ip, port), (ip, port), ...]
Tips:
	可选项输入错误不raise error, 而是返回空列表, 增强鲁棒性
'''
class ip66():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
						}
		self.urls = [
					 'http://www.66ip.cn/areaindex_{}/{}.html'
					 ]
	# 外部调用
	def get(self, page=1, area=None, proxy_type='all', quality='all'):
		if proxy_type != 'all':
			print('[Error]: 66ip代理类<proxy_type>参数不支持非<all>选项.')
			return []
		if area is None:
			area = random.randint(1, 34)
		area = 34 if area > 34 else area
		urls = self.urls
		ip_list = []
		for url in urls:
			res = requests.get(url.format(area, page), headers=self.headers)
			res.encoding = 'gbk'
			ip_port_quality = re.findall(r'<td>(\d+\.\d+.\d+.\d+)</td>.*?<td>(\d+)</td><td>.*?</td>.*?<td>(.*?)</td>', res.text.replace(' ', '').replace('\n', ''))
			for ipq in ip_port_quality:
				if quality == 'anonymous':
					if ipq[-1] == '高匿代理':
						ip_list.append(ipq[:-1])
				elif quality == 'common':
					if ipq[-1] != '高匿代理':
						ip_list.append(ipq[:-1])
				elif quality == 'all':
					ip_list.append(ipq[:-1])
				else:
					continue
		return ip_list
	# 方便查看类
	def __repr__(self):
		return '66ip代理类'
	def __str__(self):
		return '66ip代理类'


# for test
if __name__ == '__main__':
	print(ip66().get())