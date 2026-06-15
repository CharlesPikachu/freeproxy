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
from urllib.parse import urljoin
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
        self.candidate_proxies, session, urls, headers = [], requests.Session(), [], self.getrandomheaders()
        # obtain country urls
        (resp := session.get('https://proxyhub.me/', headers=headers, timeout=60)).raise_for_status()
        if not (table := BeautifulSoup(resp.text, 'lxml').select_one(".list table.table")): return self.candidate_proxies
        for tr in table.select("tbody tr"):
            try: tds = tr.find_all("td"); urls.append(tds[0].find("a")['href'])
            except Exception: continue
        if not (urls := list(set(urls))): return self.candidate_proxies
        # obtain proxies
        for url in urls:
            try:
                (resp := session.get(urljoin('https://proxyhub.me/', url), headers=headers, timeout=60)).raise_for_status()
                if not (table := BeautifulSoup(resp.text, 'lxml').select_one(".list table.table")): continue
                if not (m := re.search(r"/en/([a-z]{2})-free-proxy-list(?:\.html?)?$", url, re.IGNORECASE)): continue
                country_code = m.group(1).upper(); trs = table.select("tbody tr")
            except Exception:
                continue
            for tr in trs:
                try: tds = tr.find_all("td"); proxy_info = ProxyInfo(source=self.source, protocol=tds[3].get_text(strip=True).strip().lower(), ip=tds[1].get_text(strip=True).strip(), port=tds[2].get_text(strip=True).strip(), anonymity=tds[4].get_text(strip=True).strip().lower(), country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies