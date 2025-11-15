'''
Function:
    Implementation of KxdailiProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests
from lxml import etree
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''KxdailiProxiedSession'''
class KxdailiProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(KxdailiProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for base_url in ['http://www.kxdaili.com/dailiip/1/', 'http://www.kxdaili.com/dailiip/2/']:
            for page in (1, self.max_pages + 1):
                resp = requests.get(base_url + f'{page}.html', headers=self.randomheaders())
                if resp.status_code != 200: continue
                parsed_tree = etree.HTML(resp.content.decode('utf-8'))
                table = parsed_tree.xpath('//table')
                if not table: continue
                table = table[0]
                for tr in table.xpath('.//tr'):
                    ip = "".join(tr.xpath("./td[1]/text()")).strip()
                    port = "".join(tr.xpath("./td[2]/text()")).strip()
                    protocol = "".join(tr.xpath("./td[4]/text()")).strip().split(',')[0].lower()
                    if not ip or not port: continue
                    self.candidate_proxies.append({'http': f'{protocol}://{ip}:{port}', 'https': f'{protocol}://{ip}:{port}'})
        # return
        return self.candidate_proxies