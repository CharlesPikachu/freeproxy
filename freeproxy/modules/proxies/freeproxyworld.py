'''
Function:
    Implementation of FreeProxyWorldProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import random
import requests
import ipaddress
from lxml import etree
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FreeProxyWorldProxiedSession'''
class FreeProxyWorldProxiedSession(BaseProxiedSession):
    source = 'FreeProxyWorldProxiedSession'
    homepage = 'https://www.freeproxy.world/'
    def __init__(self, **kwargs):
        super(FreeProxyWorldProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        get_text_func = lambda node: ' '.join(''.join(node.itertext()).split())
        self.candidate_proxies, session, anonymity_map = [], requests.Session(), {'high': 'elite', 'no': 'transparent'}
        headers = {'referer': self.homepage, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: (resp := session.get(f'{self.homepage}?page={page}', headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status(); html = etree.HTML(resp.text); assert html is not None
            except Exception: continue
            for row in html.xpath('//table//tr[td]'):
                if len((cells := row.xpath('./td'))) < 8: continue
                ip, port = get_text_func(cells[0]), get_text_func(cells[1])
                if not ipaddress.ip_address(ip).is_global: continue
                country_code = country_match.group(1).upper() if (country_match := re.search(r'(?:\?|&)country=([A-Za-z]{2})(?:&|$)', ''.join(cells[2].xpath('.//a/@href')))) else ''
                delay = int(delay_match.group(1)) if (delay_match := re.search(r'(\d+)', get_text_func(cells[4]))) else None
                protocols = [str(item).strip().lower() for item in cells[5].xpath('.//a/text()') if str(item).strip().lower() in {'http', 'https', 'socks4', 'socks5'}]
                if not protocols: protocols = re.findall(r'\b(?:https?|socks[45])\b', get_text_func(cells[5]).lower())
                anonymity = anonymity_map.get(get_text_func(cells[6]).lower(), '')
                proxy_info = ProxyInfo(source=self.source, protocol=random.choice(protocols), ip=ip, port=port, country_code=country_code, in_chinese_mainland=str(country_code).lower() in {'cn'}, anonymity=anonymity, delay=delay)
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies