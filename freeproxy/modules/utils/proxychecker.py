'''
Function:
    Implementation of checking proxy related utils
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
from functools import wraps
from urllib.parse import urlparse


'''ensurevalidrequestsproxies'''
def ensurevalidrequestsproxies(func):
    # isvalidproxydict
    def isvalidproxydict(p):
        if not isinstance(p, dict) or not p: return False
        allowed_schemes = {"http", "https", "socks4", "socks5"}
        for scheme, url in p.items():
            if scheme not in allowed_schemes: return False
            if not isinstance(url, str) or not url: return False
            parsed = urlparse(url)
            if parsed.scheme not in allowed_schemes:
                return False
            if not parsed.hostname or parsed.port is None:
                return False
        return True
    # wrapper
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        raw_list = getattr(self, "candidate_proxies", None)
        if isinstance(raw_list, list):
            cleaned = [p for p in raw_list if isvalidproxydict(p)]
            self.candidate_proxies = cleaned
        else:
            cleaned = []
        return cleaned
    # return
    return wrapper