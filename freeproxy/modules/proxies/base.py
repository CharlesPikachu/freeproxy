'''
Function:
    代理基类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import requests


'''代理基类'''
class BaseProxy(requests.Session):
    def __init__(self, **kwargs):
        super(BaseProxy, self).__init__(**kwargs)
    '''刷新代理'''
    def refreshproxies(self):
        raise NotImplementedError('not to be implemented')
    '''设置代理'''
    def setproxy(self, proxy_type='all'):
        if proxy_type == 'all':
            if len(self.http_https_proxies) < 1: self.refreshproxies()
            idx = random.randint(0, len(self.http_https_proxies)-1)
            self.proxies = self.http_https_proxies.pop(idx)
        elif proxy_type == 'http':
            if len(self.http_proxies) < 1: self.refreshproxies()
            idx = random.randint(0, len(self.http_proxies)-1)
            self.proxies = self.http_proxies.pop(idx)
        elif proxy_type == 'https':
            if len(self.https_proxies) < 1: self.refreshproxies()
            idx = random.randint(0, len(self.https_proxies)-1)
            self.proxies = self.https_proxies.pop(idx)
        return self.proxies