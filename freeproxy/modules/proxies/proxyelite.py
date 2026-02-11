'''
Function:
    Implementation of ProxyEliteProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import random
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, ensureplaywrightchromium, ProxyInfo


'''ProxyEliteProxiedSession'''
class ProxyEliteProxiedSession(BaseProxiedSession):
    source = 'ProxyEliteProxiedSession'
    homepage = 'https://proxyelite.info/cn/free/asia/china/'
    def __init__(self, **kwargs):
        super(ProxyEliteProxiedSession, self).__init__(**kwargs)
    '''_fetchnonce'''
    def _fetchnonce(self):
        from playwright.sync_api import sync_playwright
        ensureplaywrightchromium()
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.homepage)
            html = page.content()
            context.close(); browser.close()
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
                resp = session.post('https://proxyelite.info/wp-admin/admin-ajax.php', headers=self.getrandomheaders(headers_override=headers), timeout=60, data=data)
                resp.raise_for_status(); resp.encoding = 'utf-8'; rows = resp.json()['data']['rows']; soup = BeautifulSoup(rows, 'html.parser'); trs = soup.find_all('tr')
            except:
                continue
            for row in trs:
                try:
                    cells = row.find_all('td')
                    protocol: str = random.choice(cells[2].text.strip().lower().split(','))
                    if cells[3].text.strip().lower() in ('anonymous', 'elite', 'transparent'): anonymity = cells[3].text.strip().lower()
                    elif '匿名' in cells[3].text.strip(): anonymity = 'anonymous'
                    elif '精英' in cells[3].text.strip(): anonymity = 'elite'
                    else: anonymity = 'transparent'
                    proxy_info = ProxyInfo(source=self.source, ip=cells[0].text.strip(), port=cells[1].text.strip(), protocol=protocol.strip(), delay=int(float(re.search(r'^(\d+)', cells[6].text.strip()).group(1))), anonymity=anonymity.lower(), country_code='CN', in_chinese_mainland=True)
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies