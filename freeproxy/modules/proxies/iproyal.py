'''
Function:
    Implementation of IPRoyalProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import pycountry
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''IPRoyalProxiedSession'''
class IPRoyalProxiedSession(BaseProxiedSession):
    source = 'IPRoyalProxiedSession'
    homepage = 'https://iproyal.com/free-proxy-list/'
    def __init__(self, **kwargs):
        super(IPRoyalProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
        (resp := session.get('https://iproyal.com/_astro/FreeProxyListTable.CHEnT7E3.js', headers=headers, timeout=60)).raise_for_status()
        headers['Authorization'] = re.search(r'Authorization:\s*(["\'])(.*?)\1', resp.text).group(2)
        # obtain proxies
        for page in range(1, self.max_pages+1):
            params = {"fields[0]": "ip", "fields[1]": "port", "fields[2]": "protocol", "fields[3]": "country", "fields[4]": "city", "pagination[page]": page, "pagination[pageSize]": 100}
            try: (resp := session.get('https://cms.iproyal.com/api/free-proxy-records', headers=self.getrandomheaders(base_headers=headers), params=params, timeout=60)).raise_for_status(); data_items = resp.json()['data']
            except Exception: continue
            for item in data_items:
                if not isinstance(item, dict): continue
                try: country_code = str(pycountry.countries.lookup(str(item['country'])).alpha_2)
                except Exception: country_code = ''
                try: proxy_info = ProxyInfo(source=self.source, ip=item['ip'], port=item['port'], protocol=item['protocol'], delay=None, anonymity="", country_code=country_code.upper(), in_chinese_mainland=(country_code.lower() in {'cn'}))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies