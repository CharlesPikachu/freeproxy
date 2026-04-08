'''
Function:
    Implementation of PubProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''PubProxyProxiedSession'''
class PubProxyProxiedSession(BaseProxiedSession):
    source = 'PubProxyProxiedSession'
    homepage = 'http://pubproxy.com/'
    def __init__(self, **kwargs):
        super(PubProxyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'http://pubproxy.com/api/proxy?limit=100&format=json&page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in resp.json()['data']:
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(item["type"]).lower(), ip=item["ip"], port=item["port"], anonymity=item['proxy_level'], country_code=item["country"], in_chinese_mainland=(item["country"] in {"CN"}), delay=float(item["speed"]))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies