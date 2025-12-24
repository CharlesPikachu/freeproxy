'''
Function:
    Implementation of IPLocateProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from tqdm import tqdm
from urllib.parse import urlparse
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''IPLocateProxiedSession'''
class IPLocateProxiedSession(BaseProxiedSession):
    source = 'IPLocateProxiedSession'
    homepage = 'https://www.iplocate.io/'
    def __init__(self, **kwargs):
        super(IPLocateProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        urls = {
            'https://raw.githubusercontent.com/iplocate/free-proxy-list/refs/heads/main/all-proxies.txt',
        }
        headers = {
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for url in urls:
            try:
                resp = session.get(url, headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
            except:
                continue
            for item in resp.text.split('\n'):
                item = item.strip()
                if not item: continue
                parse_item = urlparse(item)
                proxy_info = ProxyInfo(
                    source=self.source, protocol=parse_item.scheme, ip=parse_item.hostname, port=parse_item.port, anonymity="", 
                )
                self.candidate_proxies.append(proxy_info)
        # append country code info
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_map = {
                executor.submit(IPLocater.locate, p.ip): p for p in self.candidate_proxies
            }
            if not self.disable_print: future_map_wrapper = tqdm(as_completed(future_map), desc=f"{self.source} >>> adding country_code")
            else: future_map_wrapper = as_completed(future_map)
            for future in future_map_wrapper:
                try:
                    country_code = future.result()
                    assert country_code
                except Exception:
                    continue
                proxy_info: ProxyInfo = future_map[future]
                proxy_info.country_code = country_code
                proxy_info.in_chinese_mainland = (country_code.lower() in ['cn'])
        # return
        return self.candidate_proxies