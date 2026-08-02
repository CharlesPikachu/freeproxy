'''
Function:
    Implementation of LitportProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import random
import requests
from lxml import etree
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''LitportProxiedSession'''
class LitportProxiedSession(BaseProxiedSession):
    source = 'LitportProxiedSession'
    homepage = 'https://litport.net/free-proxy'
    def __init__(self, **kwargs):
        super(LitportProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        get_text_func, self.candidate_proxies, session, page_signatures = lambda node: ' '.join(' '.join(node.itertext()).split()), [], requests.Session(), set()
        headers = {'referer': self.homepage, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: (resp := session.get(f'{self.homepage}?page={page}', headers=self.getrandomheaders(base_headers=headers), timeout=30)).raise_for_status(); html = etree.HTML(resp.text); assert html is not None
            except Exception: continue
            proxy_table, header_indexes = None, {}
            for table in html.xpath('//table'):
                headers_text = [get_text_func(item).strip().lower() for item in table.xpath('.//tr[1]/*[self::th or self::td]')]
                if not all(any(key in header for header in headers_text) for key in ['protocol', 'host', 'port']): continue
                proxy_table = table
                for index, header in enumerate(headers_text):
                    for key in ['protocol', 'host', 'port', 'country', 'anonymity', 'response']:
                        if key in header and key not in header_indexes: header_indexes[key] = index
                break
            if proxy_table is None or not all(key in header_indexes for key in ['protocol', 'host', 'port']): continue
            if not ((rows := proxy_table.xpath('.//tr[td]')), (page_signature := tuple(get_text_func(row) for row in rows[:3])))[0] or page_signature in page_signatures: break
            page_signatures.add(page_signature)
            for row in rows:
                if max(header_indexes.values()) >= len((cells := row.xpath('./td'))): continue
                host_text, port_text = get_text_func(cells[header_indexes['host']]), get_text_func(cells[header_indexes['port']])
                ip = ip_match.group(0) if (ip_match := re.search(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])', host_text)) else ''
                port = port_match.group(1) if (port_match := re.search(r'\b([1-9]\d{0,4})\b', port_text)) and int(port_match.group(1)) <= 65535 else ''
                if not ip or not port or any(int(part) > 255 for part in ip.split('.')): continue
                if not (protocols := list(dict.fromkeys(re.findall(r'\b(?:https?|socks[45])\b', get_text_func(cells[header_indexes['protocol']]).lower())))): continue
                country_text = get_text_func(cells[header_indexes['country']]) if 'country' in header_indexes else ''
                country_code = country_match.group(1).upper() if (country_match := re.search(r'\b([A-Za-z]{2})\b', country_text)) else ''
                anonymity_text = get_text_func(cells[header_indexes['anonymity']]).lower() if 'anonymity' in header_indexes else ''
                anonymity = 'elite' if 'elite' in anonymity_text or 'high' in anonymity_text else 'anonymous' if 'anon' in anonymity_text or 'medium' in anonymity_text else 'transparent' if 'transparent' in anonymity_text or 'low' in anonymity_text else ''
                response_text = get_text_func(cells[header_indexes['response']]) if 'response' in header_indexes else ''
                delay = int(delay_match.group(1).replace(',', '')) if (delay_match := re.search(r'(\d[\d,]*)\s*ms', response_text.lower())) else None
                proxy_info = ProxyInfo(source=self.source, protocol=random.choice(protocols), ip=ip, port=port, country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']), anonymity=anonymity, delay=delay)
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies