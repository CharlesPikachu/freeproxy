'''
Function:
    Implementation of IP3366ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, cookies2string, ProxyInfo, DrissionPageUtils


'''IP3366ProxiedSession'''
class IP3366ProxiedSession(BaseProxiedSession):
    source = 'IP3366ProxiedSession'
    homepage = 'http://www.ip3366.net/free/?stype=1&page=1'
    def __init__(self, **kwargs):
        super(IP3366ProxiedSession, self).__init__(**kwargs)
    '''_getcookies'''
    def _getcookies(self):
        page = DrissionPageUtils.initsmartbrowser(headless=True, requests_headers=None, requests_proxies=None, requests_cookies=None)
        page.get(url="http://www.ip3366.net/free/?stype=1&page=1"); cookies = DrissionPageUtils.getcookiesdict(page=page); DrissionPageUtils.quitpage(page=page)
        return cookies2string(cookies)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        num_tries, self.candidate_proxies, headers = 0, [], {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Host": "www.ip3366.net",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Proxy-Connection": "keep-alive", "Referer": "http://www.ip3366.net/free/?stype=1", "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
        }
        # obtain proxies
        while True:
            headers['Cookie'], session = self._getcookies(), requests.Session()
            for page in range(1, self.max_pages+1):
                for stype in [1, 2]:
                    try: (resp := session.get(f'http://www.ip3366.net/free/?stype={stype}&page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); trs = BeautifulSoup(resp.text, 'lxml').find('table', attrs={'class': 'table table-bordered table-striped'}).find('tbody').find_all('tr')
                    except Exception: continue
                    headers.update({'Referer': f'http://www.ip3366.net/free/?stype={stype}&page={page}'})
                    for item in trs:
                        try: proxy_info = ProxyInfo(source=self.source, protocol=item.find_all('td')[3].text.strip().lower(), ip=item.find_all('td')[0].text.strip(), port=item.find_all('td')[1].text.strip(), anonymity='elite' if stype in [1] else 'anonymous', country_code='CN', in_chinese_mainland=True, delay=int(re.match(r"^(\d+)", item.find_all('td')[5].text.strip()).group(1)) * 1000)
                        except Exception: continue
                        self.candidate_proxies.append(proxy_info)
            if (num_tries := num_tries + 1) > 5 or len(self.candidate_proxies) > 0: break
        # return
        return self.candidate_proxies