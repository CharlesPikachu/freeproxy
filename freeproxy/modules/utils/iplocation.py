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


'''IPLocater'''
class IPLocater:
    DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    '''locate'''
    @staticmethod
    def locate(ip: str) -> str:
        # https://ipinfo.io/{ip}/json
        def api1_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipinfo.io/{ip}/json', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ip.zhengbingdong.com/v1/get?ip={ip}
        def api2_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://ip.zhengbingdong.com/v1/get?ip={ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['data']['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://api.ip.sb/geoip/{ip}
        def api3_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://api.ip.sb/geoip/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://demo.ip-api.com/json/{ip}
        def api4_func(ip: str) -> str:
            try:
                resp = requests.get(f'http://demo.ip-api.com/json/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipapi.co/{ip}/json/
        def api5_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipapi.co/{ip}/json/', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://ip-api.com/json/{ip}
        def api6_func(ip: str) -> str:
            try:
                resp = requests.get(f'http://ip-api.com/json/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://api.db-ip.com/v2/free/{ip}
        def api7_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://api.db-ip.com/v2/free/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://free.freeipapi.com/api/json/{ip}
        def api8_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://free.freeipapi.com/api/json/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipwhois.app/json/{ip}?format=json/
        def api9_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipwhois.app/json/{ip}?format=json/', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # http://ip-api.com/json/{ip}?fields=status,countryCode
        def api10_func(ip: str) -> str:
            try:
                resp = requests.get(f'http://ip-api.com/json/{ip}?fields=status,countryCode', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['countryCode'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # https://ipwho.is/{ip}
        def api11_func(ip: str) -> str:
            try:
                resp = requests.get(f'https://ipwho.is/{ip}', headers=IPLocater.DEFAULT_HEADERS)
                resp.raise_for_status()
                country_code = resp.json()['country_code'].upper()
                assert country_code
                return country_code
            except:
                return ""
        # random select one api to locate
        for _ in range(10):
            country_code = random.choice([api1_func, api2_func, api3_func, api4_func, api5_func, api6_func, api7_func, api8_func, api9_func, api10_func, api11_func])(ip=ip)
            if country_code: return country_code
        # too many tries, return ""
        return ""