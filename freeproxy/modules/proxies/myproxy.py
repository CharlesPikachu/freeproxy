'''
Function:
    Implementation of MyProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''MyProxyProxiedSession'''
class MyProxyProxiedSession(BaseProxiedSession):
    source = 'MyProxyProxiedSession'
    homepage = 'https://www.my-proxy.com/free-proxy-list.html'
    def __init__(self, **kwargs):
        super(MyProxyProxiedSession, self).__init__(**kwargs)
    '''_extractproxies'''
    def _extractproxies(self, html: str, protocol: str, anonymity: str = ''):
        pattern, proxies = re.compile(r'(?P<ip>(?:25[0-5]|2[0-4]\d|1?\d?\d)' r'(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3})' r':(?P<port>\d{1,5})#(?P<country>[A-Z]{2})'), []
        for match in pattern.finditer(html or ''):
            country_code = match.group('country').upper()
            try: proxies.append(ProxyInfo(source=self.source, protocol=protocol, ip=match.group('ip'), port=match.group('port'), country_code=country_code, in_chinese_mainland=(country_code == 'CN'), anonymity=anonymity))
            except Exception: continue
        return proxies
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers, urls = [], requests.Session(), {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}, []
        # HTTP pages: free-proxy-list.html, free-proxy-list-2.html, ...
        for page in range(1, min(self.max_pages, 10) + 1):
            if page == 1: urls.append(('https://www.my-proxy.com/free-proxy-list.html', 'http', ''))
            else: urls.append((f'https://www.my-proxy.com/free-proxy-list-{page}.html', 'http', ''))
        # extra categorized pages
        urls.extend([('https://www.my-proxy.com/free-elite-proxy.html', 'http', 'elite'), ('https://www.my-proxy.com/free-anonymous-proxy.html', 'http', 'anonymous'), ('https://www.my-proxy.com/free-transparent-proxy.html', 'http', 'transparent'), ('https://www.my-proxy.com/free-socks-4-proxy.html', 'socks4', 'elite'), ('https://www.my-proxy.com/free-socks-5-proxy.html', 'socks5', 'elite')])
        # obtain proxies
        for url, protocol, anonymity in urls:
            try: (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status(); resp.encoding = resp.apparent_encoding or 'utf-8'
            except Exception: continue
            self.candidate_proxies.extend(self._extractproxies(resp.text, protocol=protocol, anonymity=anonymity))
        # return
        return self.candidate_proxies