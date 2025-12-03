'''
Function:
    Implementation of ProxyhubProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyhubProxiedSession'''
class ProxyhubProxiedSession(BaseProxiedSession):
    source = 'ProxyhubProxiedSession'
    homepage = 'https://proxyhub.me/'
    def __init__(self, **kwargs):
        super(ProxyhubProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        # obtain proxies
        try:
            resp = session.get('https://proxyhub.me/', headers=self.getrandomheaders())
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'lxml')
            soup = soup.select_one("div.list table.table")
            trs = soup.select("tbody tr")
        except:
            return self.candidate_proxies
        urls = []
        for tr in trs:
            try:
                tds = tr.find_all("td")
                urls.append(tds[4].find("a")['href'])
            except:
                continue
        if not urls: return self.candidate_proxies
        urls = list(set(urls))
        for url in urls:
            try:
                resp = session.get(f'https://proxyhub.me{url}')
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, 'lxml')
                soup = soup.select_one("div.list table.table")
                trs = soup.select("tbody tr")
                m = re.search(r"/en/([a-z]{2})-free-proxy-list(?:\.html?)?$", url, re.IGNORECASE)
                country_code = m.group(1).upper()
            except:
                continue
            for tr in trs:
                try:
                    tds = tr.find_all("td")
                    proxy_info = ProxyInfo(
                        source=self.source, protocol=tds[2].get_text(strip=True).strip().lower(), ip=tds[0].get_text(strip=True).strip(),
                        port=tds[1].get_text(strip=True).strip(), anonymity=tds[3].get_text(strip=True).strip().lower(), 
                        country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']), 
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies