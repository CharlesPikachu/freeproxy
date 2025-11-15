'''
Function:
    Implementation of ProxylistProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''ProxylistProxiedSession'''
class ProxylistProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxylistProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        base_url = 'https://www.proxy-list.download/api/v1/get?type='
        for protocol in ['http', 'https', 'socks4', 'socks5']:
            resp = requests.get(base_url+protocol, headers=self.randomheaders())
            if resp.status_code != 200: continue
            for ip_port in resp.text.strip().split('\n'):
                self.candidate_proxies.append({'http': f'{protocol}://{ip_port.strip()}', 'https': f'{protocol}://{ip_port.strip()}'})
        # return
        return self.candidate_proxies