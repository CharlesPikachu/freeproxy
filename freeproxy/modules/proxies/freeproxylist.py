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
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FreeproxylistProxiedSession'''
class FreeproxylistProxiedSession(BaseProxiedSession):
    source = 'FreeproxylistProxiedSession'
    homepage = 'https://free-proxy-list.net/'
    def __init__(self, **kwargs):
        super(FreeproxylistProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        # obtain proxies
        try: resp = session.get('https://free-proxy-list.net/', headers=self.getrandomheaders()); resp.raise_for_status()
        except: return self.candidate_proxies
        parsed_html = etree.HTML(resp.text)
        proxy_table = parsed_html.xpath('//div[@class="table-responsive fpl-list"]/table')[0]
        for tr in proxy_table.xpath('.//tr')[1:]:
            try:
                https = "".join(tr.xpath("./td[7]/text()")).strip().lower()
                protocol = 'https' if https in ['yes'] else 'http'
                proxy_info = ProxyInfo(source=self.source, protocol=protocol, ip="".join(tr.xpath("./td[1]/text()")).strip(), port="".join(tr.xpath("./td[2]/text()")).strip(), anonymity="".join(tr.xpath("./td[5]/text()")).strip().split(' ')[0], country_code="".join(tr.xpath("./td[3]/text()")).strip(), in_chinese_mainland=("".join(tr.xpath("./td[3]/text()")).strip().lower() in ['cn']))
            except:
                continue
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies