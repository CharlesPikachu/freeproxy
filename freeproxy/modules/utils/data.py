'''
Function:
    Implementation of ProxyInfo
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
from __future__ import annotations
import time
import socket
import requests
import ipaddress
from datetime import datetime
from urllib.parse import urlparse
from typing import Dict, Any, Tuple
from dataclasses import dataclass, field, asdict


'''ProxyInfo'''
@dataclass
class ProxyInfo:
    source: str = ""
    protocol: str = ""
    ip: str = ""
    port: str = ""
    country_code: str = ""
    in_chinese_mainland: bool | None = None
    anonymity: str | None = None
    delay: int | None = None
    test_timeout: int = 60
    test_url: str = "https://www.facebook.com"
    test_headers: Dict[str, Any] = field(default_factory=lambda: {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"})
    failed_connection_default_timeout: int = 3600000
    created_at: datetime = field(default_factory=datetime.utcnow)
    extra: Dict[str, Any] = field(default_factory=dict)
    @property
    def proxy(self) -> str:
        return f"{self.protocol}://{self.ip}:{self.port}"
    @property
    def requests_format_proxy(self) -> dict:
        return {"http": self.proxy, "https": self.proxy}
    @property
    def tcp_connect_delay(self) -> int:
        start = time.monotonic()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.test_timeout)
        try:
            s.connect((self.ip, int(float(self.port))))
            elapsed_ms = int((time.monotonic() - start) * 1000)
            return elapsed_ms
        except (socket.timeout, OSError):
            return self.failed_connection_default_timeout
        finally:
            s.close()
    @property
    def http_connect_delay(self) -> int:
        start = time.monotonic()
        try:
            resp = requests.head(self.test_url, proxies=self.requests_format_proxy, timeout=self.test_timeout, headers=self.test_headers)
            resp.raise_for_status()
            elapsed_ms = int((time.monotonic() - start) * 1000)
            return elapsed_ms
        except Exception:
            return self.failed_connection_default_timeout
    '''todict'''
    def todict(self) -> Dict[str, Any]:
        item = asdict(self)
        if isinstance(self.created_at, datetime):
            item["created_at"] = self.created_at.isoformat()
        return item
    '''fromdict'''
    @classmethod
    def fromdict(cls, item: Dict[str, Any]) -> "ProxyInfo":
        created_at = item.get("created_at")
        if isinstance(created_at, str) and created_at:
            try: created_at = datetime.fromisoformat(created_at)
            except ValueError: created_at = datetime.utcnow()
        else:
            created_at = datetime.utcnow()
        return cls(
            source=item.get("source", ""), protocol=item.get("protocol", ""), ip=item.get("ip", ""), port=item.get("port", ""),
            country_code=item.get("country_code", ""), in_chinese_mainland=item.get("in_chinese_mainland", None), anonymity=item.get("anonymity", None),
            delay=item.get("delay", None), test_timeout=item.get("test_timeout", 5), test_url=item.get("test_url", "https://www.facebook.com"), 
            test_headers=item.get("test_headers", {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}), 
            failed_connection_default_timeout=item.get("failed_connection_default_timeout", 3600000), created_at=created_at, extra=item.get("extra", {}),
        )
    '''selfcheck'''
    def selfcheck(self) -> Tuple[bool, str]:
        # step1: protocol check
        allowed_protocols = {"http", "https", "socks4", "socks5"}
        if not self.protocol: return False, "protocol is empty"
        if self.protocol not in allowed_protocols: return False, f"unsupported protocol {self.protocol!r}"
        # step2: port check
        if not self.port: return False, "port is empty"
        try: port_int = int(self.port)
        except (TypeError, ValueError): return False, f"port is not an integer: {self.port!r}"
        if not (1 <= port_int <= 65535): return False, f"port out of range: {port_int}"
        # step3: ip naive check
        if not self.ip: return False, "ip is empty"
        if "://" in self.ip: return False, f"ip should not contain scheme: {self.ip!r}"
        # step4: ip check
        try:
            ipaddress.ip_address(self.ip)
        except:
            return False, f"invalid hostname: {self.ip!r}"
        # step5: proxy check
        parsed = urlparse(self.proxy)
        if not (parsed.scheme and parsed.hostname and parsed.port): return False, f"invalid proxy URL: {self.proxy!r}"
        return True, ""