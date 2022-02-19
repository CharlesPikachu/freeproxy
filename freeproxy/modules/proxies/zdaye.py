'''
Function:
    站大爷代理
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import re
import requests
from .base import BaseProxy
from bs4 import BeautifulSoup


'''站大爷代理'''
class ZdayeProxy(BaseProxy):
    def __init__(self, **kwargs):
        super(ZdayeProxy, self).__init__(**kwargs)
        self.http_proxies = []
        self.https_proxies = []
        self.http_https_proxies = []
    '''刷新代理'''
    def refreshproxies(self):
        # 初始化
        self.http_proxies = []
        self.https_proxies = []
        proxies_format = '{ip}:{port}'
        # 获得代理链接
        url = 'https://www.zdaye.com/dayProxy/1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        index = re.findall(r'/dayProxy/ip/(\d*?).html', response.text)[0]
        url = f'https://www.zdaye.com/dayProxy/ip/{index}.html'
        # 获得代理
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        soup = soup.find('table', attrs={'id': 'ipc'})
        for item in soup.find('tbody').find_all('tr'):
            ip = item.find_all('td')[0].text.strip()
            port = item.find_all('td')[1].text.strip()
            proxy_type = item.find_all('td')[2].text.strip()
            port = re.findall(r'(\d+)', port)[0]
            if proxy_type.lower() == 'http':
                self.http_proxies.append({'http': proxies_format.format(ip=ip, port=port)})
            else:
                self.https_proxies.append({'https': proxies_format.format(ip=ip, port=port)})
        self.http_https_proxies = self.http_proxies.copy() + self.https_proxies.copy()
        # 返回
        return self.http_proxies, self.https_proxies, self.http_https_proxies