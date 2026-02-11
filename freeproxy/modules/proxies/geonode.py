'''
Function:
    Implementation of GeonodeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''GeonodeProxiedSession'''
class GeonodeProxiedSession(BaseProxiedSession):
    source = 'GeonodeProxiedSession'
    homepage = 'https://geonode.com/free-proxy-list'
    def __init__(self, **kwargs):
        super(GeonodeProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: resp = session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page={page}&sort_by=lastChecked&sort_type=desc", headers=self.getrandomheaders(headers_override=headers)); resp.raise_for_status(); data_items = resp.json()['data']
            except Exception: continue
            for item in data_items:
                try: proxy_info = ProxyInfo(source=self.source, protocol=random.choice(item['protocols']), ip=item['ip'], port=item['port'], anonymity=item['anonymityLevel'], country_code=item['country'], in_chinese_mainland=(item['country'].lower() in ['cn']), delay=item['speed'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies