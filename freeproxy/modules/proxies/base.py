'''
Function:
    Implementation of BaseProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
import ipaddress
from fake_useragent import UserAgent


'''BaseProxiedSession'''
class BaseProxiedSession(requests.Session):
    def __init__(self, max_pages=1, **kwargs):
        super(BaseProxiedSession, self).__init__(**kwargs)
        self.max_pages = max_pages
        self.candidate_proxies = []
    '''refreshproxies'''
    def refreshproxies(self):
        raise NotImplementedError('not to be implemented')
    '''getrandomproxy'''
    def getrandomproxy(self):
        if len(self.candidate_proxies) < 1: self.refreshproxies()
        idx = random.randint(0, len(self.candidate_proxies)-1)
        return self.candidate_proxies.pop(idx)
    '''setrandomproxy'''
    def randomsetproxy(self):
        self.proxies = self.getrandomproxy()
        return self.proxies
    '''randomheaders'''
    def randomheaders(self, headers_override: dict = {}):
        # random public ipv4
        while True:
            ip_str = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip = ipaddress.ip_address(ip_str)
            if ip.is_global: break
        # construct default headers
        default_headers = {
            'X-Forwarded-For': ip_str, 'User-Agent': UserAgent().random, 
        }
        default_headers.update(headers_override)
        # return
        return default_headers