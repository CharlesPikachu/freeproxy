'''
Function:
    太阳HTTP代理
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import requests
from .base import BaseProxy
from bs4 import BeautifulSoup


'''太阳HTTP代理'''
class TaiyanghttpProxy(BaseProxy):
    def __init__(self, **kwargs):
        super(TaiyanghttpProxy, self).__init__(**kwargs)
        self.http_proxies = []
        self.https_proxies = []
        self.http_https_proxies = []
    '''刷新代理'''
    def refreshproxies(self):
        # 初始化
        self.http_proxies = []
        self.https_proxies = []
        proxies_format = '{ip}:{port}'
        # 获得代理
        page = random.randint(1, 2)
        url = f'http://www.taiyanghttp.com/free/page{page}/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        soup = soup.find('div', attrs={'class': 'table'})
        for item in soup.find('div', attrs={'class': 'list'}).find_all('div', attrs={'class': 'tr ip_tr'}):
            ip = item.find_all('div')[0].text.strip()
            port = item.find_all('div')[1].text.strip()
            proxy_type = item.find_all('div')[5].text.strip()
            if proxy_type.lower() == 'http':
                self.http_proxies.append({'http': proxies_format.format(ip=ip, port=port)})
            else:
                self.https_proxies.append({'https': proxies_format.format(ip=ip, port=port)})
        self.http_https_proxies = self.http_proxies.copy() + self.https_proxies.copy()
        # 返回
        return self.http_proxies, self.https_proxies, self.http_https_proxies