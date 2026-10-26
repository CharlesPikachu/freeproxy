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
from urllib.parse import urljoin
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FloppyDataProxiedSession'''
class FloppyDataProxiedSession(BaseProxiedSession):
    source = 'FloppyDataProxiedSession'
    homepage = 'https://floppydata.com/free-proxy/'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(FloppyDataProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
        # obtain proxies
        (resp := session.get(self.homepage, headers=headers)).raise_for_status()
        script_src = re.search(r'<script\b[^>]*\bsrc=["\']([^"\']*FreeProxyList[^"\']*\.js)["\']', resp.text, re.IGNORECASE).group(1)
        (resp := session.get(urljoin(self.homepage, script_src), headers=headers)).raise_for_status()
        auth_var = re.search(r'\bAuthorization\s*:\s*(\w+)', resp.text).group(1)
        auth_code = re.search(rf'\b{auth_var}\s*=\s*["\']([^"\']+)["\']', resp.text).group(1)
        headers.update({'content-type': 'application/json', 'authorization': auth_code})
        (resp := session.get('https://geoxy.io/proxies?count=99999', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
        for item in resp.json():
            try: proxy_info = ProxyInfo(source=self.source, protocol=item["protocols"][0], ip=str(item["address"]).split(':')[0], port=str(item["address"]).split(':')[1], anonymity=item['anonymityLevel'], country_code=str(item["country"]).upper(), in_chinese_mainland=(str(item["country"]).upper() in {"CN"}), delay=float(str(item["ping"]).removesuffix('ms').strip()))
            except Exception: continue
            self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies