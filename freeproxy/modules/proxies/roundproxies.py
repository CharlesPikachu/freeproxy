'''
Function:
    Implementation of RoundProxiesProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''RoundProxiesProxiedSession'''
class RoundProxiesProxiedSession(BaseProxiedSession):
    source = 'RoundProxiesProxiedSession'
    homepage = 'https://roundproxies.com/free-proxy-list/'
    def __init__(self, **kwargs):
        super(RoundProxiesProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: (resp := session.get(f"https://roundproxies.com/api/get-free-proxies/?limit=100&page={page}&sort_by=lastChecked&sort_type=desc", headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); data_items = resp.json()['data']
            except Exception: continue
            for item in data_items:
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(item['protocols'][0]).lower(), ip=item['ip'], port=item['port'], anonymity=str(item['anonymityLevel']).lower(), country_code=str(item['country']).upper(), in_chinese_mainland=(str(item['country']).upper() in {'CN'}), delay=item['latency'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies