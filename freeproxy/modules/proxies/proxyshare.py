'''
Function:
    Implementation of ProxyShareProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyShareProxiedSession'''
class ProxyShareProxiedSession(BaseProxiedSession):
    source = 'ProxyShareProxiedSession'
    homepage = 'https://www.proxyshare.com/zh/free-proxy/'
    def __init__(self, **kwargs):
        super(ProxyShareProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session(); protocal_mapper = {'1': 'http', '2': 'https', '4': 'socks4', '8': 'socks5'}
        anonymity_mapper = {'0': 'transparent', '1': 'anonymous', '2': 'elite'}
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: (resp := session.get(f"https://www.proxyshare.com/web_v1/free-proxy/list?&page={page}&sort_by=lastChecked&sort_type=desc&page_size=1000", headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); data_items = resp.json()['data']['list']
            except Exception: continue
            for item in data_items:
                try: proxy_info = ProxyInfo(source=self.source, protocol=protocal_mapper[str(item['protocol'])], ip=item['ip'], port=item['port'], anonymity=anonymity_mapper[str(item['anonymity'])], country_code=item['country_code'], in_chinese_mainland=(str(item['country_code']).lower() in ['cn']), delay=item['latency'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies