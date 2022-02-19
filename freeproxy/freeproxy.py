'''
Function:
    免费代理获取工具
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import warnings
if __name__ == '__main__':
    from modules import *
else:
    from .modules import *
warnings.filterwarnings('ignore')


'''免费代理获取工具'''
class FreeProxy():
    def __init__(self, proxy_type='all', proxy_sources=None, init_session_cfg={}, **kwargs):
        # 代理类型
        assert proxy_type in ['all', 'http', 'https']
        self.proxy_type = proxy_type
        # 支持的代理
        self.supported_proxies = {
            'ip3366': IP3366Proxy,
            'kuaidaili': KuaidailiProxy,
            'jiangxianli': JiangxianliProxy,
        }
        # 设置代理源
        if proxy_sources is None:
            self.used_proxies = self.supported_proxies
        else:
            self.used_proxies = {}
            for source in proxy_sources:
                assert source in self.supported_proxies
                self.used_proxies[source] = self.supported_proxies[source]
        # session初始化配置文件
        self.init_session_cfg = init_session_cfg
    '''get请求'''
    def get(self, url):
        pass
    '''post请求'''
    def post(self, url):
        pass


'''test'''
if __name__ == '__main__':
    proxy = JiangxianliProxy()
    print(proxy.refreshproxies())