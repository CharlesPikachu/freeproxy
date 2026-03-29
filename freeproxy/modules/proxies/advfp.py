'''
Function:
    Implementation of ADVFPProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import base64
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ADVFPProxiedSession'''
class ADVFPProxiedSession(BaseProxiedSession):
    source = 'ADVFPProxiedSession'
    homepage = 'https://advanced.name/freeproxy'
    def __init__(self, **kwargs):
        super(ADVFPProxiedSession, self).__init__(**kwargs)
    '''_b64decode'''
    def _b64decode(self, s: str):
        if not s: return None
        try: return base64.b64decode(s).decode("utf-8", errors="ignore")
        except Exception: return s
    '''_extractproxies'''
    def _extractproxies(self, html_text: str):
        PROTOCOLS, ANON_LEVELS = {"HTTP", "HTTPS", "SOCKS4", "SOCKS5"}, {"ANON", "ELITE", "TRANSPARENT"}
        rows, results = BeautifulSoup(html_text, "lxml").select("#table_proxies tbody tr"), []
        for tr in rows:
            if len((tds := tr.find_all("td", recursive=False))) < 7: continue
            ip, port, labels = self._b64decode(tds[1].get("data-ip")), self._b64decode(tds[2].get("data-port")), [a.get_text(strip=True).upper() for a in tds[3].select("a")]
            protocols, anon = [x.lower() for x in labels if x in PROTOCOLS], [{"ANON": "anonymous", "ELITE": "elite", "TRANSPARENT": "transparent"}.get(x) for x in labels if x in ANON_LEVELS]
            country_code = country_a.get_text(strip=True).upper() if (country_a := tds[4].select_one("a")) else None
            speed_text, last_checkup = tds[5].get_text(" ", strip=True), tds[6].get_text(" ", strip=True)
            results.append({"ip": ip, "port": int(port) if port and port.isdigit() else port, "protocols": protocols, "anonymity": anon[0] if anon else "", "country_code": country_code, "speed": int(speed_text) if speed_text.isdigit() else speed_text, "last_checkup": last_checkup})
        return results
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://advanced.name/freeproxy?page={page}', headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
            except Exception: continue
            for item in self._extractproxies(resp.text):
                try: proxy_info = ProxyInfo(source=self.source, ip=item['ip'], port=item['port'], protocol=random.choice(item['protocols']), delay=item['speed'], anonymity=item['anonymity'], country_code=item['country_code'], in_chinese_mainland=(item['country_code'] in {'CN'}))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies