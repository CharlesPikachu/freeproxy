'''
Function:
    Implementation of ProxiedSessionClient
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import copy
import random
import warnings
if __name__ == '__main__':
    from modules import BuildProxiedSession, ProxiedSessionBuilder, LoggerHandle, BaseProxiedSession
else:
    from .modules import BuildProxiedSession, ProxiedSessionBuilder, LoggerHandle, BaseProxiedSession
warnings.filterwarnings('ignore')


'''ProxiedSessionClient'''
class ProxiedSessionClient():
    def __init__(self, proxy_sources=['KuaidailiProxiedSession', 'IP3366ProxiedSession', 'QiyunipProxiedSession', 'Tomcat1235ProxiedSession', 'ProxydailyProxiedSession', 'SpysoneProxiedSession'], 
                 init_proxied_session_cfg={'max_pages': 1}, disable_print=False):
        # logger handle
        self.logger_handle = LoggerHandle()
        # proxied sessions 
        self.proxied_sessions = dict()
        if proxy_sources is None: proxy_sources = ProxiedSessionBuilder.REGISTERED_MODULES.keys()
        for source in proxy_sources:
            try:
                module_cfg = copy.deepcopy(init_proxied_session_cfg)
                module_cfg['type'] = source
                self.proxied_sessions[source] = BuildProxiedSession(module_cfg=module_cfg)
                candidate_proxies = self.proxied_sessions[source].refreshproxies()
                if len(candidate_proxies) < 1: self.proxied_sessions.pop(source)
            except Exception as err:
                self.logger_handle.error(f'{self.__class__.__name__}.__init__ >>> {source} (Error: {err})', disable_print=self.disable_print)
                if source in self.proxied_sessions: self.proxied_sessions.pop(source)
                continue
        # set attributes
        self.disable_print = disable_print
        self.proxy_sources = proxy_sources
        self.init_proxied_session_cfg = init_proxied_session_cfg
    '''get'''
    def get(self, url, **kwargs):
        while True:
            proxied_session: BaseProxiedSession = self.getrandomproxiedsession()[1]
            proxied_session.randomsetproxy()
            self.logger_handle.info(f'Getting {url} with proxy {proxied_session.proxies}.', disable_print=self.disable_print)
            resp = proxied_session.get(url, **kwargs)
            if resp.status_code == 200:
                return resp
            warnings_msg = f'invalid proxy {proxied_session.proxies}, auto switching to other proxies.'
            self.logger_handle.warning(f'{self.__class__.__name__}.get >>> {url} (Error: {warnings_msg})', disable_print=self.disable_print)
    '''post'''
    def post(self, url, **kwargs):
        while True:
            proxied_session: BaseProxiedSession = self.getrandomproxiedsession()[1]
            proxied_session.randomsetproxy()
            self.logger_handle.info(f'Posting {url} with proxy {proxied_session.proxies}.', disable_print=self.disable_print)
            resp = proxied_session.post(url, **kwargs)
            if resp.status_code == 200:
                return resp
            warnings_msg = f'invalid proxy {proxied_session.proxies}, auto switching to other proxies.'
            self.logger_handle.warning(f'{self.__class__.__name__}.post >>> {url} (Error: {warnings_msg})', disable_print=self.disable_print)
    '''getrandomproxy'''
    def getrandomproxy(self):
        proxied_session: BaseProxiedSession = random.choice(list(self.proxied_sessions.values()))
        return proxied_session.getrandomproxy()
    '''getrandomproxiedsession'''
    def getrandomproxiedsession(self):
        proxied_session_name = random.choice(list(self.proxied_sessions.keys()))
        return proxied_session_name, self.proxied_sessions[proxied_session_name]
    '''str'''
    def __str__(self):
        return 'Welcome to use freeproxy!\nYou can visit https://github.com/CharlesPikachu/freeproxy for more details.'


'''tests'''
if __name__ == '__main__':
    proxy_sources = ['KuaidailiProxiedSession']
    proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    resp = proxied_session_client.get('https://space.bilibili.com/406756145', headers=headers)
    print(resp.text)