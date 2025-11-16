'''
Function:
    Implementation of ZdayeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from playwright.sync_api import sync_playwright
from ..utils import ensurevalidrequestsproxies, ensureplaywrightchromium


'''ZdayeProxiedSession'''
class ZdayeProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ZdayeProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        ensureplaywrightchromium()
        # obtain proxies
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()
            for page_idx in range(1, self.max_pages+1):
                tab = context.new_page()
                tab.goto(f'https://www.zdaye.com/free/{page_idx}/', wait_until="networkidle")
                html = tab.content()
                soup = BeautifulSoup(html, 'lxml')
                table = soup.find('table', attrs={'id': 'ipc'})
                for tr in table.find('tbody').find_all('tr'):
                    if len(tr.find_all('td')) < 2: continue
                    port = tr.find_all('td')[2].text.strip()
                    port = re.findall(r'(\d+)', port)[0]
                    protocol = tr.find_all('td')[0].text.strip()
                    ip = tr.find_all('td')[1].text.strip()
                    self.candidate_proxies.append({'http': f'{protocol}://{ip}:{port}', 'https': f'{protocol}://{ip}:{port}'})
        # return
        return self.candidate_proxies