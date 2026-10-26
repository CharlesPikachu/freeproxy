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
from typing_extensions import Unpack
from .base import BaseProxiedSession, BaseProxiedSessionKwargs
from ..utils import filterinvalidproxies, applyfilterrule, ProxyInfo


'''QiyunipProxiedSession'''
class QiyunipProxiedSession(BaseProxiedSession):
    source = 'QiyunipProxiedSession'
    homepage = 'https://www.qiyunip.com/freeProxy/1.html'
    def __init__(self, **kwargs: Unpack[BaseProxiedSessionKwargs]):
        super(QiyunipProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @applyfilterrule()
    @filterinvalidproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies, session, headers = [], requests.Session(), {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        }; session.headers.update(headers)
        try: (resp := session.get('https://www.qiyunip.com/', timeout=10)).raise_for_status()
        except Exception: pass
        session.headers['Referer'] = 'https://www.qiyunip.com/'
        # obtain proxies
        for page in range(1, self.max_pages+1):
            try: (resp := session.get(f'https://www.qiyunip.com/freeProxy/{page}.html', headers=self.getrandomheaders(base_headers=headers))).raise_for_status(); trs = BeautifulSoup(resp.text, 'lxml').find('table', attrs={'id': 'proxyTable'}).find('tbody').find_all('tr')
            except Exception: continue
            for item in trs:
                try: anonymity = {'普匿': 'anonymous', '高匿': 'elite'}.get(str(item.find_all('th')[2].text).strip(), 'transparent'); country_code = 'CN' if '中国' in str(item.find_all('th')[4].text).strip() else ""; delay = int(float(str(item.find_all('th')[5].text).strip()) * 1000); proxy_info = ProxyInfo(source=self.source, protocol=item.find_all('th')[3].text.strip().lower(), ip=item.find_all('th')[0].text.strip(), port=item.find_all('th')[1].text.strip(), anonymity=anonymity, delay=delay, country_code=country_code, in_chinese_mainland=(country_code.lower() in ['cn']))
                except Exception: continue
                self.candidate_proxies.append(proxy_info)
        # return
        return self.candidate_proxies