'''
Function:
    Implementation of ProxyNovaProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import base64
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyNovaProxiedSession'''
class ProxyNovaProxiedSession(BaseProxiedSession):
    source = 'ProxyNovaProxiedSession'
    homepage = 'https://www.proxynova.com/proxy-server-list/'
    def __init__(self, **kwargs):
        super(ProxyNovaProxiedSession, self).__init__(**kwargs)
    '''_jsiptotext'''
    def _jsiptotext(self, script_body: str) -> str:
        import quickjs
        m = re.search(r"document\.write\((.*)\)\s*;?\s*$", script_body.strip(), flags=re.S)
        if not m: return ""
        expr = m.group(1); ctx = quickjs.Context(); out = {"s": ""}
        ctx.add_callable("py_write", lambda x: out.__setitem__("s", out["s"] + str(x)))
        ctx.add_callable("py_atob", lambda s: base64.b64decode(s).decode("utf-8", errors="ignore"))
        ctx.eval("""var document = { write: function(x){ py_write(x); } }; function atob(s){ return py_atob(s); }""")
        ctx.eval(f"document.write({expr});")
        return out["s"].strip()
    '''_parserow'''
    def _parserow(self, tr: BeautifulSoup):
        tds = tr.find_all("td")
        if len(tds) < 7: return None
        # ip
        ip = ""; script = tds[0].find("script")
        if script and script.string: ip = self._jsiptotext(script.string)
        else: ip = tds[0].get_text(strip=True)
        # port
        port = tds[1].get_text(strip=True)
        # delay
        delay_text = tds[3].find("small").get_text(strip=True) if tds[3].find("small") else tds[3].get_text(strip=True)
        m = re.search(r"(\d+)\s*ms", delay_text.lower()); latency_ms = int(m.group(1)) if m else None
        # anonymity
        anonymity = str(tds[6].get_text(" ", strip=True)).lower()
        # country_code
        img, country_code = tds[5].find("img", class_=re.compile(r"\bflag\b")), None
        country_code = (next((c.split("-", 1)[1].upper() for c in img.get("class", []) if c.startswith("flag-") and len(c) == 7), None) or (img.get("alt") or "").upper() or None) if img else None
        # return
        proxy_info = ProxyInfo(source=self.source, protocol="http", ip=ip, port=port, anonymity=anonymity, country_code=country_code, in_chinese_mainland=(str(country_code).lower() in ['cn']), delay=latency_ms)
        return proxy_info
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        # obtain proxies
        try: (resp := session.get(f"https://www.proxynova.com/proxy-server-list/", headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
        except Exception: return self.candidate_proxies
        table = BeautifulSoup(resp.text, "lxml").select_one('table#tbl_proxy_list.table')
        if not table: return self.candidate_proxies
        for tr in table.select("tbody > tr"):
            item = self._parserow(tr)
            if item: self.candidate_proxies.append(item)
        # return
        return self.candidate_proxies