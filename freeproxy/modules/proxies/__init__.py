'''initialize'''
from .base import BaseProxiedSession
from .scdn import SCDNProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .ip3366 import IP3366ProxiedSession
from .geonode import GeonodeProxiedSession
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
from .proxyelite import ProxyEliteProxiedSession
from .freeproxydb import FreeProxyDBProxiedSession
from .proxyscrape import ProxyScrapeProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'ProxiflyProxiedSession': ProxiflyProxiedSession, 'FreeproxylistProxiedSession': FreeproxylistProxiedSession, 'IP89ProxiedSession': IP89ProxiedSession, 'ProxyEliteProxiedSession': ProxyEliteProxiedSession,
        'IP3366ProxiedSession': IP3366ProxiedSession, 'KuaidailiProxiedSession': KuaidailiProxiedSession, 'KxdailiProxiedSession': KxdailiProxiedSession, 'ProxydailyProxiedSession': ProxydailyProxiedSession, 
        'ProxydbProxiedSession': ProxydbProxiedSession, 'ProxyhubProxiedSession': ProxyhubProxiedSession, 'ProxylistProxiedSession': ProxylistProxiedSession, 'QiyunipProxiedSession': QiyunipProxiedSession,
        'SpysoneProxiedSession': SpysoneProxiedSession, 'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession, 'DatabayProxiedSession': DatabayProxiedSession, 'FineProxyProxiedSession': FineProxyProxiedSession, 
        'IPLocateProxiedSession': IPLocateProxiedSession, 'JiliuipProxiedSession': JiliuipProxiedSession, 'TheSpeedXProxiedSession': TheSpeedXProxiedSession, 'GeonodeProxiedSession': GeonodeProxiedSession, 
        'FreeProxyDBProxiedSession': FreeProxyDBProxiedSession, 'ProxyScrapeProxiedSession': ProxyScrapeProxiedSession, 'SCDNProxiedSession': SCDNProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build