'''
Function:
    Implementation of HideProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import random
import requests
import pycountry
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''HideProxiedSession'''
class HideProxiedSession(BaseProxiedSession):
    source = 'HideProxiedSession'
    homepage = 'https://hide.mn/en/proxy-list/'
    def __init__(self, **kwargs):
        super(HideProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36", "Referer": "https://hide.mn/en/proxy-list/"}
        anonymity_mapper = {"high": "elite", "average": "anonymous", "low": "transparent"}
        # obtain proxies
        for page in range(self.max_pages):
            url = "https://hide.mn/en/proxy-list/" if page == 0 else f"https://hide.mn/en/proxy-list/?start={page * 64}"
            try: (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in (BeautifulSoup(resp.text, 'lxml').select("tbody tr") or []):
                if len((td := item.find_all("td"))) < 6: continue
                try: country_code = str(pycountry.countries.lookup(td[2].get_text(" ", strip=True)).alpha_2).upper()
                except Exception: country_code = ''
                try: proxy_info = ProxyInfo(source=self.source, protocol=random.choice(td[4].get_text(strip=True).lower().split(',')).strip(), ip=td[0].get_text(strip=True), port=td[1].get_text(strip=True), anonymity=anonymity_mapper.get(td[5].get_text(strip=True).lower(), 'transparent'), delay=int(re.search(r"\d+", td[3].get_text(" ", strip=True)).group()), country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies