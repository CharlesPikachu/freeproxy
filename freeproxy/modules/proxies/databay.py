'''
Function:
    Implementation of DatabayProxiedSession
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


'''DatabayProxiedSession'''
class DatabayProxiedSession(BaseProxiedSession):
    source = 'DatabayProxiedSession'
    homepage = 'https://databay.com/free-proxy-list'
    def __init__(self, **kwargs):
        super(DatabayProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        urls = [
            'https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/socks5.txt',
            'https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/http.txt',
            'https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/https.txt'
        ]
        # obtain proxies
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "if-none-match": 'W/"6dbd-ytmA54vS1G4OuZa75LiLV1DQVdE"',
            "priority": "u=0, i",
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
        for url in urls:
            try:
                resp = session.get(url, headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
            except:
                continue
            protocol = urlparse(url).path.strip('/').split('/')[-1].split('.')[0]
            for item in resp.text.split('\n'):
                item = item.strip()
                if not item: continue
                try:
                    ip, port = item.split(':')
                except:
                    continue
                proxy_info = ProxyInfo(
                    source=self.source, protocol=protocol, ip=ip, port=port, anonymity="", 
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