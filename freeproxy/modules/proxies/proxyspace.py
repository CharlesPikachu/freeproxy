'''
Function:
    Implementation of ProxySpaceProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import ipaddress
from tqdm import tqdm
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''ProxySpaceProxiedSession'''
class ProxySpaceProxiedSession(BaseProxiedSession):
    source = 'ProxySpaceProxiedSession'
    homepage = 'https://proxyspace.pro/'
    def __init__(self, **kwargs):
        super(ProxySpaceProxiedSession, self).__init__(**kwargs)
    '''_extractproxies'''
    def _extractproxies(self, text: str, protocol: str):
        pattern, proxies = re.compile(r'(?P<ip>(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}):(?P<port>\d{1,5})'), []
        for match in pattern.finditer(text or ''):
            try:
                if not ipaddress.ip_address((ip := match.group('ip'))).is_global: continue
                proxies.append(ProxyInfo(source=self.source, protocol=protocol, ip=ip, port=match.group('port'), anonymity=''))
            except Exception: continue
        return proxies
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        urls = {'http': 'https://proxyspace.pro/http.txt', 'https': 'https://proxyspace.pro/https.txt', 'socks4': 'https://proxyspace.pro/socks4.txt', 'socks5': 'https://proxyspace.pro/socks5.txt'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for protocol, url in urls.items():
            try: (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status()
            except Exception: continue
            self.candidate_proxies.extend(self._extractproxies(resp.text, protocol=protocol))
        # append country code info
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_map = {executor.submit(IPLocater.locate, p.ip): p for p in self.candidate_proxies}
            if not self.disable_print: future_map_wrapper = tqdm(as_completed(future_map), desc=f"{self.source} >>> adding country_code")
            else: future_map_wrapper = as_completed(future_map)
            for future in future_map_wrapper:
                try: country_code = future.result(); assert country_code
                except Exception: continue
                proxy_info: ProxyInfo = future_map[future]
                proxy_info.country_code = country_code
                proxy_info.in_chinese_mainland = (country_code.lower() in ['cn'])
        # return
        return self.candidate_proxies