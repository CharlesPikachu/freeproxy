'''
Function:
    Implementation of IP3366ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
try:
    from base import BaseProxiedSession
except:
    from .base import BaseProxiedSession


'''IP3366ProxiedSession'''
class IP3366ProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(IP3366ProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            url = f'http://www.ip3366.net/free/?stype=1&page={page}'
            headers = {'User-Agent': UserAgent().random}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200: continue
            soup = BeautifulSoup(resp.text, 'lxml')
            soup = soup.find('table', attrs={'class': 'table table-bordered table-striped'})
            for item in soup.find('tbody').find_all('tr'):
                formatted_proxy = f"{item.find_all('td')[3].text.strip().lower()}://{item.find_all('td')[0].text.strip()}:{item.find_all('td')[1].text.strip()}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # return
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(IP3366ProxiedSession().refreshproxies())