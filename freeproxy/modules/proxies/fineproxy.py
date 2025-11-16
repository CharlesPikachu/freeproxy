'''
Function:
    Implementation of FineProxyProxiedSession
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
from bs4 import BeautifulSoup
from .base import BaseProxiedSession
from ..utils import ensurevalidrequestsproxies


'''FineProxyProxiedSession'''
class FineProxyProxiedSession(BaseProxiedSession):
    def __init__(self, **kwargs):
        super(FineProxyProxiedSession, self).__init__(**kwargs)
    '''refreshproxies'''
    @ensurevalidrequestsproxies
    def refreshproxies(self):
        # initialize
        self.candidate_proxies = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # obtain proxies
        for page in range(1, self.max_pages+1):
            data = {
                'action': 'proxylister_load_more', 'nonce': 'c17c69b379', 'page': f'{page}', 'atts[downloads]': 'true'
            }
            resp = requests.post('https://fineproxy.org/wp-admin/admin-ajax.php', headers=self.randomheaders(headers_override=headers), timeout=60, data=data)
            if resp.status_code != 200: return self.candidate_proxies
            resp.encoding = 'utf-8'
            rows = resp.json()['data']['rows']
            soup = BeautifulSoup(rows, 'html.parser')
            for row in soup.find_all('tr'):
                cells = row.find_all('td')
                if len(cells) < 4: continue
                ip, port, protocol = cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip()
                protocol = protocol.lower().split(',')[0].strip()
                self.candidate_proxies.append({'http': f"{protocol}://{ip}:{port}", 'https': f"{protocol}://{ip}:{port}"})
        # return
        return self.candidate_proxies