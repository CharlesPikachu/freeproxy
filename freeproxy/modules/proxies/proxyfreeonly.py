'''
Function:
    Implementation of ProxyFreeOnlyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyFreeOnlyProxiedSession'''
class ProxyFreeOnlyProxiedSession(BaseProxiedSession):
    source = 'ProxyFreeOnlyProxiedSession'
    homepage = 'https://proxyfreeonly.com/free-proxy-list#google_vignette'
    def __init__(self, **kwargs):
        super(ProxyFreeOnlyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://proxyfreeonly.com/api/free-proxy-list?limit=500&page={page}&sortBy=lastChecked&sortType=desc', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in resp.json():
                try: proxy_info = ProxyInfo(source=self.source, protocol=item["protocols"][0], ip=item["ip"], port=item["port"], anonymity=str(item["anonymityLevel"]).lower(), country_code=item["country"], in_chinese_mainland=(item["country"] in {"CN"}), delay=item["latency"])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies