'''
Function:
    Implementation of IPRoyalProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
import pycountry
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''IPRoyalProxiedSession'''
class IPRoyalProxiedSession(BaseProxiedSession):
    source = 'IPRoyalProxiedSession'
    homepage = 'https://iproyal.com/free-proxy-list/'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(IPRoyalProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
        headers.update({'Origin': 'https://iproyal.com', 'Referer': self.homepage, 'Accept': 'application/json'})
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try:
                (resp := session.post('https://iproyal.com/_actions/getFreeProxyList/', headers=self.getrandomheaders(base_headers=headers), json={'page': page}, timeout=60)).raise_for_status()
                data = resp.json(); data_items = [{k: data[v] if v >= 0 else None for k, v in data[i].items()} for i in data[data[0]['records']]]
            except Exception: continue
            for item in data_items:
                if not isinstance(item, dict): continue
                try: country_code = str(pycountry.countries.lookup(str(item['country'])).alpha_2)
                except Exception: country_code = ''
                try: proxy_info = ProxyInfo(source=self.source, ip=item['ip'], port=item['port'], protocol=item['protocol'], delay=None, anonymity="", country_code=country_code.upper(), in_chinese_mainland=(country_code.lower() in {'cn'}))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        self.candidate_proxies = self.candidate_proxies[:self.max_proxies_per_refresh]
        return self.candidate_proxies