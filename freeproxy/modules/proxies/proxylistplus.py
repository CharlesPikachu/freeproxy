'''
Function:
    Implementation of ProxylistplusProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
try:
    from base import BaseProxiedSession
except:
    from .base import BaseProxiedSession


'''ProxylistplusProxiedSession'''
class ProxylistplusProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxylistplusProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            url = f'https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{page}'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml')
            for item in soup.find_all('tr', attrs={'class': 'cells'}):
                try:
                    item.find_all('td')[6].text.strip().lower()
                except:
                    continue
                if item.find_all('td')[6].text.strip().lower() == 'no':
                    formatted_proxy = f"http://{item.find_all('td')[1].text.strip()}:{item.find_all('td')[2].text.strip()}"
                else:
                    formatted_proxy = f"https://{item.find_all('td')[1].text.strip()}:{item.find_all('td')[2].text.strip()}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # return
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(ProxylistplusProxiedSession().refreshproxies())