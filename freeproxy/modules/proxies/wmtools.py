
'''
Function:
    Implementation of WMToolsProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from bs4 import BeautifulSoup
from typing_extensions import Unpack
from urllib.parse import urljoin, urlparse
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''WMToolsProxiedSession'''
class WMToolsProxiedSession(BaseProxiedSession):
    source = 'WMToolsProxiedSession'
    homepage = 'https://wmgrid.com/zh/proxy'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(WMToolsProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, protocols = [], requests.Session(), ['http', 'socks4', 'socks5']
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        urls, anonymity_map = {protocol: [f'{self.homepage}/{protocol}'] for protocol in protocols}, {'高匿': 'elite', '普匿': 'anonymous', '透明': 'transparent'}
        # obtain country-specific pages
        if self.max_pages > 1:
            try:
                (resp := session.get(self.homepage, headers=self.getrandomheaders(base_headers=headers), timeout=60)).raise_for_status()
                for link in BeautifulSoup(resp.text, 'html.parser').select('a[href]'):
                    parts = (parsed := urlparse((url := urljoin(self.homepage, link['href'])))).path.strip('/').split('/')
                    if parsed.netloc != 'wmgrid.com' or len(parts) != 4: continue
                    if parts[:2] != ['zh', 'proxy'] or parts[2] not in protocols: continue
                    if len(parts[3]) != 2 or not parts[3].isalpha(): continue
                    if url not in urls[parts[2]]: urls[parts[2]].append(url)
            except Exception: pass
        # obtain proxies
        for protocol in protocols:
            for url in urls[protocol][:self.max_pages]:
                try:
                    (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers), timeout=60)).raise_for_status()
                    if (table := BeautifulSoup(resp.text, 'html.parser').find('table')) is None: continue
                except Exception: continue
                for row in table.select('tr'):
                    try:
                        if len((cells := [td.get_text(' ', strip=True) for td in row.find_all('td')])) < 7: continue
                        ip, port = cells[0].rsplit(':', 1); ip, port = ip.strip('[]'), port.strip()
                        if (item_protocol := cells[1].lower()) not in protocols: continue
                        country_code, anonymity = cells[2].upper() if re.fullmatch(r'[A-Za-z]{2}', cells[2]) else '', anonymity_map.get(cells[3], '')
                        delay = float(delay_match.group()) if (delay_match := re.search(r'\d+(?:\.\d+)?', cells[5])) else None
                        proxy_info = ProxyInfo(source=self.source, protocol=item_protocol, ip=ip, port=port, country_code=country_code, in_chinese_mainland=(country_code == 'CN'), anonymity=anonymity, delay=delay)
                    except Exception: continue
                    self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies