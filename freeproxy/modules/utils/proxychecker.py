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
from typing import Any, Iterable, Optional, Callable


'''filterinvalidproxies'''
def filterinvalidproxies(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # init
        result = func(*args, **kwargs)
        proxies: list[ProxyInfo] = []
        def _normalize(item: Any) -> ProxyInfo:
            if isinstance(item, ProxyInfo): return item
            if isinstance(item, dict): return ProxyInfo.fromdict(item)
            raise TypeError(f"{func.__qualname__} must return ProxyInfo or dict, but got {type(item)!r}")
        if isinstance(result, ProxyInfo) or isinstance(result, dict):
            proxies = [_normalize(result)]
        elif isinstance(result, Iterable) and not isinstance(result, (str, bytes)):
            for x in result: proxies.append(_normalize(x))
        else:
            raise TypeError(f"{func.__qualname__} must return ProxyInfo, dict, or iterable of them, but got {type(result)!r}")
        # proxies with valid and invalid format
        valid: list[ProxyInfo] = []
        invalid_info: list[tuple[ProxyInfo, str]] = []
        for p in proxies:
            ok, reason = p.selfcheck()
            if ok: valid.append(p)
            else: invalid_info.append((p, reason))
        # logging if necessary
        if args:
            self_obj = args[0]
            logger_handle: LoggerHandle = getattr(self_obj, "logger_handle", None)
            disable_print: bool = getattr(self_obj, "disable_print", False)
            homepage: str = getattr(self_obj, "homepage", "")
            if logger_handle and invalid_info:
                for bad_p, reason in invalid_info:
                    logger_handle.warning(f"{func.__qualname__} >>> {bad_p.proxy} (Error: {reason}, auto drop by default)", disable_print=disable_print)
            if logger_handle and not valid:
                reasons = ", ".join(set(reason for _, reason in invalid_info)) or "no proxies"
                logger_handle.warning(f"{func.__qualname__} >>> {homepage} (Error: {reasons})", disable_print=disable_print)
        # filter repeated proxies
        unique_proxy_infos, unique_identifiers = [], set()
        for p in valid:
            if p.proxy in unique_identifiers: continue
            unique_identifiers.add(p.proxy)
            unique_proxy_infos.append(p)
        # setting to class attributes
        if args:
            self_obj = args[0]
            self_obj.candidate_proxies = unique_proxy_infos
        # return
        return unique_proxy_infos
    return wrapper


'''__tolist__'''
def __tolist__(obj: Optional[str | list | tuple] = None):
    try:
        obj = list(obj or [])
    except:
        obj = []
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
            anonymity = __tolist__(rule.get('anonymity'))
            protocol = __tolist__(rule.get('protocol'))
            country_code = __tolist__(rule.get('country_code'))
            max_tcp_ms = rule.get('max_tcp_ms')
            max_http_ms = rule.get('max_http_ms')
            for p in proxies:
                if not isinstance(p, ProxyInfo): continue
                if anonymity and (p.anonymity.lower() not in anonymity): continue
                if protocol and (p.protocol.lower() not in protocol): continue
                if country_code and (p.country_code.lower() not in country_code): continue
                if (max_tcp_ms is not None) and isinstance(max_tcp_ms, (int, float)) and p.tcp_connect_delay > max_tcp_ms: continue
                if (max_http_ms is not None) and isinstance(max_tcp_ms, (int, float)) and p.http_connect_delay > max_http_ms: continue
                filtered.append(p)
            self.candidate_proxies = filtered
            return filtered
        return wrapper
    return decorator