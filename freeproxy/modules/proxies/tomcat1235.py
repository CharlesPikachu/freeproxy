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
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo, IPLocater


'''Tomcat1235ProxiedSession'''
class Tomcat1235ProxiedSession(BaseProxiedSession):
    source = 'Tomcat1235ProxiedSession'
    homepage = 'https://tomcat1235.nyc.mn/proxy_list?page=1'
    def __init__(self, **kwargs):
        super(Tomcat1235ProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                resp = session.get(f'https://tomcat1235.nyc.mn/proxy_list?page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)
                resp.raise_for_status()
                resp.encoding = 'utf-8'
                soup = BeautifulSoup(resp.text, 'html.parser')
                table = soup.find('table')
                trs = table.find_all('tr')[1:]
            except:
                continue
            for row in trs:
                cells = row.find_all('td')
                try:
                    proxy_info = ProxyInfo(
                        source=self.source, protocol=cells[0].text.strip().lower(), ip=cells[1].text.strip(), port=cells[2].text.strip(),
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # append country code info
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_map = {
                executor.submit(IPLocater.locate, p.ip): p for p in self.candidate_proxies
            }
            for future in as_completed(future_map):
                try:
                    country_code = future.result()
                    assert country_code
                except Exception:
                    continue
                proxy_info: ProxyInfo = future_map[future]
                proxy_info.country_code = country_code
                proxy_info.in_chinese_mainland = (country_code.lower() in ['cn'])
        # return
        return self.candidate_proxies