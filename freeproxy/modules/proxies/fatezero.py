'''
Function:
    fatezero代理
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import json
import requests
from .base import BaseProxy


'''fatezero代理'''
class FatezeroProxy(BaseProxy):
    def __init__(self, **kwargs):
        super(FatezeroProxy, self).__init__(**kwargs)
        self.http_proxies = []
        self.https_proxies = []
        self.http_https_proxies = []
    '''刷新代理'''
    def refreshproxies(self):
        # 初始化
        self.http_proxies = []
        self.https_proxies = []
        proxies_format = '{ip}:{port}'
        # 获得代理
        url = 'http://proxylist.fatezero.org/proxy.list'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url, headers=headers, verify=False)
        for item in response.text.split('\n'):
            if not item.strip(): continue
            item = json.loads(item)
            ip = item['host']
            port = item['port']
            proxy_type = item['type']
            if proxy_type.lower() == 'http':
                self.http_proxies.append({'http': proxies_format.format(ip=ip, port=port)})
            else:
                self.https_proxies.append({'https': proxies_format.format(ip=ip, port=port)})
        self.http_https_proxies = self.http_proxies.copy() + self.https_proxies.copy()
        # 返回
        return self.http_proxies, self.https_proxies, self.http_https_proxies