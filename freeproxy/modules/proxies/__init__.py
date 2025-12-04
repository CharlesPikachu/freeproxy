'''initialize'''
from .base import BaseProxiedSession
from ..utils import BaseModuleBuilder
from .proxydb import ProxydbProxiedSession
from .spysone import SpysoneProxiedSession
from .proxifly import ProxiflyProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .proxylist import ProxylistProxiedSession
from .tomcat1235 import Tomcat1235ProxiedSession
from .proxydaily import ProxydailyProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'ProxiflyProxiedSession': ProxiflyProxiedSession, 'FreeproxylistProxiedSession': FreeproxylistProxiedSession,
        'ProxydailyProxiedSession': ProxydailyProxiedSession, 'ProxydbProxiedSession': ProxydbProxiedSession,
        'ProxyhubProxiedSession': ProxyhubProxiedSession, 'ProxylistProxiedSession': ProxylistProxiedSession,
        'SpysoneProxiedSession': SpysoneProxiedSession, 'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession, 
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build