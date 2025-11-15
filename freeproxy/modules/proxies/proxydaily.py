'''
Function:
    Implementation of ProxydailyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import time
import requests
from fake_useragent import UserAgent
from .base import BaseProxiedSession


'''ProxydailyProxiedSession'''
class ProxydailyProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxydailyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            params = {
                "draw": f"{page}", "columns[0][data]": "ip", "columns[0][name]": "ip", "columns[0][searchable]": "true", "columns[0][orderable]": "false",
                "columns[0][search][value]": "", "columns[0][search][regex]": "false", "columns[1][data]": "port", "columns[1][name]": "port",
                "columns[1][searchable]": "true", "columns[1][orderable]": "false", "columns[1][search][value]": "", "columns[1][search][regex]": "false",
                "columns[2][data]": "protocol", "columns[2][name]": "protocol", "columns[2][searchable]": "true", "columns[2][orderable]": "false",
                "columns[2][search][value]": "", "columns[2][search][regex]": "false", "columns[3][data]": "speed", "columns[3][name]": "speed",
                "columns[3][searchable]": "true", "columns[3][orderable]": "false", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
                "columns[4][data]": "anonymity", "columns[4][name]": "anonymity", "columns[4][searchable]": "true", "columns[4][orderable]": "false",
                "columns[4][search][value]": "", "columns[4][search][regex]": "false", "columns[5][data]": "country", "columns[5][name]": "country",
                "columns[5][searchable]": "true", "columns[5][orderable]": "false", "columns[5][search][value]": "", "columns[5][search][regex]": "false",
                "start": f"{(page - 1) * 10}", "length": "10", "search[value]": "", "search[regex]": "false", "_": f"{int(time.time() * 1000)}"
            }
            resp = requests.get('https://proxy-daily.com/api/serverside/proxies', headers={'User-Agent': UserAgent().random}, params=params)
            if resp.status_code != 200: continue
            for item in resp.json().get('data', []):
                formatted_proxy = f"{item['protocol'].lower()}://{item['ip']}:{item['port']}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # return
        return self.candidate_proxies