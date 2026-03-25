'''
Function:
    Implementation of FineProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import random
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater, DrissionPageUtils


'''FineProxyProxiedSession'''
class FineProxyProxiedSession(BaseProxiedSession):
    source = 'FineProxyProxiedSession'
    homepage = 'https://fineproxy.org/cn/free-proxy/'
    def __init__(self, **kwargs):
        super(FineProxyProxiedSession, self).__init__(**kwargs)
    '''_getnonce'''
    def _getnonce(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        page = DrissionPageUtils.initsmartbrowser(headless=True, requests_headers=headers, requests_proxies=None, requests_cookies=None)
        page.get(self.homepage); m = re.search(r'"nonce"\s*:\s*"([^"]+)"', page.html); nonce = m.group(1); DrissionPageUtils.quitpage(page=page)
        return nonce
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, nonce = [], requests.Session(), self._getnonce()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            data = {'action': 'proxylister_load_more', 'nonce': nonce, 'page': f'{page}', 'atts[downloads]': 'true'}
            try: (resp := session.post('https://fineproxy.org/wp-admin/admin-ajax.php', headers=self.getrandomheaders(base_headers=headers), timeout=60, data=data)).raise_for_status(); resp.encoding = 'utf-8'; rows = resp.json()['data']['rows']
            except Exception: continue
            for row in (BeautifulSoup(rows, 'html.parser').find_all('tr') or []):
                if not (cells := row.find_all('td')) or (len(cells) < 7): continue
                protocol: str = random.choice(str(cells[2].text).strip().lower().split(',')); anonymity = ""
                if str(cells[3].text).strip().lower() in ('anonymous', 'elite', 'transparent'): anonymity = str(cells[3].text).strip().lower()
                elif '佚名' in str(cells[3].text).strip(): anonymity = 'anonymous'
                try: proxy_info = ProxyInfo(source=self.source, ip=str(cells[0].text).strip(), port=str(cells[1].text).strip(), protocol=protocol.strip(), delay=int(float(re.search(r'^(\d+)', str(cells[6].text).strip()).group(1))), anonymity=anonymity.lower())
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