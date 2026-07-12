'''initialize'''
from .base import BaseProxiedSession
from .scdn import SCDNProxiedSession
from .hide import HideProxiedSession
from .ip89 import IP89ProxiedSession
from ..utils import BaseModuleBuilder
from .advfp import ADVFPProxiedSession
from .spysme import SpysMeProxiedSession
from .ip3366 import IP3366ProxiedSession
from .geonix import GeonixProxiedSession
from .myproxy import MyProxyProxiedSession
from .goodips import GoodIPSProxiedSession
from .geonode import GeonodeProxiedSession
from .qiyunip import QiyunipProxiedSession
from .kxdaili import KxdailiProxiedSession
from .proxydb import ProxydbProxiedSession
from .spysone import SpysoneProxiedSession
from .databay import DatabayProxiedSession
from .jiliuip import JiliuipProxiedSession
from .iproyal import IPRoyalProxiedSession
from .pubproxy import PubProxyProxiedSession
from .iplocate import IPLocateProxiedSession
from .proxifly import ProxiflyProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .fineproxy import FineProxyProxiedSession
from .thespeedx import TheSpeedXProxiedSession
from .proxynova import ProxyNovaProxiedSession
from .sockslist import SocksListProxiedSession
from .proxiware import ProxiwareProxiedSession
from .proxybros import ProxybrosProxiedSession
from .proxyspace import ProxySpaceProxiedSession
from .floppydata import FloppyDataProxiedSession
from .trustytech import TrustyTechProxiedSession
from .proxydaily import ProxydailyProxiedSession
from .proxyelite import ProxyEliteProxiedSession
from .dpangestuw import DpangestuwProxiedSession
from .proxyshare import ProxyShareProxiedSession
from .chillyproxy import ChillyProxyProxiedSession
from .freeproxydb import FreeProxyDBProxiedSession
from .proxyscrape import ProxyScrapeProxiedSession
from .sixsixdaili import SixSixDailiProxiedSession
from .freevpnnode import FreeVPNNodeProxiedSession
from .proxyverity import ProxyVerityProxiedSession
from .roundproxies import RoundProxiesProxiedSession
from .openproxylist import OpenProxyListProxiedSession
from .freeproxylist import FreeproxylistProxiedSession
from .proxyfreeonly import ProxyFreeOnlyProxiedSession
from .freeproxyworld import FreeProxyWorldProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'ProxiflyProxiedSession': ProxiflyProxiedSession,             'FreeproxylistProxiedSession': FreeproxylistProxiedSession,    'IP89ProxiedSession': IP89ProxiedSession,                  'ProxyEliteProxiedSession': ProxyEliteProxiedSession,            'IP3366ProxiedSession': IP3366ProxiedSession,            'KuaidailiProxiedSession': KuaidailiProxiedSession,       'KxdailiProxiedSession': KxdailiProxiedSession, 
        'ProxydailyProxiedSession': ProxydailyProxiedSession,         'ProxydbProxiedSession': ProxydbProxiedSession,                'ProxyhubProxiedSession': ProxyhubProxiedSession,          'ProxybrosProxiedSession': ProxybrosProxiedSession,              'QiyunipProxiedSession': QiyunipProxiedSession,          'SpysoneProxiedSession': SpysoneProxiedSession,           'HideProxiedSession': HideProxiedSession,
        'DatabayProxiedSession': DatabayProxiedSession,               'FineProxyProxiedSession': FineProxyProxiedSession,            'IPLocateProxiedSession': IPLocateProxiedSession,          'JiliuipProxiedSession': JiliuipProxiedSession,                  'TheSpeedXProxiedSession': TheSpeedXProxiedSession,      'GeonodeProxiedSession': GeonodeProxiedSession,           'FreeProxyDBProxiedSession': FreeProxyDBProxiedSession, 
        'ProxyScrapeProxiedSession': ProxyScrapeProxiedSession,       'SCDNProxiedSession': SCDNProxiedSession,                      'GoodIPSProxiedSession': GoodIPSProxiedSession,            'SixSixDailiProxiedSession': SixSixDailiProxiedSession,          'DpangestuwProxiedSession': DpangestuwProxiedSession,    'ProxyNovaProxiedSession': ProxyNovaProxiedSession,       'ProxyShareProxiedSession': ProxyShareProxiedSession,
        'OpenProxyListProxiedSession': OpenProxyListProxiedSession,   'IPRoyalProxiedSession': IPRoyalProxiedSession,                'ADVFPProxiedSession': ADVFPProxiedSession,                'RoundProxiesProxiedSession': RoundProxiesProxiedSession,        'SocksListProxiedSession': SocksListProxiedSession,      'ProxiwareProxiedSession': ProxiwareProxiedSession,       'ProxyFreeOnlyProxiedSession': ProxyFreeOnlyProxiedSession,
        'TrustyTechProxiedSession': TrustyTechProxiedSession,         'FreeVPNNodeProxiedSession': FreeVPNNodeProxiedSession,        'FloppyDataProxiedSession': FloppyDataProxiedSession,      'PubProxyProxiedSession': PubProxyProxiedSession,                'GeonixProxiedSession': GeonixProxiedSession,            'ProxyVerityProxiedSession': ProxyVerityProxiedSession,   'MyProxyProxiedSession': MyProxyProxiedSession,
        'SpysMeProxiedSession': SpysMeProxiedSession,                 'FreeProxyWorldProxiedSession': FreeProxyWorldProxiedSession,  'ChillyProxyProxiedSession': ChillyProxyProxiedSession,    'ProxySpaceProxiedSession': ProxySpaceProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build