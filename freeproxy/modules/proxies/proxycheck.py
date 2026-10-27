'''
Function:
    Implementation of ProxyCheckProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from urllib.parse import urlsplit
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyCheckProxiedSession'''
class ProxyCheckProxiedSession(BaseProxiedSession):
    source = 'ProxyCheckProxiedSession'
    homepage = 'https://proxycheck.app/free-proxies'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(ProxyCheckProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'accept': 'application/json', 'referer': 'https://proxycheck.app/free-proxies', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try:
                (resp := session.get('https://proxycheck.app/api/v1/public-proxies', params={'page': page, 'limit': 200}, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status()
                data: dict = resp.json(); data_items: list[dict] = data['items']
            except Exception: continue
            for item in data_items:
                try:
                    parsed, country_code = urlsplit(str(item['proxy_norm'])), str(item.get('country') or '').upper()
                    proxy_info = ProxyInfo(source=self.source, protocol=str(item['protocol']).lower(), ip=parsed.hostname, port=parsed.port, anonymity=str(item.get('anonymity') or '').lower(), delay=item.get('ttfb_ms'), country_code=country_code, in_chinese_mainland=(country_code == 'CN'))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
            if not data_items or page * 200 >= int(data.get('total', 0)): break
        # return
        return self.candidate_proxies