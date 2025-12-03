'''
Function:
    Implementation of IP89ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''IP89ProxiedSession'''
class IP89ProxiedSession(BaseProxiedSession):
    source = 'IP89ProxiedSession'
    homepage = 'https://api.89ip.cn/tqdl.html?api=1&num=1000&port=&address=&isp='
    def __init__(self, **kwargs):
        super(IP89ProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        octet = r'(?:25[0-5]|2[0-4]\d|1?\d?\d)'
        port  = r'(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3})'
        PATTERN = re.compile(rf'^{octet}\.{octet}\.{octet}\.{octet}:{port}$')
        # obtain proxies
        headers = {
            "Cookie": "SITE_TOTAL_ID=28e0ae30b9d2b0a987fabb84a43c5463; Hm_lvt_f9e56acddd5155c92b9b5499ff966848=1763228860; https_waf_cookie=6320761e-bf5e-4bc528dc5bc370a4cfba1f09d75c67e9c505; https_ydclearance=e82780cd571068577c7a6319-4565-457f-9838-834798c3daef-1764713025",
            "Host": "api.89ip.cn",
            "Referer": "https://api.89ip.cn/tqdl.html?api=1&num=200&port=&address=&isp=",
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        params = {"api": "1", "num": "200", "port": "", "address": "", "isp": ""}
        try:
            resp = session.get('https://api.89ip.cn/tqdl.html', params=params, headers=self.getrandomheaders(headers_override=headers))
            resp.raise_for_status()
        except:
            return self.candidate_proxies
        for item in resp.text.split('<br>'):
            if PATTERN.fullmatch(item.strip()) is None: continue
            try:
                ip, port = item.split(':')
            except:
                continue
            proxy_info = ProxyInfo(
                source=self.source, protocol='http', ip=ip, port=port, anonymity="", 
            )
            self.candidate_proxies.append(proxy_info)
        # append country code info
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_map = {
                executor.submit(IPLocater.locate, p.ip): p for p in self.candidate_proxies
            }
            for future in as_completed(future_map):
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