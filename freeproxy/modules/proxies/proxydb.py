'''
Function:
    Implementation of ProxydbProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''ProxydbProxiedSession'''
class ProxydbProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxydbProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            resp = requests.get(f'https://proxydb.net/?offset={(page - 1) * 30}', headers=self.randomheaders())
            if resp.status_code != 200: continue
            soup = BeautifulSoup(resp.text, 'lxml')
            soup = soup.select_one("table.table.table-sm.table-hover.table-striped")
            for item in soup.select("tbody > tr"):
                tds = item.find_all("td")
                if len(tds) < 9: continue
                ip = (tds[0].get_text(strip=True) or "").strip()
                port_link = tds[1].find_all("a")[-1] if tds[1].find_all("a") else None
                port = (port_link.get_text(strip=True) if port_link else tds[1].get_text(strip=True)).strip()
                ptype_raw = tds[2].get_text(strip=True).lower()
                formatted_proxy = f"{ptype_raw}://{ip}:{port}"
                self.candidate_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})
        # return
        return self.candidate_proxies