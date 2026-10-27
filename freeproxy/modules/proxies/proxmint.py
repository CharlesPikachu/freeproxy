'''
Function:
    Implementation of ProxmintProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxmintProxiedSession'''
class ProxmintProxiedSession(BaseProxiedSession):
    source = 'ProxmintProxiedSession'
    homepage = 'https://proxmint.com/free-proxies'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(ProxmintProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'referer': self.homepage, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: (resp := session.get('https://proxmint.com/api/free-proxies', params={'page': page, 'pageSize': 200, 'sort': 'score'}, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status(); data: dict = resp.json()
            except Exception: continue
            for item in (data.get('rows', []) or []):
                if not isinstance(item, dict): continue
                try:
                    ip, port, protocol = str(item['ip']), str(item['port']), str(item.get('protocol') or '').lower()
                    country_code, anonymity = str(item.get('countryCode') or '').upper(), str(item.get('anonymity') or '').lower()
                    proxy_info = ProxyInfo(source=self.source, protocol=protocol, ip=ip, port=port, country_code=country_code, in_chinese_mainland=country_code.lower() in {'cn'}, anonymity=anonymity, delay=item.get('latencyMs'))
                    self.candidate_proxies.append(proxy_info)
                except (KeyError, ValueError, TypeError): continue
            if page * 200 >= data.get('total', 0): break
        # return
        return self.candidate_proxies