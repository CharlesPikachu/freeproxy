'''
Function:
    Implementation of FreeProxyDBProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FreeProxyDBProxiedSession'''
class FreeProxyDBProxiedSession(BaseProxiedSession):
    source = 'FreeProxyDBProxiedSession'
    homepage = 'https://freeproxydb.com/'
    def __init__(self, **kwargs):
        super(FreeProxyDBProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try:
                resp = session.get(f"https://freeproxydb.com/api/proxy/search?country=&protocol=&anonymity=&speed=0,60&https=&page_index={page}&page_size=100", headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
                data_items = resp.json()['data']['data']
            except:
                continue
            for item in data_items:
                try:
                    proxy_info = ProxyInfo(
                        source=self.source, protocol=item['site_protocol'], ip=item['ip'], port=item['port'], anonymity=item['anonymity'], 
                        country_code=item['country'], in_chinese_mainland=(item['country'].lower() in ['cn']), delay=int(item['speed'] * 1000),
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies