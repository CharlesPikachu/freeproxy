'''
Function:
    Implementation of ProxyhubProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''ProxyhubProxiedSession'''
class ProxyhubProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxyhubProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        resp = requests.get('https://proxyhub.me/', headers=self.randomheaders())
        if resp.status_code != 200: return self.candidate_proxies
        soup = BeautifulSoup(resp.text, 'lxml')
        soup = soup.select_one("div.list table.table")
        for tr in soup.select("tbody tr"):
            tds = tr.find_all("td")
            ip = tds[0].get_text(strip=True)
            port = tds[1].get_text(strip=True)
            ptype_raw = tds[2].get_text(strip=True).lower()
            formatted_proxy = f"{ptype_raw}://{ip}:{port}"
            self.candidate_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})
        # return
        return self.candidate_proxies