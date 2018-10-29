# 作者: Charles
# 公众号: Charles的皮卡丘
# 工具函数
from http.client import HTTPConnection


'''
Function:
	代理有效性验证
Input:
	ip_port: ip和port, 格式为(ip, port)
	host: 验证主机
	headers: 验证时的请求头
	method: 请求类型(GET/POST)
Return:
	is_valid(bool): True(有效)/False(无效)
'''
def checker(ip_port, host='http://www.baidu.com/', headers=None, method='GET'):
	if headers is None:
		headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
					}
	try:
		conn = HTTPConnection(ip_port[0], ip_port[1], timeout=5.0)
		conn.request(method=method, url=host, headers=headers)
		res = conn.getresponse()
		return True
	except:
		return False
