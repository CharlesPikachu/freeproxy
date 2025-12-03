'''
Function:
    Implementation of KxdailiProxiedSession
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


'''KxdailiProxiedSession'''
class KxdailiProxiedSession(BaseProxiedSession):
    source = 'KxdailiProxiedSession'
    homepage = 'http://www.kxdaili.com/dailiip.html'
    def __init__(self, **kwargs):
        super(KxdailiProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Cookie": "UCT=91530587; ASPSESSIONIDQSCRTQSS=OCNEDMKDPFHBHJPIHEILIBGE; __51cke__=; __tins__17751595=%7B%22sid%22%3A%201764712759101%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201764714579700%7D; __51laig__=2",
            "Host": "www.kxdaili.com",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://www.kxdaili.com/dailiip.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for base_url in ['http://www.kxdaili.com/dailiip/1/', 'http://www.kxdaili.com/dailiip/2/']:
            anonymity = 'elite' if base_url in ['http://www.kxdaili.com/dailiip/1/'] else 'anonymous'
            for page in (1, self.max_pages + 1):
                try:
                    resp = session.get(base_url + f'{page}.html', headers=self.getrandomheaders(headers_override=headers))
                    resp.raise_for_status()
                    parsed_html = etree.HTML(resp.content.decode('utf-8'))
                    table = parsed_html.xpath('//table')[0]
                    trs = table.xpath('.//tr')
                except:
                    continue
                for tr in trs[1:]:
                    try:
                        proxy_info = ProxyInfo(
                            source=self.source, protocol="".join(tr.xpath("./td[4]/text()")).strip().split(',')[0].lower(), 
                            ip="".join(tr.xpath("./td[1]/text()")).strip(), port="".join(tr.xpath("./td[2]/text()")).strip(), anonymity=anonymity, 
                            country_code='CN', in_chinese_mainland=True, delay=int(float(re.match(r"^(\d*\.?\d+)", "".join(tr.xpath("./td[5]/text()")).strip()).group(1)) * 1000)
                        )
                    except:
                        continue
                    self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies