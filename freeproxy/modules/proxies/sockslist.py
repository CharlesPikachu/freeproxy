'''
Function:
    Implementation of SocksListProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
import pycountry
from lxml import html
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''SocksListProxiedSession'''
class SocksListProxiedSession(BaseProxiedSession):
    source = 'SocksListProxiedSession'
    homepage = 'https://sockslist.us/'
    def __init__(self, **kwargs):
        super(SocksListProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "accept": "*/*", "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://sockslist.us", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "sec-fetch-dest": "empty", "x-requested-with": "XMLHttpRequest", "sec-ch-ua-platform": '"Windows"', 
            "priority": "u=1, i", "referer": "https://sockslist.us/", "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"', "sec-ch-ua-mobile": "?0", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.post('https://sockslist.us/server/index.php?controller=FrontPublic&action=ActionGetProxy', headers=self.getrandomheaders(base_headers=headers), data={'page': page, 'country': 'All'})).raise_for_status(); target_table = None
            except Exception: continue
            for table in html.fromstring(resp.text).xpath('//table'):
                headers = [h.strip() for h in table.xpath('.//thead//th//text()') if h.strip()]
                if {'Ip', 'Port', 'Type', 'Level'}.issubset(set(headers)): target_table = table; break
            if target_table is None: continue
            headers, rows = [h.strip() for h in target_table.xpath('.//thead//th//text()') if h.strip()], []
            for tr in target_table.xpath('.//tbody/tr'): len(cells := [' '.join(td.xpath('.//text()')).strip() for td in tr.xpath('./td')]) == len(headers) and rows.append(dict(zip(headers, cells)))
            for item in rows:
                try: country_code = str(pycountry.countries.lookup(str(item['Country'])).alpha_2).upper()
                except Exception: country_code = ''
                try: proxy_info = ProxyInfo(source=self.source, protocol=str(item['Type']).lower(), ip=item['Ip'], port=item['Port'], anonymity=str(item['Level']).lower().rstrip('+'), delay=None, country_code=country_code, in_chinese_mainland=(country_code.lower() in {'cn'}))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies