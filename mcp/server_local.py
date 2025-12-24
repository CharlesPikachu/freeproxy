'''
Function:
    Implementation of Naive MCP Examples
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import sys, logging
from mcp.server.fastmcp import FastMCP
from freeproxy.freeproxy import ProxiedSessionClient


'''settings'''
_client = None
mcp = FastMCP("freeproxy")
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def getclient(proxy_sources=None, init_proxied_session_cfg=None, disable_print=True, max_tries=5):
    """get proxied session client"""
    global _client
    if _client is None:
        _client = ProxiedSessionClient(
            proxy_sources=proxy_sources or ['ProxiflyProxiedSession'], init_proxied_session_cfg=init_proxied_session_cfg or {}, disable_print=disable_print, max_tries=max_tries,
        )
    return _client


@mcp.tool()
def get(url: str, kwargs: dict | None = None) -> dict:
    """HTTP GET via rotating proxies."""
    resp = getclient().get(url, **(kwargs or {}))
    return {
        "status_code": getattr(resp, "status_code", None), "url": getattr(resp, "url", url), "text": getattr(resp, "text", None),
    }


@mcp.tool()
def post(url: str, kwargs: dict | None = None) -> dict:
    """HTTP POST via rotating proxies."""
    resp = getclient().post(url, **(kwargs or {}))
    return {
        "status_code": getattr(resp, "status_code", None), "url": getattr(resp, "url", url), "text": getattr(resp, "text", None),
    }


@mcp.tool()
def getrandomproxy(proxy_format: str = "requests") -> dict:
    """Get a random proxy in specified format."""
    p = getclient().getrandomproxy(proxy_format=proxy_format)
    return {"proxy": p}


'''main'''
if __name__ == "__main__":
    mcp.run(transport="stdio")