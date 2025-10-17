'''
Function:
    Implementation of KuaidailiProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
from user_agent import generate_user_agent
try:
    from base import BaseProxiedSession
except:
    from .base import BaseProxiedSession


'''KuaidailiProxiedSession'''
class KuaidailiProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(KuaidailiProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        # obtain proxies: 'https://www.kuaidaili.com/free/inha/1/'
        for page in range(1, self.max_pages+1):
            url = f'https://www.kuaidaili.com/free/inha/{page}/'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200: continue
            proxies = re.findall(r'const fpsList = (\[.*?\]);', resp.text)
            if len(proxies) < 1: continue
            proxies = eval(proxies[0])
            for proxy in proxies:
                formatted_proxy = f"http://{proxy['ip']}:{proxy['port']}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # obtain proxies: 'https://www.kuaidaili.com/free/dps/1/'
        for page in range(1, self.max_pages+1):
            url = f'https://www.kuaidaili.com/free/dps/{page}/'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200: continue
            proxies = re.findall(r'const fpsList = (\[.*?\]);', resp.text)
            if len(proxies) < 1: continue
            proxies = eval(proxies[0].replace('true', 'True').replace('false', 'False'))
            for proxy in proxies:
                formatted_proxy = f"http://{proxy['ip']}:{proxy['port']}"
                if not proxy['is_valid']: continue
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # obtain proxies: 'https://www.kuaidaili.com/free/intr/1/'
        for page in range(1, self.max_pages+1):
            url = f'https://www.kuaidaili.com/free/inha/{page}/'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200: continue
            proxies = re.findall(r'const fpsList = (\[.*?\]);', resp.text)
            if len(proxies) < 1: continue
            proxies = eval(proxies[0])
            for proxy in proxies:
                formatted_proxy = f"http://{proxy['ip']}:{proxy['port']}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # obtain proxies: 'https://www.kuaidaili.com/free/fps/1/'
        for page in range(1, self.max_pages+1):
            url = f'https://www.kuaidaili.com/free/fps/{page}/'
            headers = {'User-Agent': generate_user_agent()}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200: continue
            proxies = re.findall(r'const fpsList = (\[.*?\]);', resp.text)
            if len(proxies) < 1: continue
            proxies = eval(proxies[0])
            for proxy in proxies:
                formatted_proxy = f"http://{proxy['ip']}:{proxy['port']}"
                self.candidate_proxies.append({
                    'http': formatted_proxy, 'https': formatted_proxy
                })
        # return
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(KuaidailiProxiedSession().refreshproxies())