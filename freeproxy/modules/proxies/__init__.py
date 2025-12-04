'''initialize'''
from .base import BaseProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .ihuan import IhuanProxiedSession
from .ip3366 import IP3366ProxiedSession
from .qiyunip import QiyunipProxiedSession
from .kxdaili import KxdailiProxiedSession
from .proxydb import ProxydbProxiedSession
from .spysone import SpysoneProxiedSession
from .databay import DatabayProxiedSession
from .jiliuip import JiliuipProxiedSession
from .iplocate import IPLocateProxiedSession
from .proxifly import ProxiflyProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .proxylist import ProxylistProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .fineproxy import FineProxyProxiedSession
from .thespeedx import TheSpeedXProxiedSession
from .tomcat1235 import Tomcat1235ProxiedSession
from .proxydaily import ProxydailyProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'ProxiflyProxiedSession': ProxiflyProxiedSession, 'FreeproxylistProxiedSession': FreeproxylistProxiedSession, 'IhuanProxiedSession': IhuanProxiedSession,
        'IP89ProxiedSession': IP89ProxiedSession, 'IP3366ProxiedSession': IP3366ProxiedSession, 'KuaidailiProxiedSession': KuaidailiProxiedSession,
        'KxdailiProxiedSession': KxdailiProxiedSession, 'ProxydailyProxiedSession': ProxydailyProxiedSession, 'ProxydbProxiedSession': ProxydbProxiedSession,
        'ProxyhubProxiedSession': ProxyhubProxiedSession, 'ProxylistProxiedSession': ProxylistProxiedSession, 'QiyunipProxiedSession': QiyunipProxiedSession,
        'SpysoneProxiedSession': SpysoneProxiedSession, 'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession, 'DatabayProxiedSession': DatabayProxiedSession,
        'FineProxyProxiedSession': FineProxyProxiedSession, 'IPLocateProxiedSession': IPLocateProxiedSession, 'JiliuipProxiedSession': JiliuipProxiedSession,
        'TheSpeedXProxiedSession': TheSpeedXProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build