'''
Function:
    Implementation of ProxyVerityProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import base64
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyVerityProxiedSession'''
class ProxyVerityProxiedSession(BaseProxiedSession):
    source = 'ProxyVerityProxiedSession'
    homepage = 'https://proxyverity.com/free-proxy-list'
    def __init__(self, **kwargs):
        super(ProxyVerityProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {"host": "proxyverity.com", "referer": "https://proxyverity.com/free-proxy-list/", "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "same-origin", "sec-fetch-user": "?1", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"}
        parse_ms_func = lambda x: None if not x else (lambda m: float(m.group()) if m else None)(re.search(r"[\d.]+", str(x)))
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://proxyverity.com/free-proxy-list/?page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for elem in BeautifulSoup(resp.text, "lxml").select('table tbody tr:not(.pv-decoy)'):
                try:
                    ip, port = base64.b64decode((columns := elem.select('td'))[0].select_one('[data-p]')['data-p']).decode()[::-1].rsplit(':', 1)
                    country_code = columns[2].select_one('img[src*="/flags/"]')['src'].rsplit('/', 1)[-1].split('.', 1)[0].upper()
                    proxy_info = ProxyInfo(source=self.source, protocol=columns[1].get_text(strip=True).lower(), ip=ip, port=int(port), anonymity=columns[3].get_text(strip=True).lower(), country_code=country_code, in_chinese_mainland=(country_code in {"CN"}), delay=parse_ms_func(columns[6].get_text(strip=True)),)
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies