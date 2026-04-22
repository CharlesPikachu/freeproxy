'''
Function:
    Implementation of ProxyVerityProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import pycountry
import json_repair
from itertools import chain
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
        iter_itemlists_func = (lambda f: lambda obj: f(f, obj))(lambda self, obj: chain([obj] if isinstance(obj, dict) and obj.get("@type") == "ItemList" and "itemListElement" in obj else [], *(self(self, v) for v in obj.values())) if isinstance(obj, dict) else (chain.from_iterable(self(self, x) for x in obj) if isinstance(obj, list) else iter(())))
        parse_ms_func = lambda x: None if not x else (lambda m: float(m.group()) if m else None)(re.search(r"[\d.]+", str(x)))
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://proxyverity.com/free-proxy-list/?proxy_page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for proxies_node in BeautifulSoup(resp.text, "lxml").select('script[type="application/ld+json"]'):
                for itemlist in iter_itemlists_func(json_repair.loads(proxies_node.get_text(strip=True))):
                    for elem in itemlist.get("itemListElement", []):
                        if not elem or not isinstance(elem, dict): continue
                        props = {p.get("name"): p.get("value") for p in (elem.get("item", {}) or {}).get("additionalProperty", []) if isinstance(p, dict)}
                        try: country_code = str(pycountry.countries.lookup(str(props['Country'])).alpha_2).upper()
                        except Exception: country_code = ''
                        try: proxy_info = ProxyInfo(source=self.source, protocol=str(props["Type"]).lower(), ip=props["IP Address"], port=props['Port'], anonymity=str(props['Anonymity']).lower(), country_code=country_code, in_chinese_mainland=(country_code in {"CN"}), delay=parse_ms_func(props["Latency"]))
                        except Exception: continue
                        self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies