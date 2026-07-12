'''
Function:
    Implementation of ProxyNovaProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import base64
import quickjs
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyNovaProxiedSession'''
class ProxyNovaProxiedSession(BaseProxiedSession):
    source = 'ProxyNovaProxiedSession'
    homepage = 'https://www.proxynova.com/proxy-server-list/'
    def __init__(self, **kwargs):
        super(ProxyNovaProxiedSession, self).__init__(**kwargs)
    '''_jsiptotext'''
    def _jsiptotext(self, script_body: str):
        try:
            expression, context = re.search(r'document\.write\((.*)\)\s*;?', script_body, re.S).group(1), quickjs.Context()
            context.add_callable('atob', lambda text: base64.b64decode(text).decode())
            return str(context.eval(expression)).strip()
        except Exception:
            return ''
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}
        # obtain proxies
        try: (resp := session.get(self.homepage, headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
        except Exception: return self.candidate_proxies
        for tr in BeautifulSoup(resp.text, 'lxml').select('#tbl_proxy_list tbody > tr'):
            if len((tds := tr.find_all('td'))) < 7: continue
            if not (ip := self._jsiptotext(script.text) if (script := tds[0].find('script')) else tds[0].get_text(strip=True)): continue
            delay = re.search(r'(\d+)\s*ms', tds[3].get_text(' ', strip=True), re.I)
            country_code = next((item[5:].upper() for item in flag.get('class', []) if item.startswith('flag-')), '') if (flag := tds[5].find('img')) else ''
            proxy_info = ProxyInfo(source=self.source, protocol='http', ip=ip, port=tds[1].get_text(strip=True), anonymity=tds[6].get_text(' ', strip=True).lower(), country_code=country_code, in_chinese_mainland=(country_code in ['CN']), delay=int(delay.group(1)) if delay else None)
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies