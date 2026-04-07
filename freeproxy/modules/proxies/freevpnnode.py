'''
Function:
    Implementation of FreeVPNNodeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''FreeVPNNodeProxiedSession'''
class FreeVPNNodeProxiedSession(BaseProxiedSession):
    source = 'FreeVPNNodeProxiedSession'
    homepage = 'https://www.freevpnnode.com/free-proxy'
    def __init__(self, **kwargs):
        super(FreeVPNNodeProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "priority": "u=0, i", "referer": "https://www.freevpnnode.com/free-proxy/", 
            "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"', "upgrade-insecure-requests": "1", "sec-fetch-site": "same-origin", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.freevpnnode.com/free-proxy?page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
                table = BeautifulSoup(resp.text, "lxml").select_one("div.vpn-list table")
                columns, proxies = [th.get_text(" ", strip=True) for th in table.select("thead th")], []
                for tr in table.select("tbody tr"):
                    if not (tds := tr.find_all("td", recursive=False)): continue
                    row = [(img["data-text"].strip() if (img := td.find("img", attrs={"data-text": True})) and img.get("data-text") else " ".join(td.stripped_strings)) for td in tds]
                    proxies.append(dict(zip(columns, row)))
            except Exception: continue
            for item in proxies:
                try: proxy_info = ProxyInfo(source=self.source, protocol=item['Protocols'], ip=item['IP Address'], port=item['Port'], anonymity=str(item['Anonymity']).split(' ')[0], country_code=item['Country'], in_chinese_mainland=(item['Country'] in {'CN'}), delay=int(str(item["Latency"]).removesuffix(' ms').strip()))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies