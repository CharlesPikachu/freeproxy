'''
Function:
    Implementation of ProxyhubProxiedSession
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


'''ProxyhubProxiedSession'''
class ProxyhubProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(ProxyhubProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies
        url = 'https://proxyhub.me/'
        headers = {'User-Agent': generate_user_agent()}
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200: return self.candidate_proxies
        soup = BeautifulSoup(resp.text, 'lxml')
        soup = soup.select_one("div.list table.table")
        for tr in soup.select("tbody tr"):
            tds = tr.find_all("td")
            ip = tds[0].get_text(strip=True)
            port = tds[1].get_text(strip=True)
            ptype_raw = tds[2].get_text(strip=True).lower()
            formatted_proxy = f"{ptype_raw}://{ip}:{port}"
            self.candidate_proxies.append({
                'http': formatted_proxy, 'https': formatted_proxy
            })
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(ProxyhubProxiedSession().refreshproxies())