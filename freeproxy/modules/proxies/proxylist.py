'''
Function:
    Implementation of ProxylistProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxylistProxiedSession'''
class ProxylistProxiedSession(BaseProxiedSession):
    source = 'ProxylistProxiedSession'
    homepage = 'https://www.proxy-list.download/HTTP/'
    def __init__(self, **kwargs):
        super(ProxylistProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Referer": "https://www.proxy-list.download/SOCKS5", "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"', "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"', "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        base_url = 'https://www.proxy-list.download/api/v2/get?l=en&t='
        for protocol in ['http', 'https', 'socks4', 'socks5']:
            headers['Referer'] = f"https://www.proxy-list.download/{protocol.upper()}"
            try: (resp := session.get(f'{base_url}{protocol}', headers=self.getrandomheaders(headers_override=headers))).raise_for_status(); data_items = resp.json()['LISTA']
            except Exception: continue
            for item in data_items:
                try: proxy_info = ProxyInfo(source=self.source, protocol=protocol, ip=item["IP"], port=item["PORT"], anonymity=item["ANON"].lower(), country_code=item["ISO"], in_chinese_mainland=(item["ISO"].lower() in ['cn']), delay=item["PING"])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies