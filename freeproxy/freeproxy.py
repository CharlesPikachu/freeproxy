'''
Function:
    Implementation of FreeProxy
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import warnings
import requests
if __name__ == '__main__':
    from modules import BuildProxiedSession
else:
    from .modules import BuildProxiedSession
warnings.filterwarnings('ignore')


'''FreeProxy'''
class FreeProxy():
    def __init__(self, proxy_sources=None, init_session_cfg={}):
        # 支持的代理
        self.supported_proxies = {
            'yqie': YqieProxy,
            'ip89': IP89Proxy,
            'zdaye': ZdayeProxy,
            'ip3366': IP3366Proxy,
            'daili66': Daili66Proxy,
            'fatezero': FatezeroProxy,
            'kuaidaili': KuaidailiProxy,
            'seofangfa': SeofangfaProxy,
            'jiangxianli': JiangxianliProxy,
            'taiyanghttp': TaiyanghttpProxy,
            'proxylistplus': ProxylistplusProxy,
        }
        # 设置代理源
        self.used_proxies = {}
        if proxy_sources is None:
            for source in self.supported_proxies:
                try:
                    self.used_proxies[source] = self.supported_proxies[source](**init_session_cfg)
                    self.used_proxies[source].refreshproxies()
                except:
                    if source in self.used_proxies: self.used_proxies.pop(source)
                    continue
        else:
            for source in proxy_sources:
                try:
                    assert source in self.supported_proxies
                    self.used_proxies[source] = self.supported_proxies[source](**init_session_cfg)
                    self.used_proxies[source].refreshproxies()
                except:
                    if source in self.used_proxies: self.used_proxies.pop(source)
                    continue
        # session初始化配置文件
        self.init_session_cfg = init_session_cfg
        # logger handle
        self.logger_handle = None
        if logfilepath is not None: self.logger_handle = Logger(logfilepath)
    '''get请求'''
    def get(self, url, **kwargs):
        while True:
            session_name = random.choice(list(self.used_proxies.keys()))
            session = self.used_proxies[session_name]
            session.setproxy(proxy_type=self.proxy_type)
            if self.logger_handle is not None: self.logger_handle.info(f'正在使用代理{session.proxies}')
            response = session.get(url, **kwargs)
            if response.status_code == 200: break
            if self.logger_handle is not None: self.logger_handle.info(f'代理{session.proxies}无效')
        return response
    '''post请求'''
    def post(self, url, **kwargs):
        while True:
            session_name = random.choice(list(self.used_proxies.keys()))
            session = self.used_proxies[session_name]
            session.setproxy(proxy_type=self.proxy_type)
            if self.logger_handle is not None: self.logger_handle.info(f'正在使用代理{session.proxies}')
            response = session.post(url, **kwargs)
            if response.status_code == 200: break
            if self.logger_handle is not None: self.logger_handle.info(f'代理{session.proxies}无效')
        return response
    '''随机获得一个代理'''
    def getrandomproxy(self):
        session_name = random.choice(list(self.used_proxies.keys()))
        session = self.used_proxies[session_name]
        session.setproxy(proxy_type=self.proxy_type)
        return session.proxies
    '''随机获得一个设置了代理的session'''
    def getrandomproxysession(self):
        session = requests.Session()
        session.proxies = self.getrandomproxy()
        return session
    '''str'''
    def __str__(self):
        return 'Welcome to use freeproxy!\nYou can visit https://github.com/CharlesPikachu/freeproxy for more details.'


'''test'''
if __name__ == '__main__':
    proxy_sources = ['proxylistplus', 'kuaidaili']
    proxy_session = FreeProxy(proxy_sources=proxy_sources)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = proxy_session.get('https://space.bilibili.com/406756145', headers=headers)
    print(response.text)