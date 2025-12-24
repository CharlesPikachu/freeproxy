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
from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, ensureplaywrightchromium, ProxyInfo, IPLocater


'''FineProxyProxiedSession'''
class FineProxyProxiedSession(BaseProxiedSession):
    source = 'FineProxyProxiedSession'
    homepage = 'https://fineproxy.org/cn/free-proxy/'
    def __init__(self, **kwargs):
        super(FineProxyProxiedSession, self).__init__(**kwargs)
    '''_fetchnonce'''
    def _fetchnonce(self):
        ensureplaywrightchromium()
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.homepage)
            html = page.content()
            browser.close()
            m = re.search(r'"nonce"\s*:\s*"([^"]+)"', html)
            nonce = m.group(1)
            return nonce
    '''refreshproxies'''
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        nonce = self._fetchnonce()
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                data = {'action': 'proxylister_load_more', 'nonce': nonce, 'page': f'{page}', 'atts[downloads]': 'true'}
                resp = session.post('https://fineproxy.org/wp-admin/admin-ajax.php', headers=self.getrandomheaders(headers_override=headers), timeout=60, data=data)
                resp.raise_for_status()
                resp.encoding = 'utf-8'
                rows = resp.json()['data']['rows']
                soup = BeautifulSoup(rows, 'html.parser')
                trs = soup.find_all('tr')
            except:
                continue
            for row in trs:
                try:
                    cells = row.find_all('td')
                    protocol: str = random.choice(cells[2].text.strip().lower().split(','))
                    anonymity = cells[3].text.strip()
                    if anonymity == '佚名': anonymity = 'anonymous'
                    proxy_info = ProxyInfo(
                        source=self.source, ip=cells[0].text.strip(), port=cells[1].text.strip(), protocol=protocol.strip(),
                        delay=int(float(re.search(r'^(\d+)', cells[6].text.strip()).group(1))), anonymity=anonymity.lower()
                    )
                except:
                    continue
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