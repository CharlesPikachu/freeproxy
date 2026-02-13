'''
Function:
    Implementation of DpangestuwProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from tqdm import tqdm
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''DpangestuwProxiedSession'''
class DpangestuwProxiedSession(BaseProxiedSession):
    source = 'DpangestuwProxiedSession'
    def __init__(self, **kwargs):
        super(DpangestuwProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        try: (resp := session.get('https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/allive.txt', headers=headers)).raise_for_status()
        except Exception: return self.candidate_proxies
        for item in resp.text.split('\n'):
            try: protocol, ip, port = re.match(r'(?:(\w+)://)?(\d{1,3}(?:\.\d{1,3}){3}):(\d+)', item.strip()).groups(default='http')
            except Exception: continue
            self.candidate_proxies.append(ProxyInfo(source=self.source, protocol=protocol, ip=ip, port=port, country_code="", in_chinese_mainland=None, anonymity=""))
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