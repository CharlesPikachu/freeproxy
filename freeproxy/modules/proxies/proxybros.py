'''
Function:
    Implementation of ProxybrosProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
import pycountry
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxybrosProxiedSession'''
class ProxybrosProxiedSession(BaseProxiedSession):
    source = 'ProxybrosProxiedSession'
    homepage = 'https://proxybros.com/free-proxy-list/'
    def __init__(self, **kwargs):
        super(ProxybrosProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Origin": "https://proxybros.com", "Referer": "https://proxybros.com/free-proxy-list/", "X-Requested-With": "XMLHttpRequest",
        }
        anonymity_mapper = {"high": "elite", "average": "anonymous", "low": "transparent"}
        # obtain proxies
        data = {"action": "nrproxyexport", "type": "2", "lang": "en", "path": "/free-proxy-list/"}
        (resp := session.post("https://proxybros.com/wp-admin/admin-ajax.php", headers=headers, data=data)).raise_for_status()
        (resp := session.get(resp.json()["href"], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36", "Referer": "https://proxybros.com/free-proxy-list/"})).raise_for_status()
        for item in resp.json():
            try: country_code = str(pycountry.countries.lookup(item['Country']).alpha_2).upper()
            except Exception: country_code = ''
            try: proxy_info = ProxyInfo(source=self.source, protocol=str(item['Type']).lower(), ip=item['IP_Address'], port=item['Port'], anonymity=anonymity_mapper.get(item['Anonymity'], 'transparent'), country_code=country_code, delay=float(item['Delay']), in_chinese_mainland=(country_code.lower() in ['cn']))
            except Exception: continue
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies