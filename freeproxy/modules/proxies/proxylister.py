'''
Function:
    Implementation of ProxyListerProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyListerProxiedSession'''
class ProxyListerProxiedSession(BaseProxiedSession):
    source = 'ProxyListerProxiedSession'
    homepage = 'https://proxylister.com/free-proxies'
    def __init__(self, **kwargs):
        super(ProxyListerProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            params = {'limit': 500, 'page': page, 'sort': '-last_checked_at'}
            try: (resp := session.get('https://proxylister.com/api/v1/proxies', params=params, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status(); data_items: list[dict] = (resp.json() or {}).get('results') or []
            except Exception: continue
            for item in data_items:
                location, metrics, protocols = item.get('location') or {}, item.get('metrics') or {}, item.get('protocols') or []
                protocols, country_code = [protocols] if isinstance(protocols, str) else protocols, (location.get('country_code') or '').upper()
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(random.choice(protocols)).lower(), ip=item['ip_address'], port=str(item['port']), country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']), anonymity=item.get('anonymity'), delay=metrics.get('latency_ms'))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
            if len(data_items) < params['limit']: break
        # return
        return self.candidate_proxies