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
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''SpysoneProxiedSession'''
class SpysoneProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(SpysoneProxiedSession, self).__init__(**kwargs)
    '''_buildvaluemap'''
    def _buildvaluemap(self, soup: BeautifulSoup):
        val = {}
        for sc in soup.find_all('script', attrs={'type': 'text/javascript'}):
            txt = (sc.string or '').replace('\n', '').replace('\r', '')
            if not (re.search(r'=\d+;', txt) and '^' in txt): continue
            for name, num in re.findall(r'([a-z0-9]{3,})=(\d+);', txt):
                val[name] = int(num)
            for name, num, other in re.findall(r'([a-z0-9]{3,})=(\d+)\^([a-z0-9]{3,});', txt):
                if other in val: val[name] = int(num) ^ val[other]
            if val: return val
        return val
    '''_decodeportfromcell'''
    def _decodeportfromcell(self, td: BeautifulSoup, valmap: dict):
        sc = td.find('script')
        if not sc or not sc.string: return ''
        expr = sc.string
        pairs = re.findall(r'\((\w+)\^(\w+)\)', expr)
        digits = []
        for a, b in pairs:
            va, vb = valmap.get(a), valmap.get(b)
            if va is None or vb is None: return ''
            digits.append(str(va ^ vb))
        return ''.join(digits)
    '''_firsttextbeforescript'''
    def _firsttextbeforescript(self, font_tag: BeautifulSoup):
        for s in font_tag.strings:
            s = s.strip()
            if s: return s
        return ''
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }
        # obtain proxies
        resp = requests.get('https://spys.one/en/free-proxy-list/', headers=self.randomheaders(headers_override=headers))
        if resp.status_code != 200: return self.candidate_proxies
        soup = BeautifulSoup(resp.text, 'lxml')
        valmap = self._buildvaluemap(soup)
        rows = soup.find_all('tr', class_=re.compile(r'^spy1x{0,3}$'))
        for tr in rows:
            tds = tr.find_all('td')
            if len(tds) < 2: continue
            ip_font = tds[0].find('font', class_='spy14')
            if not ip_font: continue
            ip = self._firsttextbeforescript(ip_font)
            port = self._decodeportfromcell(tds[0], valmap)
            if not ip or not port: continue
            proto_font = tds[1].find('font', class_='spy1')
            protocol = (proto_font.get_text(strip=True).lower() if proto_font else '').strip()
            if not protocol: continue
            self.candidate_proxies.append({'http': f"{protocol}://{ip}:{port}", 'https': f"{protocol}://{ip}:{port}"})
        # return
        return self.candidate_proxies