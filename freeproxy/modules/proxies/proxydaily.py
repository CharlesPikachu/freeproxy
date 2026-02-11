'''
Function:
    Implementation of ProxydailyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import time
import random
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxydailyProxiedSession'''
class ProxydailyProxiedSession(BaseProxiedSession):
    source = 'ProxydailyProxiedSession'
    homepage = 'https://proxy-daily.com/'
    def __init__(self, **kwargs):
        super(ProxydailyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Cache-Control": "max-age=0", "Priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            params = {
                "draw": f"{page}", "columns[0][data]": "ip", "columns[0][name]": "ip", "columns[0][searchable]": "true", "columns[0][orderable]": "false", "columns[0][search][value]": "", "columns[0][search][regex]": "false", "columns[1][data]": "port", "columns[1][name]": "port",
                "columns[1][searchable]": "true", "columns[1][orderable]": "false", "columns[1][search][value]": "", "columns[1][search][regex]": "false", "columns[2][data]": "protocol", "columns[2][name]": "protocol", "columns[2][searchable]": "true", "columns[2][orderable]": "false",
                "columns[2][search][value]": "", "columns[2][search][regex]": "false", "columns[3][data]": "speed", "columns[3][name]": "speed", "columns[3][searchable]": "true", "columns[3][orderable]": "false", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
                "columns[4][data]": "anonymity", "columns[4][name]": "anonymity", "columns[4][searchable]": "true", "columns[4][orderable]": "false", "columns[4][search][value]": "", "columns[4][search][regex]": "false", "columns[5][data]": "country", "columns[5][name]": "country",
                "columns[5][searchable]": "true", "columns[5][orderable]": "false", "columns[5][search][value]": "", "columns[5][search][regex]": "false", "start": f"{(page - 1) * 100}", "length": "100", "search[value]": "", "search[regex]": "false", "_": f"{int(time.time() * 1000)}"
            }
            try: (resp := session.get('https://proxy-daily.com/api/serverside/proxies', headers=self.getrandomheaders(headers_override=headers), params=params)).raise_for_status(); data_items = resp.json()['data']
            except Exception: continue
            for item in data_items:
                try: protocol = random.choice(item['protocol'].split(',')); proxy_info = ProxyInfo(source=self.source, protocol=protocol.strip().lower(), ip=item['ip'], port=item['port'], anonymity=item['anonymity'].lower(), country_code=item['country'], delay=item['speed'], in_chinese_mainland=(item['country'].lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies