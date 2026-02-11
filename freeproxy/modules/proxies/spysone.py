'''
Function:
    Implementation of SpysoneProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
import functools
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''SpysoneProxiedSession'''
class SpysoneProxiedSession(BaseProxiedSession):
    source = 'SpysoneProxiedSession'
    homepage = 'https://spys.one/en/free-proxy-list/'
    def __init__(self, **kwargs):
        super(SpysoneProxiedSession, self).__init__(**kwargs)
    '''extractspysproxies'''
    def extractspysproxies(self, html: str):
        soup, obf_script = BeautifulSoup(html, 'html.parser'), None
        for s in soup.find_all('script'):
            if s.string and "eval(function(p,r,o,x,y,s)" in s.string: obf_script = s.string; break
        if not obf_script: return []
        m = re.search(r"return p\}\('([^']+)',(\d+),(\d+),'([^']+)'\.split\('([^']*)'\),0,\{\}\)\)", obf_script)
        if not m: return []
        p_code, base, cnt, dict_str, sep = m.groups(); base, cnt = int(base), int(cnt); tokens = dict_str.split('^'); chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        y_func = lambda c, r, chars=chars: ((chr(c + 29) if c > 35 else chars[c]) if c < r else y_func(int(c / r), r) + (chr((s := (c % r)) + 29) if s > 35 else chars[s]))
        unpack_func = lambda p, r, c, k, y_func=y_func: functools.reduce(lambda acc, idx: (re.sub(r"\b%s\b" % re.escape(y_func(idx, r)), k[idx], acc) if k[idx] else acc), range(c - 1, -1, -1), p)
        decoded: str = unpack_func(p_code, base, cnt, tokens); env = {}; exec(decoded.replace(";", "\n"), {}, env)
        proxies = []; anonymity_map = {'NOA': 'transparent', 'ANM': 'anonymous', 'HIA': 'elite'}
        for row in soup.find_all('tr', onmouseover=True):
            tds = row.find_all('td')
            if len(tds) < 6: continue
            ip_font = tds[0].find('font', class_='spy14')
            if not ip_font or not ip_font.contents: continue
            ip = str(ip_font.contents[0]).strip(); script = tds[0].find('script')
            if not script or not script.string: continue
            pairs = re.findall(r'(\w+)\^(\w+)', script.string)
            if not pairs: continue
            port_digits = []
            for left, right in pairs: v1 = env[left] if left in env else int(left); v2 = env[right] if right in env else int(right); port_digits.append(str(v1 ^ v2))
            port = int("".join(port_digits)); type_text = tds[1].get_text(" ", strip=True).upper()
            if 'SOCKS5' in type_text: protocol = 'socks5'
            elif 'SOCKS4' in type_text or 'SOCKS ' in type_text: protocol = 'socks4'
            elif 'HTTPS' in type_text or 'SSL' in type_text: protocol = 'https'
            else: protocol = 'http'
            anonymity_raw = tds[2].get_text(strip=True); anonymity = anonymity_map.get(anonymity_raw, anonymity_raw); latency_text = tds[5].get_text(strip=True)
            try: delay_ms = int(float(latency_text.replace(',', '.')) * 1000)
            except ValueError: delay_ms = None
            proxies.append({"ip": ip, "port": port, "protocol": protocol, "anonymity": anonymity, "anonymity_raw": anonymity_raw, "delay_ms": delay_ms})
        return proxies
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        # obtain proxies
        try: (resp := session.get('https://spys.one/en/free-proxy-list/', headers=self.getrandomheaders(headers_override=headers))).raise_for_status(); soup = BeautifulSoup(resp.text, 'lxml'); rows = soup.find_all('tr', class_=re.compile(r'^spy1x{0,3}$'))
        except Exception: return self.candidate_proxies
        urls: list[str] = []
        for tr in rows:
            tds = tr.find_all('td')
            try: urls.append(f"https://spys.one{tds[3].find('a')['href']}")
            except Exception: continue
        urls: list[str] = list(set(urls))
        if not urls: return self.candidate_proxies
        for url in urls:
            try: (resp := session.get(url, headers=self.getrandomheaders(headers_override=headers))).raise_for_status(); results = self.extractspysproxies(resp.text)
            except Exception: continue
            country_code = urlparse(url).path.strip('/').split('/')[-1].upper()
            for result in results:
                proxy_info = ProxyInfo(source=self.source, ip=result['ip'], port=result['port'], protocol=result['protocol'], anonymity=result['anonymity'], delay=result['delay_ms'], country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies