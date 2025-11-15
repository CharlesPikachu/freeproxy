'''
Function:
    Implementation of IP89ProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import re
import requests
try:
    from base import BaseProxiedSession
except:
    from .base import BaseProxiedSession


'''IP89ProxiedSession'''
class IP89ProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(IP89ProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        octet = r'(?:25[0-5]|2[0-4]\d|1?\d?\d)'
        port  = r'(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3})'
        PATTERN = re.compile(rf'^{octet}\.{octet}\.{octet}\.{octet}:{port}$')
        # obtain proxies
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Referer": "https://www.89ip.cn/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        params = {"api": "1", "num": "200", "port": "", "address": "", "isp": ""}
        resp = requests.get('https://api.89ip.cn/tqdl.html', params=params, headers=headers)
        if resp.status_code != 200: return self.candidate_proxies
        for item in resp.text.split('<br>'):
            if PATTERN.fullmatch(item.strip()) is None: continue
            self.candidate_proxies.append({
                'http': f"http://{item}", 'https': f"http://{item}",
            })
        # return
        return self.candidate_proxies


'''tests'''
if __name__ == '__main__':
    print(IP89ProxiedSession().refreshproxies())