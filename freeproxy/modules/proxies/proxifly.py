'''
Function:
    Implementation of ProxiflyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxiflyProxiedSession'''
class ProxiflyProxiedSession(BaseProxiedSession):
    source = 'ProxiflyProxiedSession'
    homepage = 'https://proxifly.dev/'
    def __init__(self, **kwargs):
        super(ProxiflyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        urls = ['https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.json']
        country_codes = [
            "AE", "AM", "AO", "AR", "AT", "AU", "BA", "BD", "BE", "BR", "BY", "CA", "CH", "CL", "CM", "CN", "CO", "CR", "CY", "CZ",
            "DE", "DK", "DO", "EC", "EE", "EG", "ES", "FI", "FR", "GB", "GE", "GR", "GT", "HK", "HN", "HU", "ID", "IN", "IQ", "IR",
            "IT", "JP", "KE", "KH", "KR", "KZ", "LA", "LS", "LU", "LV", "LY", "MK", "MX", "MY", "MZ", "NG", "NL", "NO", "NP", "PE",
            "PH", "PK", "PL", "PR", "PY", "RO", "RU", "RW", "SC", "SE", "SG", "SK", "SN", "SY", "TH", "TL", "TV", "TW", "TZ", "UA",
            "US", "VE", "VN", "YE", "ZA", "ZZ",
        ]
        for country_code in country_codes: urls.append(f'https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/{country_code}/data.json')
        # obtain proxies
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        def _fetchonecountry(url: str):
            try:
                session = requests.Session()
                resp = session.get(url, headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
                proxies_data = resp.json()
            except:
                return
            for item in proxies_data:
                try:
                    proxy_info = ProxyInfo(
                        source=self.source, protocol=item['protocol'], ip=item['ip'], port=item['port'], anonymity=item['anonymity'], 
                        country_code=item['geolocation']['country'], in_chinese_mainland=(item['geolocation']['country'].lower() in ['cn']),
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(_fetchonecountry, url) for url in urls]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    continue
        # return
        return self.candidate_proxies