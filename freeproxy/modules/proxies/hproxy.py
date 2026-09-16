'''
Function:
    Implementation of TrustyTechProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''HProxyProxiedSession'''
class HProxyProxiedSession(BaseProxiedSession):
    source = 'HProxyProxiedSession'
    homepage = 'https://hproxy.com/free-proxy-list'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(HProxyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://hproxy.com/api/proxy-list?format=json&limit=500&offset={(page-1)*500}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in resp.json():
                try: proxy_info = ProxyInfo(source=self.source, protocol=item["protocols"][0], ip=item["ip"], port=item["port"], anonymity=str(item["anonymity"]).lower(), country_code=item["country_code"], in_chinese_mainland=(item["country_code"] in {"CN"}), delay=item["latency_ms"])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies