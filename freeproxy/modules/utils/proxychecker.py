'''
Function:
    Implementation of checking proxy related utils
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
from functools import wraps
from .data import ProxyInfo
from .logger import LoggerHandle
from typing import Iterable, Optional, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed


'''filterinvalidproxies'''
def filterinvalidproxies(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # init
        result = func(*args, **kwargs); proxies: list[ProxyInfo] = []
        normalize_func = (lambda item, _func=func: item if isinstance(item, ProxyInfo) else ProxyInfo.fromdict(item) if isinstance(item, dict) else (_ for _ in ()).throw(TypeError(f"{_func.__qualname__} must return ProxyInfo or dict, but got {type(item)!r}")))
        if isinstance(result, ProxyInfo) or isinstance(result, dict): proxies = [normalize_func(result)]
        elif isinstance(result, Iterable) and not isinstance(result, (str, bytes)): proxies.extend([normalize_func(x) for x in result])
        else: raise TypeError(f"{func.__qualname__} must return ProxyInfo, dict, or iterable of them, but got {type(result)!r}")
        # proxies with valid and invalid format
        valid: list[ProxyInfo] = []; invalid_info: list[tuple[ProxyInfo, str]] = []
        for p in proxies:
            ok, reason = p.selfcheck()
            if ok: valid.append(p)
            else: invalid_info.append((p, reason))
        # logging if necessary
        if args:
            logger_handle: LoggerHandle = getattr(args[0], "logger_handle", None)
            disable_print: bool = getattr(args[0], "disable_print", False)
            homepage: str = getattr(args[0], "homepage", "")
            if logger_handle and invalid_info:
                for bad_p, reason in invalid_info: logger_handle.warning(f"{func.__qualname__} >>> {bad_p.proxy} (Error: {reason}, auto drop by default)", disable_print=disable_print)
            if logger_handle and not valid:
                reasons = ", ".join(set(reason for _, reason in invalid_info)) or "no proxies"
                logger_handle.warning(f"{func.__qualname__} >>> {homepage} (Error: {reasons})", disable_print=disable_print)
        # filter repeated proxies
        unique_proxy_infos, unique_identifiers = [], set()
        for p in valid:
            if p.proxy in unique_identifiers: continue
            unique_identifiers.add(p.proxy); unique_proxy_infos.append(p)
        # setting to class attributes
        if args: args[0].candidate_proxies = unique_proxy_infos
        # return
        return unique_proxy_infos
    return wrapper


'''tolist'''
def __tolist__(obj: Optional[str | list | tuple] = None):
    try: obj = list(obj or [])
    except: obj = []
    if isinstance(obj, str): obj: list[str] = [obj]
    return [o.lower() for o in obj]


'''applyfilterrule'''
def applyfilterrule():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            proxies, filtered = func(self, *args, **kwargs), []
            rule = getattr(self, "filter_rule", None)
            if rule is None or not rule or not isinstance(rule, dict): return proxies
            anonymity, protocol, country_code = __tolist__(rule.get('anonymity')), __tolist__(rule.get('protocol')), __tolist__(rule.get('country_code'))
            max_tcp_ms, max_tcp_ms_flag = rule.get('max_tcp_ms'), False
            if (max_tcp_ms is not None) and isinstance(max_tcp_ms, (int, float)):
                with ThreadPoolExecutor(max_workers=20) as executor:
                    futures = [executor.submit(p.tcp_connect_delay,) for p in proxies]
                    for future in as_completed(futures):
                        try: future.result()
                        except Exception: continue
                max_tcp_ms_flag = True
            max_http_ms, max_http_ms_flag = rule.get('max_http_ms'), False
            if (max_http_ms is not None) and isinstance(max_http_ms, (int, float)):
                with ThreadPoolExecutor(max_workers=20) as executor:
                    futures = [executor.submit(p.http_connect_delay,) for p in proxies]
                    for future in as_completed(futures):
                        try: future.result()
                        except Exception: continue
                max_http_ms_flag = True
            for p in proxies:
                if not isinstance(p, ProxyInfo): continue
                if anonymity and (p.anonymity.lower() not in anonymity): continue
                if protocol and (p.protocol.lower() not in protocol): continue
                if country_code and (p.country_code.lower() not in country_code): continue
                if max_tcp_ms_flag and p.tcp_connect_delay > max_tcp_ms: continue
                if max_http_ms_flag and p.http_connect_delay > max_http_ms: continue
                filtered.append(p)
            self.candidate_proxies = filtered
            return filtered
        return wrapper
    return decorator