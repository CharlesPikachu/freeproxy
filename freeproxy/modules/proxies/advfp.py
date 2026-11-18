'''
Function:
    Implementation of ADVFPProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ADVFPProxiedSession'''
class ADVFPProxiedSession(BaseProxiedSession):
    source = 'ADVFPProxiedSession'
    homepage = 'https://advanced.name/freeproxy'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(ADVFPProxiedSession, self).__init__(**kwargs)
    '''_extractproxies'''
    def _extractproxies(self, data: dict):
        results = []
        for item in data.get('items', []):
            if not isinstance(item, dict): continue
            anon, country_code = item.get('anon', ''), (item.get('country') or '').upper()
            results.append({"ip": item.get('ip'), "port": item.get('port'), "protocols": item.get('proto', []), "anonymity": "anonymous" if anon == "anon" else anon, "country_code": country_code or None, "speed": item.get('ms'), "last_checkup": item.get('checked')})
        return results
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://fp.advanced.name/v1/all/all/{page}.json', headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); items = self._extractproxies(resp.json())
            except Exception: continue
            for item in items:
                try: proxy_info = ProxyInfo(source=self.source, ip=item['ip'], port=item['port'], protocol=random.choice(item['protocols']), delay=item['speed'], anonymity=item['anonymity'], country_code=item['country_code'], in_chinese_mainland=(item['country_code'] in {'CN'}))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        self.candidate_proxies = self.candidate_proxies[:self.max_proxies_per_refresh]
        return self.candidate_proxies