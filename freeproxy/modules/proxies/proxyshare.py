'''
Function:
    Implementation of ProxyShareProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import secrets
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''ProxyShareProxiedSession'''
class ProxyShareProxiedSession(BaseProxiedSession):
    endpoint = ''
    source = 'ProxyShareProxiedSession'
    homepage = 'https://www.proxyshare.com/zh/free-proxy/'
    def __init__(self, **kwargs):
        super(ProxyShareProxiedSession, self).__init__(**kwargs)
        self.client_hash = secrets.token_hex(16)
    '''resolveendpoint'''
    def resolveendpoint(self, session: requests.Session, headers: dict, force=False):
        # return cached endpoint
        if self.endpoint and not force: return self.endpoint
        # initialize
        self.endpoint, parse_aliases_func = '', lambda value: {(match.group(2) or match.group(1)): match.group(1) for item in value.split(',') if (match := re.fullmatch(r'\s*([A-Za-z_$][\w$]*)(?:\s+as\s+([A-Za-z_$][\w$]*))?\s*', item))}
        # obtain javascript assets
        (resp := session.get(self.homepage, headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); soup = BeautifulSoup(resp.text, 'lxml')
        asset_sources, asset_urls = {}, [urljoin(self.homepage, elem.get('src') or elem.get('href')) for elem in soup.select('script[src], link[rel="modulepreload"][href]') if str(elem.get('src') or elem.get('href', '')).split('?', 1)[0].endswith('.js')]
        for asset_url in dict.fromkeys(asset_urls):
            try: (resp := session.get(asset_url, headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); asset_sources[asset_url] = resp.text
            except Exception: continue
        # resolve endpoint
        for page_asset_url, page_source in list(asset_sources.items()):
            if 'lastChecked' not in page_source: continue
            for local_name in re.findall(r'\b([A-Za-z_$][\w$]*)\s*\(\s*\{[^{}]{0,1000}?sort_by\s*:\s*["\']lastChecked["\']', page_source):
                for imports, imported_asset in re.findall(r'import\{([^}]+)\}from["\']([^"\']+)["\']', page_source):
                    if not (exported_name := parse_aliases_func(imports).get(local_name)): continue
                    if (imported_asset_url := urljoin(page_asset_url, imported_asset)) not in asset_sources:
                        try: (resp := session.get(imported_asset_url, headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); asset_sources[imported_asset_url] = resp.text
                        except Exception: continue
                    for exports in re.findall(r'export\{([^}]+)\}', (imported_source := asset_sources[imported_asset_url])):
                        if not (internal_name := parse_aliases_func(exports).get(exported_name)): continue
                        if match := re.search(rf'\b{re.escape(internal_name)}\s*=\s*[^;]{{0,500}}?url\s*:\s*["\']([^"\']+)["\'][^;]{{0,300}}?method\s*:\s*["\']get["\']', imported_source, re.I): self.endpoint = urljoin(self.homepage, match.group(1)); return self.endpoint
        raise RuntimeError('Unable to resolve ProxyShare endpoint')
    '''getproxydata'''
    def getproxydata(self, session: requests.Session, endpoint: str, page: int, headers: dict):
        (resp := session.get(endpoint, params={'leaf': page, 'take': 1000, 'sort_by': 'lastChecked', 'sort_type': 'desc'}, headers=self.getrandomheaders(base_headers=headers))).raise_for_status()
        payload: dict = resp.json(); data = payload.get('content') or payload.get('data') or {}
        if not isinstance(data, dict): raise ValueError('Invalid ProxyShare response')
        return data
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, protocol_mapper, anonymity_mapper = [], requests.Session(), {1: 'http', 2: 'https', 4: 'socks4', 8: 'socks5'}, {0: 'transparent', 1: 'anonymous', 2: 'elite'}
        headers = {'accept': 'application/json, text/plain, */*', 'hash': self.client_hash, 'referer': self.homepage, 'ua-sec': 'https://www.proxyshare.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}
        try: endpoint = self.resolveendpoint(session, headers)
        except Exception: return self.candidate_proxies
        # obtain proxies
        for page in range(1, self.max_pages + 1):
            try: data = self.getproxydata(session, endpoint, page, headers)
            except Exception:
                try: endpoint = self.resolveendpoint(session, headers, force=True); data = self.getproxydata(session, endpoint, page, headers)
                except Exception: continue
            if not (data_items := data.get('list', [])): break
            for item in data_items:
                if not isinstance(item, dict): continue
                try:
                    country_code = str(item.get('country_code') or '').upper()
                    proxy_info = ProxyInfo(source=self.source, protocol=protocol_mapper[int(item['protocol'])], ip=str(item['ip']).strip(), port=int(item['port']), anonymity=anonymity_mapper[int(item['anonymity'])], country_code=country_code, in_chinese_mainland=(country_code in {'CN'}), delay=item.get('latency'))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
            if str(data.get('page_count', '')).isdigit() and page >= int(data['page_count']): break
        # return
        return self.candidate_proxies