'''initialize'''
from .base import BaseProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .ip3366 import IP3366ProxiedSession
from .qiyunip import QiyunipProxiedSession
from .spysone import SpysoneProxiedSession
from .proxydb import ProxydbProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .proxydaily import ProxydailyProxiedSession
from .tomcat1235 import Tomcat1235ProxiedSession
from .proxylistplus import ProxylistplusProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'IP89ProxiedSession': IP89ProxiedSession, 'IP3366ProxiedSession': IP3366ProxiedSession, 'KuaidailiProxiedSession': KuaidailiProxiedSession, 
        'ProxylistplusProxiedSession': ProxylistplusProxiedSession, 'QiyunipProxiedSession': QiyunipProxiedSession, 'ProxydailyProxiedSession': ProxydailyProxiedSession,
        'ProxyhubProxiedSession': ProxyhubProxiedSession, 'ProxydbProxiedSession': ProxydbProxiedSession, 'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession,
        'SpysoneProxiedSession': SpysoneProxiedSession, 'FreeproxylistProxiedSession': FreeproxylistProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build