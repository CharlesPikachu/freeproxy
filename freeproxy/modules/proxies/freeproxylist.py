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
from ..utils import ensurevalidrequestsproxies


'''FreeproxylistProxiedSession'''
class FreeproxylistProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(FreeproxylistProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        resp = requests.get('https://free-proxy-list.net/', headers=self.randomheaders())
        if resp.status_code != 200: return self.candidate_proxies
        parsed_tree = etree.HTML(resp.text)
        proxy_table = parsed_tree.xpath('//div[@class="table-responsive fpl-list"]/table')[0]
        tr_list = proxy_table.xpath('.//tr')
        for tr in tr_list:
            ip = "".join(tr.xpath("./td[1]/text()")).strip()
            port = "".join(tr.xpath("./td[2]/text()")).strip()
            https = "".join(tr.xpath("./td[7]/text()")).strip().lower()
            if not ip or not port: continue
            if https == 'yes':
                self.candidate_proxies.append({'http': f'https://{ip}:{port}', 'https': f'https://{ip}:{port}'})
            else:
                self.candidate_proxies.append({'http': f'http://{ip}:{port}', 'https': f'http://{ip}:{port}'})
        # return
        return self.candidate_proxies