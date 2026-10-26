'''
Function:
    Implementation of ProxybrosProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxybrosProxiedSession'''
class ProxybrosProxiedSession(BaseProxiedSession):
    source = 'ProxybrosProxiedSession'
    homepage = 'https://proxybros.com/free-proxy-list/'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(ProxybrosProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Origin": "https://proxybros.com", "Referer": "https://proxybros.com/free-proxy-list/", "X-Requested-With": "XMLHttpRequest",
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            params = {"limit": "40", "page": f"{page}"}
            try: (resp := session.get("https://proxybros.com/api/free-proxies/", headers=self.getrandomheaders(base_headers=headers), params=params)).raise_for_status(); data = resp.json(); data_items: list[dict[str, str | int | float | None]] = data['docs']
            except Exception: continue
            for item in data_items:
                try: ip, port = item['endpoint'].rsplit(':', 1); country_code = (item.get('iso') or '').upper(); proxy_info = ProxyInfo(source=self.source, protocol=item['protocol'].lower(), ip=ip, port=int(port), anonymity=item['anonymity'].lower(), country_code=country_code, delay=item['speed'], in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
            if page >= data['totalPages']: break
        # return
        return self.candidate_proxies