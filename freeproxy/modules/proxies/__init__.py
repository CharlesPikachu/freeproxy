'''initialize'''
from .base import BaseProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .zdaye import ZdayeProxiedSession
from .ip3366 import IP3366ProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .proxylistplus import ProxylistplusProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'BaseProxiedSession': BaseProxiedSession, 'IP89ProxiedSession': IP89ProxiedSession,
        'ZdayeProxiedSession': ZdayeProxiedSession, 'IP3366ProxiedSession': IP3366ProxiedSession,
        'KuaidailiProxiedSession': KuaidailiProxiedSession, 'ProxylistplusProxiedSession': ProxylistplusProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build