'''initialize'''
from .base import BaseProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .zdaye import ZdayeProxiedSession
from .ip3366 import IP3366ProxiedSession
from .qiyunip import QiyunipProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .proxylistplus import ProxylistplusProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'IP89ProxiedSession': IP89ProxiedSession, 'ZdayeProxiedSession': ZdayeProxiedSession, 'IP3366ProxiedSession': IP3366ProxiedSession,
        'KuaidailiProxiedSession': KuaidailiProxiedSession, 'ProxylistplusProxiedSession': ProxylistplusProxiedSession, 'QiyunipProxiedSession': QiyunipProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build