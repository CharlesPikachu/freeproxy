'''
Function:
    Implementation of QiyunipProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''QiyunipProxiedSession'''
class QiyunipProxiedSession(BaseProxiedSession):
    source = 'QiyunipProxiedSession'
    homepage = 'https://www.qiyunip.com/freeProxy/1.html'
    def __init__(self, **kwargs):
        super(QiyunipProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session = [], requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Priority": "u=0, i",
            "Cookie": "SITE_TOTAL_ID=00bde4a9e753338419ac87060ab79cb0; server_name_session=da1f1107209e525945cda151baa4abac; Hm_lvt_b5a2bb0620d64e270273677db2ded096=1762700985,1763209661,1764723680; Hm_lpvt_b5a2bb0620d64e270273677db2ded096=1764723680; HMACCOUNT=E9868533209C5410",
            "Cache-Control": "max-age=0", "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"', "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try:
                (resp := session.get(f'https://www.qiyunip.com/freeProxy/{page}.html', headers=self.getrandomheaders(headers_override=headers))).raise_for_status()
                soup = BeautifulSoup(resp.text, 'lxml'); soup = soup.find('table', attrs={'id': 'proxyTable'}); trs = soup.find('tbody').find_all('tr')
            except Exception:
                continue
            for item in trs:
                try:
                    anonymity_cn = item.find_all('th')[2].text.strip()
                    if anonymity_cn == '普匿': anonymity = 'anonymous'
                    elif anonymity_cn == '高匿': anonymity = 'elite'
                    else: anonymity = 'transparent'
                    country_code = 'CN' if '中国' in item.find_all('th')[4].text.strip() else ""
                    delay = int(float(item.find_all('th')[5].text.strip()) * 1000)
                    proxy_info = ProxyInfo(source=self.source, protocol=item.find_all('th')[3].text.strip().lower(), ip=item.find_all('th')[0].text.strip(), port=item.find_all('th')[1].text.strip(), anonymity=anonymity, delay=delay, country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception:
                    continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies