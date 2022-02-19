'''
Function:
    IP89代理
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import requests
from .base import BaseProxy


'''IP89代理'''
class IP89Proxy(BaseProxy):
    def __init__(self, **kwargs):
        super(IP89Proxy, self).__init__(**kwargs)
        self.http_proxies = []
        self.https_proxies = []
        self.http_https_proxies = []
    '''刷新代理'''
    def refreshproxies(self):
        # 初始化
        self.http_proxies = []
        self.https_proxies = []
        # 获得代理
        url = 'http://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url, headers=headers, verify=False)
        for item in response.text.split('<br>'):
            if len(item.split(':')) != 2: continue
            if len(item.split('.')) != 4: continue
            if '>' in item or '<' in item: continue
            proxy_type = random.choice(['http', 'https'])
            if proxy_type.lower() == 'http':
                self.http_proxies.append({'http': item})
            else:
                self.https_proxies.append({'https': item})
        self.http_https_proxies = self.http_proxies.copy() + self.https_proxies.copy()
        # 返回
        return self.http_proxies, self.https_proxies, self.http_https_proxies