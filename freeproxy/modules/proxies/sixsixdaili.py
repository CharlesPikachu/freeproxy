'''
Function:
    Implementation of SixSixDailiProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''SixSixDailiProxiedSession'''
class SixSixDailiProxiedSession(BaseProxiedSession):
    source = 'SixSixDailiProxiedSession'
    def __init__(self, **kwargs):
        super(SixSixDailiProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            # --https
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%AB%98%E5%8C%BF&protocol=HTTPS&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='https', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="elite"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E6%99%AE%E5%8C%BF&protocol=HTTPS&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='https', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="anonymous"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%80%8F%E6%98%8E&protocol=HTTPS&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='https', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="transparent"))
            except Exception: pass
            # --http
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%AB%98%E5%8C%BF&protocol=HTTP&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='http', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="elite"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E6%99%AE%E5%8C%BF&protocol=HTTP&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='http', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="anonymous"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%80%8F%E6%98%8E&protocol=HTTP&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='http', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="transparent"))
            except Exception: pass
            # --socks4
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%AB%98%E5%8C%BF&protocol=Socks4&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks4', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="elite"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E6%99%AE%E5%8C%BF&protocol=Socks4&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks4', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="anonymous"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%80%8F%E6%98%8E&protocol=Socks4&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks4', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="transparent"))
            except Exception: pass
            # --socks5
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%AB%98%E5%8C%BF&protocol=Socks5&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks5', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="elite"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E6%99%AE%E5%8C%BF&protocol=Socks5&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks5', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="anonymous"))
            except Exception: pass
            try:
                (resp := session.get(f'http://api.66daili.com//?num=60&anonymity=%E9%80%8F%E6%98%8E&protocol=Socks5&format=json&page={page}', headers=self.getrandomheaders(headers_override=headers), timeout=60)).raise_for_status()
                for item in resp.json()['data']: self.candidate_proxies.append(ProxyInfo(source=self.source, protocol='socks5', ip=item['ip'], port=item['port'], country_code="CN", in_chinese_mainland=True, anonymity="transparent"))
            except Exception: pass
        # return
        return self.candidate_proxies