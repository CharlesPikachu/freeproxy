'''
Function:
    Implementation of IPLocater
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import random
import requests


'''settings'''
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}


'''IPLocater'''
class IPLocater:
    '''locate'''
    @staticmethod
    def locate(ip: str) -> str:
        # https://ipinfo.io/{ip}/json
        def _api1(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipinfo.io/{ip}/json', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ip.zhengbingdong.com/v1/get?ip={ip}
        def _api2(ip: str) -> str:
            try:
                resp = requests.get(f'https://ip.zhengbingdong.com/v1/get?ip={ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['data']['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://api.ip.sb/geoip/{ip}
        def _api3(ip: str) -> str:
            try:
                resp = requests.get(f'https://api.ip.sb/geoip/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://demo.ip-api.com/json/{ip}
        def _api4(ip: str) -> str:
            try:
                resp = requests.get(f'http://demo.ip-api.com/json/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipapi.co/{ip}/json/
        def _api5(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipapi.co/{ip}/json/', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://ip-api.com/json/{ip}
        def _api6(ip: str) -> str:
            try:
                resp = requests.get(f'http://ip-api.com/json/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://api.db-ip.com/v2/free/{ip}
        def _api7(ip: str) -> str:
            try:
                resp = requests.get(f'https://api.db-ip.com/v2/free/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://free.freeipapi.com/api/json/{ip}
        def _api8(ip: str) -> str:
            try:
                resp = requests.get(f'https://free.freeipapi.com/api/json/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipwhois.app/json/{ip}?format=json/
        def _api9(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipwhois.app/json/{ip}?format=json/', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://ip-api.com/json/{ip}?fields=status,countryCode
        def _api10(ip: str) -> str:
            try:
                resp = requests.get(f'http://ip-api.com/json/{ip}?fields=status,countryCode', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipwho.is/{ip}
        def _api11(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipwho.is/{ip}', headers=DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # random select one api to locate
        for _ in range(10):
            country_code = random.choice([_api1, _api2, _api3, _api4, _api5, _api6, _api7, _api8, _api9, _api10, _api11])(ip=ip)
            if country_code: return country_code
        # too many tries, return ""
        return ""