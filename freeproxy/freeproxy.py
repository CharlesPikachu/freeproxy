'''
Function:
    免费代理获取工具
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import warnings
if __name__ == '__main__':
    from modules import *
else:
    from .modules import *
warnings.filterwarnings('ignore')


'''免费代理获取工具'''
class FreeProxy():
    def __init__(self, proxy_type='all', proxy_sources=None, init_session_cfg={}, logfilepath='freeproxy.log', **kwargs):
        # 代理类型
        assert proxy_type in ['all', 'http', 'https']
        self.proxy_type = proxy_type
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
                self.used_proxies[source] = self.supported_proxies[source](**init_session_cfg)
                self.used_proxies[source].refreshproxies()
        else:
            for source in proxy_sources:
                assert source in self.supported_proxies
                self.used_proxies[source] = self.supported_proxies[source](**init_session_cfg)
                self.used_proxies[source].refreshproxies()
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


'''test'''
if __name__ == '__main__':
    proxy_sources = ['proxylistplus', 'kuaidaili']
    proxy_session = FreeProxy(proxy_sources=proxy_sources)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = proxy_session.get('https://space.bilibili.com/406756145', headers=headers)
    print(response.text)