'''
Function:
    Naive scraping proxies from specified proxy sources
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import json, random
from tqdm import tqdm
from freeproxy.modules import BaseProxiedSession, ProxyInfo, BuildProxiedSession, printtable, colorize


'''settings'''
SOURCES = ["ProxiflyProxiedSession", "KuaidailiProxiedSession", "QiyunipProxiedSession", "ProxylistProxiedSession"]
TITLES = ["Source", "Retrieved Example", "HTTP", "HTTPS", "SOCKS4", "SOCKS5", "Chinese IP", "Elite", "Total"]


'''scrape'''
def scrape(src: str) -> list[ProxyInfo]:
    try:
        sess: BaseProxiedSession = BuildProxiedSession({"max_pages": 1, "type": src, "disable_print": False})
        return sess.refreshproxies()
    except Exception:
        return []


'''stats'''
def stats(proxies: list[ProxyInfo]) -> dict:
    return {
        "http":   sum(p.protocol.lower() == "http"   for p in proxies),
        "https":  sum(p.protocol.lower() == "https"  for p in proxies),
        "socks4": sum(p.protocol.lower() == "socks4" for p in proxies),
        "socks5": sum(p.protocol.lower() == "socks5" for p in proxies),
        "cn":     sum(bool(p.in_chinese_mainland) for p in proxies),
        "elite":  sum(p.anonymity.lower() == "elite" for p in proxies),
        "total":  len(proxies),
        "ex":     (random.choice(proxies).proxy if proxies else "NULL"),
    }


'''row'''
def row(src: str, s: dict) -> list:
    ex = colorize(s["ex"], "green") if s["total"] else "NULL"
    return [
        src.removesuffix("ProxiedSession"),
        ex,
        colorize(s["http"], "number"),
        colorize(s["https"], "number"),
        colorize(s["socks4"], "number"),
        colorize(s["socks5"], "number"),
        colorize(s["cn"], "number"),
        colorize(s["elite"], "number"),
        colorize(s["total"], "number"),
    ]


'''main'''
def main():
    free_proxies, items = {}, []
    for src in tqdm(SOURCES):
        proxies = scrape(src)
        items.append(row(src, stats(proxies)))
        free_proxies[src] = [p.todict() for p in proxies]
    print("The proxy distribution for each source you specified is as follows:")
    printtable(titles=TITLES, items=items, terminal_right_space_len=1)
    json.dump(free_proxies, open("free_proxies.json", "w"), indent=2)


'''tests'''
if __name__ == "__main__":
    main()