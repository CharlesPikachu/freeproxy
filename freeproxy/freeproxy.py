'''
Function:
    Implementation of ProxiedSessionClient
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import os
import json
import copy
import random
import warnings
from typing import Dict, List
if __name__ == '__main__':
    from modules import BuildProxiedSession, ProxiedSessionBuilder, LoggerHandle, BaseProxiedSession, ProxyInfo, touchdir
else:
    from .modules import BuildProxiedSession, ProxiedSessionBuilder, LoggerHandle, BaseProxiedSession, ProxyInfo, touchdir
warnings.filterwarnings('ignore')


'''ProxiedSessionClient'''
class ProxiedSessionClient():
    def __init__(self, proxy_sources: list = None, init_proxied_session_cfg: dict = None, disable_print: bool = False, max_tries: int = 5):
        # logger handle
        self.logger_handle = LoggerHandle()
        # proxied sessions
        self.proxied_sessions: Dict[str, BaseProxiedSession] = dict()
        if proxy_sources is None or not proxy_sources: proxy_sources = ProxiedSessionBuilder.REGISTERED_MODULES.keys()
        if init_proxied_session_cfg is None: init_proxied_session_cfg = dict(max_pages=1, logger_handle=self.logger_handle, disable_print=disable_print, filter_rule=None)
        for source in proxy_sources:
            try:
                module_cfg = copy.deepcopy(init_proxied_session_cfg)
                module_cfg['type'] = source
                self.proxied_sessions[source] = BuildProxiedSession(module_cfg=module_cfg)
                candidate_proxies = self.proxied_sessions[source].refreshproxies()
                if len(candidate_proxies) < 1: self.proxied_sessions.pop(source)
            except Exception as err:
                self.logger_handle.error(f'{self.__class__.__name__}.__init__ >>> {source} (Error: {err})', disable_print=disable_print)
                if source in self.proxied_sessions: self.proxied_sessions.pop(source)
                continue
        # set attributes
        self.max_tries = max_tries
        self.disable_print = disable_print
        self.proxy_sources = proxy_sources
        self.init_proxied_session_cfg = init_proxied_session_cfg
    '''get'''
    def get(self, url, **kwargs):
        for _ in range(self.max_tries):
            proxied_session: BaseProxiedSession = self.getrandomproxiedsession()[1]
            proxied_session.setrandomproxy()
            try:
                self.logger_handle.info(f'{self.__class__.__name__}.get >>> {url}, with proxy {proxied_session.proxies}.', disable_print=self.disable_print)
                resp = proxied_session.get(url, **kwargs)
                resp.raise_for_status()
                return resp
            except:
                warnings_msg = f'invalid proxy {proxied_session.proxies}, auto switching to other proxies.'
                self.logger_handle.warning(f'{self.__class__.__name__}.get >>> {url} (Error: {warnings_msg})', disable_print=self.disable_print)
                continue
    '''post'''
    def post(self, url, **kwargs):
        for _ in range(self.max_tries):
            proxied_session: BaseProxiedSession = self.getrandomproxiedsession()[1]
            proxied_session.setrandomproxy()
            try:
                self.logger_handle.info(f'{self.__class__.__name__}.post >>> {url}, with proxy {proxied_session.proxies}.', disable_print=self.disable_print)
                resp = proxied_session.post(url, **kwargs)
                resp.raise_for_status()
                return resp
            except:
                warnings_msg = f'invalid proxy {proxied_session.proxies}, auto switching to other proxies.'
                self.logger_handle.warning(f'{self.__class__.__name__}.post >>> {url} (Error: {warnings_msg})', disable_print=self.disable_print)
                continue
    '''getrandomproxy'''
    def getrandomproxy(self, proxy_format: str = 'requests'):
        for _ in range(self.max_tries):
            try:
                proxied_session: BaseProxiedSession = random.choice(list(self.proxied_sessions.values()))
                return proxied_session.getrandomproxy(proxy_format=proxy_format)
            except:
                continue
    '''savetojson'''
    def savetojson(self, save_path: dict = './free_proxies.json'):
        touchdir(os.path.dirname(save_path))
        free_proxies = {}
        for proxied_session_name, proxied_session in self.proxied_sessions.items():
            candidate_proxies: List[ProxyInfo] = proxied_session.candidate_proxies
            free_proxies[proxied_session_name] = [p.todict() for p in candidate_proxies]
        json.dump(free_proxies, open(save_path, 'w'), indent=2)
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
    init_proxied_session_cfg = {'filter_rule': {'country_code': 'CN'}}
    proxied_session_client = ProxiedSessionClient(proxy_sources=proxy_sources, init_proxied_session_cfg=init_proxied_session_cfg)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    resp = proxied_session_client.get('https://space.bilibili.com/406756145', headers=headers)
    print(resp.text)