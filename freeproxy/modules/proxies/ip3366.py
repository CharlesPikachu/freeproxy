'''
Function:
    Implementation of IP3366ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensureplaywrightchromium, filterinvalidproxies, applyfilterrule, ProxyInfo


'''IP3366ProxiedSession'''
class IP3366ProxiedSession(BaseProxiedSession):
    source = 'IP3366ProxiedSession'
    homepage = 'http://www.ip3366.net/free/?stype=1&page=1'
    def __init__(self, **kwargs):
        super(IP3366ProxiedSession, self).__init__(**kwargs)
    '''_getcookies'''
    def _getcookies(self):
        from playwright.sync_api import sync_playwright
        ensureplaywrightchromium()
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://www.ip3366.net/free/?stype=1&page=1", wait_until="networkidle")
            cookies = context.cookies()
            context.close(); browser.close()
            cookies_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            return cookies_str
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, headers = [], {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Host": "www.ip3366.net",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Proxy-Connection": "keep-alive", "Referer": "http://www.ip3366.net/free/?stype=1", "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
        }
        # obtain proxies
        num_tries = 0
        while True:
            headers['Cookie'], session = self._getcookies(), requests.Session()
            for page in range(1, self.max_pages+1):
                for stype in [1, 2]:
                    try:
                        resp = session.get(f'http://www.ip3366.net/free/?stype={stype}&page={page}', headers=self.getrandomheaders(headers_override=headers))
                        resp.raise_for_status()
                        soup = BeautifulSoup(resp.text, 'lxml'); soup = soup.find('table', attrs={'class': 'table table-bordered table-striped'})
                        trs = soup.find('tbody').find_all('tr')
                        headers.update({'Referer': f'http://www.ip3366.net/free/?stype={stype}&page={page}'})
                    except:
                        continue
                    for item in trs:
                        try: proxy_info = ProxyInfo(source=self.source, protocol=item.find_all('td')[3].text.strip().lower(), ip=item.find_all('td')[0].text.strip(), port=item.find_all('td')[1].text.strip(), anonymity='elite' if stype in [1] else 'anonymous', country_code='CN', in_chinese_mainland=True, delay=int(re.match(r"^(\d+)", item.find_all('td')[5].text.strip()).group(1)) * 1000)
                        except Exception: continue
                        self.candidate_proxies.append(proxy_info)
            num_tries += 1
            if num_tries > 5 or len(self.candidate_proxies) > 0: break
        # return
        return self.candidate_proxies