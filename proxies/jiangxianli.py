# 作者: Charles
# 公众号: Charles的皮卡丘
# 免费代理IP库代理爬取: http://ip.jiangxianli.com/?page=1
import re
import requests


'''
Function:
	免费代理IP库代理类
Input:
	-page: 抓取的页码
	-proxy_type: 代理类型, 可选项为'all', 'http', 'https'
	-quality: 高(普)匿代理/普通代理, 可选项为'all', 'anonymous', 'common'
Return:
	-proxyList: 该页所有满足条件的代理列表[(ip, port), (ip, port), ...]
Tips:
	可选项输入错误不raise error, 而是返回空列表, 增强鲁棒性
'''
class jiangxianli():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
						}
		self.urls = [
					 'http://ip.jiangxianli.com/?page='
					 ]
	# 外部调用
	def get(self, page=1, proxy_type='all', quality='all'):
		ip_list = []
		for url in self.urls:
			res = requests.get(url, headers=self.headers)
			if proxy_type == 'all' and quality == 'all':
				ip_port = re.findall(r'\<td\>(\d+\.\d+.\d+.\d+)\</td\>.*?\<td\>(\d+)\</td\>', res.text.replace(' ', '').replace('\n', ''))
				ip_list += ip_port
			elif quality == 'all':
				ip_port_quality_type = re.findall(r'\<td\>(\d+\.\d+.\d+.\d+)\</td\>.*?\<td\>(\d+)\</td\>.*?\<td\>(\w+)\</td\>.*?\<td\>([HTPShtps]+)\</td\>', res.text.replace(' ', '').replace('\n', ''))
				for ipqt in ip_port_quality_type:
					if ipqt[-1].lower() == proxy_type:
						ip_list.append(ipqt[:-2])
			elif quality == 'anonymous':
				ip_port_quality_type = re.findall(r'\<td\>(\d+\.\d+.\d+.\d+)\</td\>.*?\<td\>(\d+)\</td\>.*?\<td\>(\w+)\</td\>.*?\<td\>([HTPShtps]+)\</td\>', res.text.replace(' ', '').replace('\n', ''))
				for ipqt in ip_port_quality_type:
					if proxy_type != 'all':
						if ipqt[-1].lower() == proxy_type:
							if '匿' in ipqt[2]:
								ip_list.append(ipqt[:-2])
					else:
						if '匿' in ipqt[2]:
							ip_list.append(ipqt[:-2])
			elif quality == 'common':
				ip_port_quality_type = re.findall(r'\<td\>(\d+\.\d+.\d+.\d+)\</td\>.*?\<td\>(\d+)\</td\>.*?\<td\>(\w+)\</td\>.*?\<td\>([HTPShtps]+)\</td\>', res.text.replace(' ', '').replace('\n', ''))
				for ipqt in ip_port_quality_type:
					if proxy_type != 'all':
						if ipqt[-1].lower() == proxy_type:
							if '匿' not in ipqt[2]:
								ip_list.append(ipqt[:-2])
					else:
						if '匿' not in ipqt[2]:
							ip_list.append(ipqt[:-2])
			else:
				continue
		return ip_list
	# 方便查看类
	def __repr__(self):
		return '免费代理IP库代理类'
	def __str__(self):
		return '免费代理IP库代理类'


# for test
if __name__ == '__main__':
	print(jiangxianli().get())