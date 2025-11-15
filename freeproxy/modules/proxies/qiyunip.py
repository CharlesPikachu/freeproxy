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
from ..utils import ensurevalidrequestsproxies


'''QiyunipProxiedSession'''
class QiyunipProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(QiyunipProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            resp = requests.get(f'https://www.qiyunip.com/freeProxy/{page}.html', headers=self.randomheaders())
            if resp.status_code != 200: continue
            soup = BeautifulSoup(resp.text, 'lxml')
            soup = soup.find('table', attrs={'id': 'proxyTable'})
            for item in soup.find('tbody').find_all('tr'):
                try:
                    formatted_proxy = f"{item.find_all('th')[3].text.strip().lower()}://{item.find_all('th')[0].text.strip()}:{item.find_all('th')[1].text.strip()}"
                except:
                    continue
                self.candidate_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})
        # return
        return self.candidate_proxies