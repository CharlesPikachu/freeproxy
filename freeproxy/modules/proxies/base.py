'''
Function:
    Implementation of BaseProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
import ipaddress
from fake_useragent import UserAgent
from ..utils import LoggerHandle, ProxyInfo


'''BaseProxiedSession'''
class BaseProxiedSession(requests.Session):
    source = "BaseProxiedSession"
    homepage = "https://github.com/CharlesPikachu/freeproxy"
    def __init__(self, max_pages=1, logger_handle: LoggerHandle | None = None, disable_print: bool = False, filter_rule: dict = None, trust_env: bool = False, **kwargs):
        super(BaseProxiedSession, self).__init__(**kwargs)
        self.trust_env = trust_env # trust_env=True may cause requests to respect NO_PROXY or system proxy settings, which can bypass your configured proxy.
        self.max_pages = max_pages
        self.logger_handle = logger_handle if logger_handle else LoggerHandle()
        self.disable_print = disable_print
        self.filter_rule = filter_rule or {}
        self.candidate_proxies = []
    '''refreshproxies'''
    def refreshproxies(self):
        raise NotImplementedError('not to be implemented')
    '''getrandomproxy'''
    def getrandomproxy(self, proxy_format: str = 'requests'):
        assert proxy_format in ['requests', 'freeproxy']
        if len(self.candidate_proxies) < 1: self.refreshproxies()
        idx = random.randint(0, len(self.candidate_proxies)-1)
        proxy: ProxyInfo = self.candidate_proxies.pop(idx)
        return proxy if proxy_format in ['freeproxy'] else proxy.requests_format_proxy
    '''setrandomproxy'''
    def setrandomproxy(self):
        self.proxies = self.getrandomproxy(proxy_format='requests')
        return self.proxies
    '''getrandomheaders'''
    def getrandomheaders(self, headers_override: dict = None):
        # init
        headers_override = headers_override or {}
        # random public ipv4
        while True:
            ip_str = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip = ipaddress.ip_address(ip_str)
            if ip.is_global: break
        # construct default headers
        default_headers = {
            'X-Forwarded-For': ip_str, 'User-Agent': UserAgent().random, 
        }
        default_headers.update(headers_override)
        # return
        return default_headers