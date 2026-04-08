'''
Function:
    Implementation of FloppyDataProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FloppyDataProxiedSession'''
class FloppyDataProxiedSession(BaseProxiedSession):
    source = 'FloppyDataProxiedSession'
    homepage = 'https://floppydata.com/free-proxy/'
    def __init__(self, **kwargs):
        super(FloppyDataProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        (resp := session.get('https://floppydata.com/free-proxy/', headers=headers)).raise_for_status()
        auth_code = re.compile(r"(['\"]?)Authorization\1\s*:\s*(['\"`])([^'\"`]+)\2", re.IGNORECASE).search(resp.text).group(3)
        headers.update({'content-type': 'application/json', 'authorization': auth_code})
        (resp := session.get('https://geoxy.io/proxies?count=99999', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
        for item in resp.json():
            try: proxy_info = ProxyInfo(source=self.source, protocol=item["protocols"][0], ip=str(item["address"]).split(':')[0], port=str(item["address"]).split(':')[1], anonymity=item['anonymityLevel'], country_code=str(item["country"]).upper(), in_chinese_mainland=(str(item["country"]).upper() in {"CN"}), delay=float(str(item["ping"]).removesuffix('ms').strip()))
            except Exception: continue
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies