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
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''IhuanProxiedSession'''
class IhuanProxiedSession(BaseProxiedSession):
    source = 'IhuanProxiedSession'
    homepage = 'https://ip.ihuan.me/'
    def __init__(self, **kwargs):
        super(IhuanProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        try:
            session.headers.update(self.getrandomheaders(headers_override={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}))
            resp = session.get('https://ip.ihuan.me/ti.html')
            if resp.status_code != 200:
                session.headers.update({'Referer': 'https://ip.ihuan.me'})
                resp = session.get('https://ip.ihuan.me/ti.html')
            session.headers.update({'Referer': 'https://ip.ihuan.me/ti.html'})
            resp = session.get(f'https://ip.ihuan.me/mouse.do')
            match = re.search(r'\$\(\"input\[name=\'key\'\]\"\)\.val\(\"([a-fA-F0-9]+)\"\)', resp.text)
            key = match.group(1)
        except:
            return self.candidate_proxies
        # obtain proxies
        data_json_items = [
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '0', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '0', 'type': '1', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '1', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '1', 'type': '1', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '2', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '中国', 'kill_address': '', 'anonymity': '2', 'type': '1', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '0', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '0', 'type': '1', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '1', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '1', 'type': '1', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '2', 'type': '0', 'post': '', 'sort': '', 'key': key},
            {'num': '100', 'port': '', 'kill_port': '', 'address': '', 'kill_address': '中国', 'anonymity': '2', 'type': '1', 'post': '', 'sort': '', 'key': key},
        ]
        for data_json in data_json_items[1:]:
            try:
                resp = session.post('https://ip.ihuan.me/tqdl.html', data=data_json)
                parsed_html = etree.HTML(resp.text)
                panel_body = parsed_html.xpath('//div[@class="col-md-10"]/div[@class="panel panel-default"]/div[@class="panel-body"]/text()')
            except:
                continue
            protocol = 'http' if data_json['type'] in ['0'] else 'https'
            if data_json['anonymity'] in ['0']: anonymity = 'transparent'
            elif data_json['anonymity'] in ['1']: anonymity = 'anonymous'
            else: anonymity = 'elite'
            in_chinese_mainland = True if data_json['address'] in ['中国'] else False
            country_code = 'CN' if data_json['address'] in ['中国'] else ''
            for proxy_str in panel_body:
                try:
                    proxy_str: str = proxy_str.strip()
                    ip, port = proxy_str.split(':')
                except:
                    continue
                proxy_info = ProxyInfo(
                    source=self.source, protocol=protocol, ip=ip, port=port, anonymity=anonymity, in_chinese_mainland=in_chinese_mainland, country_code=country_code,
                )
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies