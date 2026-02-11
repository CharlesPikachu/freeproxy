'''
Function:
    Implementation of KuaidailiProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import json_repair
from tqdm import tqdm
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''KuaidailiProxiedSession'''
class KuaidailiProxiedSession(BaseProxiedSession):
    source = 'KuaidailiProxiedSession'
    homepage = 'https://www.kuaidaili.com/free/inha/1/'
    def __init__(self, **kwargs):
        super(KuaidailiProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Cache-Control": "max-age=0", "Referer": "https://www.kuaidaili.com/free/", "Priority": "u=0, i", "Sec-Fetch-Dest": "document",
            "Cookie": "_ga=GA1.1.1864369019.1760681496; _gcl_au=1.1.1364992688.1760681496; _ss_s_uid=1b98b08ced2f1593cbe681865367d6ff; _c_WBKFRo=mRxb7QxJwWmnkswyxZyEkP5mHxMuYnEZ7Ej0zYBX; channelid=0; sid=1763310002694491; _ga_DC1XM0P4JL=GS2.1.s1764710961$o8$g1$t1764712249$j4$l0$h0; _uetsid=f7c306d0cfc511f088a86b03723d086f; _uetvid=1d9648c0ab2811f0802a5b28cd762674", "Sec-Fetch-User": "?1",
            "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin",  "Upgrade-Insecure-Requests": "1", "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"', "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies: 'https://www.kuaidaili.com/free/inha/1/'
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.kuaidaili.com/free/inha/{page}/', headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
                pattern = re.compile(r'\b(?:const|let|var)\s+fpsList\s*=\s*(\[[\s\S]*?\])\s*;', re.MULTILINE)
                m = pattern.search(resp.text); proxies = m.group(1); proxies = json_repair.loads(proxies)
            except:
                continue
            for proxy in proxies:
                try: proxy_info = ProxyInfo(source=self.source, protocol='http', ip=proxy['ip'], port=proxy['port'], anonymity='elite', delay=proxy['speed'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # obtain proxies: 'https://www.kuaidaili.com/free/dps/1/'
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.kuaidaili.com/free/dps/{page}/', headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
                pattern = re.compile(r'\b(?:const|let|var)\s+fpsList\s*=\s*(\[[\s\S]*?\])\s*;', re.MULTILINE)
                m = pattern.search(resp.text); proxies = m.group(1); proxies = json_repair.loads(proxies)
            except:
                continue
            for proxy in proxies:
                if not isinstance(proxy, dict) or not proxy.get('is_valid'): continue
                try: proxy_info = ProxyInfo(source=self.source, protocol='https', ip=proxy['ip'], port=proxy['port'], anonymity='elite', delay=proxy['speed'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # obtain proxies: 'https://www.kuaidaili.com/free/intr/1/'
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.kuaidaili.com/free/intr/{page}/', headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
                pattern = re.compile(r'\b(?:const|let|var)\s+fpsList\s*=\s*(\[[\s\S]*?\])\s*;', re.MULTILINE)
                m = pattern.search(resp.text); proxies = m.group(1); proxies = json_repair.loads(proxies)
            except:
                continue
            for proxy in proxies:
                try: proxy_info = ProxyInfo(source=self.source, protocol='http', ip=proxy['ip'], port=proxy['port'], anonymity='elite', delay=proxy['speed'])
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # obtain proxies: 'https://www.kuaidaili.com/free/fps/1/'
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.kuaidaili.com/free/fps/{page}/', headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
                pattern = re.compile(r'\b(?:const|let|var)\s+fpsList\s*=\s*(\[[\s\S]*?\])\s*;', re.MULTILINE)
                m = pattern.search(resp.text); proxies = m.group(1); proxies = json_repair.loads(proxies)
            except:
                continue
            for proxy in proxies:
                try: proxy_info = ProxyInfo(source=self.source, protocol='https', ip=proxy['ip'], port=proxy['port'], anonymity='elite', delay=proxy['speed'])
                except Exception: continue
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