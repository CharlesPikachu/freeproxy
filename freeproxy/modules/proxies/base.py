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