'''
Function:
    Implementation of TrustyTechProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''TrustyTechProxiedSession'''
class TrustyTechProxiedSession(BaseProxiedSession):
    source = 'TrustyTechProxiedSession'
    homepage = 'https://trustytech.io/tools/free-proxy/'
    def __init__(self, **kwargs):
        super(TrustyTechProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            payload = {"countryIds": [], "cityIds": [], "google": "", "type": "", "page": page, "pageSize": 100}
            try: (resp := session.post(f'https://trustytech.io/api/front/proxy/free', headers=self.getrandomheaders(base_headers=headers), json=payload)).raise_for_status()
            except Exception: continue
            for item in resp.json()['content']:
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(item["protocol"]).lower(), ip=item["ip"], port=item["port"], anonymity={'NOTANONYMOUS': 'transparent'}.get(item['anonymity'], 'transparent'), country_code=item["countryIsoCode"], in_chinese_mainland=(item["countryIsoCode"] in {"CN"}), delay=item["delayMS"])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies