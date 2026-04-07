'''
Function:
    Implementation of ProxiwareProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxiwareProxiedSession'''
class ProxiwareProxiedSession(BaseProxiedSession):
    source = 'ProxiwareProxiedSession'
    homepage = 'https://proxiware.com/free-proxy-list'
    def __init__(self, **kwargs):
        super(ProxiwareProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://papi.proxiware.com/proxies?page={page}&country=&protocol=&anonymity=&speed=', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in resp.json()['proxies']:
                try: proxy_info = ProxyInfo(source=self.source, protocol=item["protocol"], ip=item["addr"], port=item["port"], anonymity=str(item["anonymity"]).lower(), country_code=item["country_code"], in_chinese_mainland=(item["country_code"] in {"CN"}), delay=item["speed_ms"])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies