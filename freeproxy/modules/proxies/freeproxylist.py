'''
Function:
    Implementation of FreeproxylistProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from lxml import etree
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FreeproxylistProxiedSession'''
class FreeproxylistProxiedSession(BaseProxiedSession):
    source = 'FreeproxylistProxiedSession'
    homepage = 'https://free-proxy-list.net/'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(FreeproxylistProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        # obtain proxies
        for path in ['', 'socks-proxy.html', 'us-proxy.html', 'uk-proxy.html', 'ssl-proxy.html', 'anonymous-proxy.html', 'google-proxy.html']:
            try: (resp := session.get(f'https://free-proxy-list.net/zh-cn/{path}', headers=self.getrandomheaders())).raise_for_status()
            except Exception: continue
            if not (proxy_tables := etree.HTML(resp.text).xpath('//div[@class="table-responsive fpl-list"]/table')): continue
            for tr in proxy_tables[0].xpath('.//tr')[1:]:
                if (not isinstance(tr, etree._Element)) or len(tr.xpath('./td')) < 7: continue
                is_new, is_socks = len(tr.xpath('./td')) == 7, path == 'socks-proxy.html'
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[1]/span/text()' if is_new else './td[2]/text()')).strip().lstrip(':')
                anonymity = ("".join(tr.xpath('./td[5]/text()' if is_new or not is_socks else './td[6]/text()')).strip().split(' ')[0]).lower()
                protocol = "".join(tr.xpath('./td[2]/text()' if is_new else './td[5]/text()')).strip().lower() if is_new or is_socks else 'http'
                https = "".join(tr.xpath('./td[6]/text()' if is_new else './td[7]/text()')).strip().lower()
                if protocol == 'http' and https == 'yes': protocol = 'https'
                country_code = "".join(tr.xpath('./td[3]/text()')).strip()
                try: proxy_info = ProxyInfo(source=self.source, protocol=protocol, ip=ip, port=port, anonymity=anonymity, country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        self.candidate_proxies = self.candidate_proxies[:self.max_proxies_per_refresh]
        return self.candidate_proxies