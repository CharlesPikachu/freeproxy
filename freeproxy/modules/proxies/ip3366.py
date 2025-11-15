'''
Function:
    Implementation of IP3366ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensureplaywrightchromium
from playwright.sync_api import sync_playwright


'''IP3366ProxiedSession'''
class IP3366ProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(IP3366ProxiedSession, self).__init__(**kwargs)
    '''_getcookies'''
    def _getcookies(self):
        ensureplaywrightchromium()
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://www.ip3366.net/free/?stype=1", wait_until="networkidle")
            cookies = context.cookies()
            browser.close()
            cookies_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            return cookies_str
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        num_tries = 0
        while True:
            session = requests.Session()
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Host': 'www.ip3366.net',
                'Proxy-Connection': 'keep-alive',
                'Referer': 'http://www.ip3366.net/',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': self._getcookies(),
            }
            session.headers.update(headers)
            for page in range(1, self.max_pages+1):
                for stype in [1, 2]:
                    resp = session.get(f'http://www.ip3366.net/free/?stype={stype}&page={page}')
                    if resp.status_code != 200: continue
                    soup = BeautifulSoup(resp.text, 'lxml')
                    soup = soup.find('table', attrs={'class': 'table table-bordered table-striped'})
                    for item in soup.find('tbody').find_all('tr'):
                        formatted_proxy = f"{item.find_all('td')[3].text.strip().lower()}://{item.find_all('td')[0].text.strip()}:{item.find_all('td')[1].text.strip()}"
                        self.candidate_proxies.append({
                            'http': formatted_proxy, 'https': formatted_proxy
                        })
            num_tries += 1
            if num_tries > 5 or len(self.candidate_proxies) > 0: break
        # return
        return self.candidate_proxies