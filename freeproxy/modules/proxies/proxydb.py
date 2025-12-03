'''
Function:
    Implementation of ProxydbProxiedSession
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


'''ProxydbProxiedSession'''
class ProxydbProxiedSession(BaseProxiedSession):
    source = 'ProxydbProxiedSession'
    homepage = 'https://proxydb.net/?offset=0'
    def __init__(self, **kwargs):
        super(ProxydbProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                resp = session.get(f'https://proxydb.net/?offset={(page - 1) * 30}', headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, 'lxml')
                soup = soup.select_one("table.table.table-sm.table-hover.table-striped")
                trs = soup.select("tbody > tr")
            except:
                continue
            for item in trs:
                try:
                    tds = item.find_all("td")
                    port_link = tds[1].find_all("a")[-1] if tds[1].find_all("a") else None
                    port = (port_link.get_text(strip=True) if port_link else tds[1].get_text(strip=True)).strip()
                    country_code = tds[3].get_text(strip=True)
                    anonymity = tds[4].get_text(strip=True).lower()
                    if anonymity == 'High Anonymous'.lower(): anonymity = 'elite'
                    proxy_info = ProxyInfo(
                        source=self.source, protocol=tds[2].get_text(strip=True).lower(), ip=tds[0].get_text(strip=True).strip(), 
                        port=port, anonymity=anonymity, country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']),
                        delay=int(float(re.match(r"^(\d*\.?\d+)", tds[6].get_text(strip=True)).group(1)) * 1000), 
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies