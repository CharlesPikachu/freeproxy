'''
Function:
    Implementation of SpysMeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account:
    Charles的皮卡丘
'''
import re
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''SpysMeProxiedSession'''
class SpysMeProxiedSession(BaseProxiedSession):
    source = 'SpysMeProxiedSession'
    homepage = 'https://spys.me/'
    def __init__(self, **kwargs):
        super(SpysMeProxiedSession, self).__init__(**kwargs)
    '''_extractproxies'''
    def _extractproxies(self, text, default_protocol):
        pattern = re.compile(r'(?P<ip>(?:25[0-5]|2[0-4]\d|1?\d?\d)' r'(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3})' r':(?P<port>\d{1,5})' r'(?:\s+(?P<country>[A-Z]{2})-(?P<level>[NAH])(?P<ssl>-S)?)?', flags=re.I)
        anonymity_map, proxies = {'N': 'transparent', 'A': 'anonymous', 'H': 'elite'}, []
        for match in pattern.finditer(text or ''):
            country_code, level, ssl_supported = (match.group('country') or '').upper(), (match.group('level') or '').upper(), bool(match.group('ssl'))
            protocol = 'https' if (default_protocol == 'http' and ssl_supported) else default_protocol
            try: proxies.append(ProxyInfo(source=self.source, protocol=protocol, ip=match.group('ip'), port=match.group('port'), country_code=country_code, in_chinese_mainland=(country_code == 'CN') if country_code else False, anonymity=anonymity_map.get(level, '')))
            except Exception: continue
        return proxies
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        self.candidate_proxies, session, headers = [], requests.Session(), {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        urls = [('https://spys.me/proxy.txt', 'http'), ('https://spys.me/socks.txt', 'socks5')]
        for url, default_protocol in urls:
            try: (resp := session.get(url, headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status()
            except Exception: continue
            self.candidate_proxies.extend(self._extractproxies(resp.text, default_protocol))
        return self.candidate_proxies