'''
Function:
    Implementation of JiliuipProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import json_repair
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''JiliuipProxiedSession'''
class JiliuipProxiedSession(BaseProxiedSession):
    source = 'JiliuipProxiedSession'
    homepage = 'https://www.jiliuip.com/free/page-1/'
    def __init__(self, **kwargs):
        super(JiliuipProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            'priority': 'u=0, i',
            'referer': 'https://www.jiliuip.com/free/page-1/',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                resp = session.get(f'https://www.jiliuip.com/free/page-{page}/', headers=self.getrandomheaders(headers_override=headers))
                resp.raise_for_status()
                soup, target_script = BeautifulSoup(resp.text, "html.parser"), None
                for script in soup.find_all("script"):
                    if script.string and "const fpsList" in script.string:
                        target_script: str = script.string
                        break
                m = re.search(r"const\s+fpsList\s*=\s*(\[[\s\S]*?\]);", target_script)
                json_text = m.group(1)
                fps_list = json_repair.loads(json_text)
            except:
                continue
            for item in fps_list:
                try:
                    proxy_info = ProxyInfo(
                        source=self.source, protocol='http', ip=item["ip"], port=item["port"], anonymity="elite", country_code="CN", in_chinese_mainland=True, delay=item["speed"],
                    )
                except:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies