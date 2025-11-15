'''
Function:
    Implementation of Tomcat1235ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''Tomcat1235ProxiedSession'''
class Tomcat1235ProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(Tomcat1235ProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            resp = requests.get(f'https://tomcat1235.nyc.mn/proxy_list?page={page}', headers=self.randomheaders(headers_override=headers), timeout=60)
            if resp.status_code != 200: continue
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'html.parser')
            table = soup.find('table')
            if not table: continue
            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')
                if len(cells) < 4: continue
                protocol, ip, port = cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip()
                self.candidate_proxies.append({'http': f"{protocol}://{ip}:{port}", 'https': f"{protocol}://{ip}:{port}"})
        # return
        return self.candidate_proxies