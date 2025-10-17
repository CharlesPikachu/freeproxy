'''
Function:
    Implementation of ZdayeProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
try:
    from base import BaseProxiedSession
except:
    from .base import BaseProxiedSession


'''ZdayeProxiedSession'''
class ZdayeProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ZdayeProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        for page in range(1, self.max_pages+1):
            url = f'https://www.zdaye.com/free/{page}/'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml')
            soup = soup.find('table', attrs={'id': 'ipc'})
            for item in soup.find('tbody').find_all('tr'):
                port = item.find_all('td')[1].text.strip()
                port = re.findall(r'(\d+)', port)[0]
                if 'iyes' in str(item.find_all('td')[5]):
                    formatted_proxy = f"https://{item.find_all('td')[0].text.strip()}:{port}"
                else:
                    formatted_proxy = f"http://{item.find_all('td')[0].text.strip()}:{port}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # return
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(ZdayeProxiedSession().refreshproxies())