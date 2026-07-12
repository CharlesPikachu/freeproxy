'''
Function:
    Implementation of ChillyProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ChillyProxyProxiedSession'''
class ChillyProxyProxiedSession(BaseProxiedSession):
    source = 'ChillyProxyProxiedSession'
    homepage = 'https://chillyproxy.com/tool-free-proxy-list'
    def __init__(self, **kwargs):
        super(ChillyProxyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, limit = [], requests.Session(), 50
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36', 'Referer': self.homepage}
        # obtain proxies
        try: (resp := session.get(f"https://chillyproxy.com/api/tools/free-proxies/details?protocol=all&country=ALL&limit={limit}", headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status()
        except Exception: return self.candidate_proxies
        for item in resp.json()['data']['proxies']:
            if not isinstance(item, dict): continue
            proxy_info = ProxyInfo(source=self.source, ip=str(item['ip']).strip(), port=str(item['port']).strip(), protocol=str(item['protocol']).strip(), delay=float(item.get('latency_ms', 0) or 0), anonymity=item.get('anonymity'), country_code=item.get('country'), in_chinese_mainland=(str(item.get('country')).lower() in {'cn'}))
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies