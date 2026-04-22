'''
Function:
    Implementation of GeonixProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
import pycountry
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''GeonixProxiedSession'''
class GeonixProxiedSession(BaseProxiedSession):
    source = 'GeonixProxiedSession'
    homepage = 'https://free.geonix.com'
    def __init__(self, **kwargs):
        super(GeonixProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36", "accept": "application/json, text/plain, */*", "origin": "https://free.geonix.com", "referer": "https://free.geonix.com"}
        (resp := session.get("https://free.geonix.com/api/front/main/captcha/info", headers=(headers := self.getrandomheaders(base_headers=headers)))).raise_for_status()
        # obtain proxies
        payload = {"captchaKey": dict(resp.json()).get("captchaKey", "") or "", "countries": [], "proxyProtocols": [], "proxyTypes": []}
        (resp := session.post("https://free.geonix.com/api/front/main/proxy/export", json=payload, timeout=20)).raise_for_status()
        ip_port_mapper = {ip: int(port) for ip, port in (str(x).rsplit(":", 1) for x in resp.json()[::-1])}
        for page in range(0, self.max_pages):
            payload = {"page": page, "size": 100, "countries": [], "proxyProtocols": [], "proxyTypes": []}
            try: (resp := session.post(f'https://free.geonix.com/api/front/main/pagination/filtration', headers=self.getrandomheaders(base_headers=headers), json=payload)).raise_for_status()
            except Exception: continue
            for item in resp.json()['content']:
                try: country_code = str(pycountry.countries.lookup(str(item['country'])).alpha_2).upper()
                except Exception: country_code = ''
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(item["proxyType"]).lower(), ip=item["ip"], port=ip_port_mapper[item["ip"]], anonymity={'el-elit.txt': 'elite', 'an-anonim.txt': 'anonymous', 'pr-proz.txt': 'transparent'}.get(item['anonymity'], 'transparent'), country_code=country_code, in_chinese_mainland=(country_code in {"CN"}), delay=float(item["delay"]))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies