'''
Function:
    Implementation of ProxyScrapeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyScrapeProxiedSession'''
class ProxyScrapeProxiedSession(BaseProxiedSession):
    source = 'ProxyScrapeProxiedSession'
    homepage = 'https://proxyscrape.com/free-proxy-list'
    def __init__(self, **kwargs):
        super(ProxyScrapeProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        for page in range(self.max_pages):
            try: (resp := session.get(f"https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&skip={page * 1000}&proxy_format=protocolipport&format=json&limit=1000", headers=self.getrandomheaders(headers_override=headers))).raise_for_status(); data_items: list[dict] = resp.json()['proxies']
            except Exception: continue
            for item in data_items:
                if not item.get('alive'): continue
                try: proxy_info = ProxyInfo(source=self.source, protocol=item['protocol'], ip=item['ip'], port=item['port'], anonymity=item['anonymity'], country_code=item['ip_data']['countryCode'], in_chinese_mainland=(item['ip_data']['countryCode'].lower() in ['cn']), delay=item['timeout'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies