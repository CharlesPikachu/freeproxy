'''
Function:
    Implementation of OpenProxyListProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from tqdm import tqdm
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''OpenProxyListProxiedSession'''
class OpenProxyListProxiedSession(BaseProxiedSession):
    source = 'OpenProxyListProxiedSession'
    homepage = 'https://api.openproxylist.xyz/'
    def __init__(self, **kwargs):
        super(OpenProxyListProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, urls = [], requests.Session(), {'socks5': 'https://api.openproxylist.xyz/socks5.txt', 'socks4': 'https://api.openproxylist.xyz/socks4.txt', 'http': 'https://api.openproxylist.xyz/http.txt', 'https': 'https://api.openproxylist.xyz/https.txt'}
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        for protocol, url in urls.items():
            try: (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in resp.text.split('\n'):
                if not (item := item.strip()): continue
                try: ip, port = item.split(':')
                except Exception: continue
                proxy_info = ProxyInfo(source=self.source, protocol=protocol, ip=ip, port=port, anonymity="")
                self.candidate_proxies.append(proxy_info)
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