'''
Function:
    Implementation of IhuanProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from lxml import etree
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''IhuanProxiedSession'''
class IhuanProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(IhuanProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        # visit 'https://ip.ihuan.me/ti.html'
        headers = self.randomheaders()
        session.headers.update(headers)
        resp = session.get('https://ip.ihuan.me/ti.html')
        if resp.status_code != 200:
            session.headers.update({'Referer': 'https://ip.ihuan.me'})
            resp = session.get('https://ip.ihuan.me/ti.html', headers=headers)
        session.headers.update({'Referer': 'https://ip.ihuan.me/ti.html'})
        # key
        resp = session.get(f'https://ip.ihuan.me/mouse.do')
        match = re.search(r'\$\(\"input\[name=\'key\'\]\"\)\.val\(\"([a-fA-F0-9]+)\"\)', resp.text)
        if match: key = match.group(1)
        else: return self.candidate_proxies
        session.headers.update({"Origin": 'https://ip.ihuan.me/'})
        # obtain proxies
        data_items = [
            {'num': '3000', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '', 'type': '', 'post': '', 'sort': '', 'key': key},
            {'num': '3000', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '', 'type': '', 'post': '', 'sort': '', 'key': key},
        ]
        for data in data_items:
            resp = session.post('https://ip.ihuan.me/tqdl.html', data=data)
            parsed_text = etree.HTML(resp.text)
            panel_body = parsed_text.xpath('//div[@class="col-md-10"]/div[@class="panel panel-default"]/div[@class="panel-body"]/text()')
            for proxy_str in panel_body:
                proxy_str = proxy_str.strip()
                if not proxy_str: continue
                self.candidate_proxies.append({'http': f'http://{proxy_str}', 'https': f'http://{proxy_str}'})
        # return
        return self.candidate_proxies