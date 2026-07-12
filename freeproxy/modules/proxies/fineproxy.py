'''
Function:
    Implementation of FineProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import json
import random
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FineProxyProxiedSession'''
class FineProxyProxiedSession(BaseProxiedSession):
    source = 'FineProxyProxiedSession'
    homepage = 'https://fineproxy.org/cn/free-proxy/'
    def __init__(self, **kwargs):
        super(FineProxyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}
        # obtain proxies
        try: (resp := session.get(self.homepage, headers=self.getrandomheaders(base_headers=headers), timeout=60)).raise_for_status()
        except Exception: return self.candidate_proxies
        proxies: list[dict] = json.loads(BeautifulSoup(resp.text, 'html.parser').find('script', id='fpb-data').text)
        for item in proxies:
            country_code, anonymity = item.get('country', '') or '', {'anon': 'anonymous', 'trans': 'transparent'}.get(item.get('anon', ''), item.get('anon', ''))
            proxy_info = ProxyInfo(source=self.source, protocol=str(random.choice(item['protos'])).lower(), ip=item['ip'], port=item['port'], anonymity=anonymity, delay=item.get('latency'), country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']),)
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies