'''
Function:
	some utils.
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import re
import requests


'''
Function:
	代理有效性验证
Class method:
	checkResponse:
		Input:
			--ip_port: ip和port, 格式为(ip, port)
			--host: 验证主机
			--headers: 验证时的请求头
			--method: 请求类型(GET/POST)
			--timeout: 最大延迟
			--post_data: POST验证时提交的data
			--proxy_type: http/https, 代理类型
		Return:
			--is_valid(bool): True(有效)/False(无效)
	checkFormat:
		Input:
			--ip_port: ip和port, 格式为(ip, port)
		Return:
			--is_valid(bool): True(有效)/False(无效)
	check:
		checkResponse && checkFormat
'''
class ProxyChecker():
	def __init__(self, **kwargs):
		self.info = 'ProxyChecker'
	'''代理有效性检验'''
	def check(self, ip_port, host='http://www.baidu.com/', headers=None, method='GET', timeout=0.5, post_data={}, proxy_type='http'):
		return self.checkFormat(ip_port) and self.checkResponse(ip_port, host, headers, method, timeout, post_data, proxy_type)
	'''检查代理格式'''
	def checkFormat(self, ip_port):
		proxy = ip_port[0] + ':' + ip_port[1]
		verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
		result = re.findall(verify_regex, proxy)
		if len(result) == 1 and result[0] == proxy:
			return True
		return False
	'''检查响应情况'''
	def checkResponse(self, ip_port, host='http://www.baidu.com/', headers=None, method='GET', timeout=0.5, post_data={}, proxy_type='http'):
		if headers is None:
			headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
						}
		try:
			if proxy_type == 'http':
				proxy = {'http': 'http://%s:%s' % ip_port}
			else:
				proxy = {'https': 'https://%s:%s' % ip_port}
			if method == 'GET':
				res = requests.get(host, headers=headers, proxies=proxy, timeout=timeout)
			else:
				res = requests.post(host, headers=headers, data=post_data)
			if res.status_code != 200:
				raise RuntimeError('requests error...')
			return True
		except:
			return False
	'''return info'''
	def __repr__(self):
		return self.info


'''16进制转10进制'''
def hex2Decimal(string):
	string = list(string.upper())
	string.reverse()
	map_dict = {
				'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
				'9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
				}
	number = 0
	for i, s in enumerate(string):
		number += (16 ** i) * map_dict[s]
	return str(number)