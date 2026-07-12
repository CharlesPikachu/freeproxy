'''
Function:
    Implementation of ProxyEliteProxiedSession
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


'''ProxyEliteProxiedSession'''
class ProxyEliteProxiedSession(BaseProxiedSession):
    source = 'ProxyEliteProxiedSession'
    homepage = 'https://proxyelite.info/cn/free/asia/china/'
    def __init__(self, **kwargs):
        super(ProxyEliteProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        # obtain proxies
        try: (resp := session.get(self.homepage, headers=self.getrandomheaders(base_headers=headers), timeout=60)).raise_for_status()
        except Exception: return self.candidate_proxies
        for item in json.loads(BeautifulSoup(resp.text, 'html.parser').find('script', id='fpb-data').text):
            if not isinstance(item, dict) or not (protocols := [str(protocol).lower() for protocol in item.get('protos', []) if str(protocol).lower() in ('http', 'https', 'socks4', 'socks5')]): continue
            anonymity = {'anon': 'anonymous', 'trans': 'transparent'}.get((item.get('anon', '') or '').lower(), (item.get('anon', 'transparent') or '').lower())
            proxy_info = ProxyInfo(source=self.source, ip=str(item['ip']).strip(), port=str(item['port']).strip(), protocol=random.choice(protocols), delay=int(item.get('latency', 0)), anonymity=anonymity, country_code='CN', in_chinese_mainland=True)
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies