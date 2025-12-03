'''
Function:
    Proxies update for proxy.json in https://github.com/CharlesPikachu/freeproxy
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import json
import requests
from datetime import datetime


# APIs
JSON_ENDPOINTS1 = [
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=1&start=0&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=2&start=100&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=3&start=200&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=4&start=300&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=5&start=400&length=100"},
]
JSON_ENDPOINTS2 = [
    {"url": "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.json"},
    {"url": "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/us/data.json"},
]
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}


'''fetchjsonendpoint1'''
def fetchjsonendpoint1(ep):
    url = ep["url"]
    print(f"[JSON1] Fetching from {url}")
    try:
        resp = requests.get(url, timeout=25, headers=DEFAULT_HEADERS)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[JSON1] Error fetching JSON endpoint: {e}")
        return []
    rows = data.get("data", []) or []
    proxies = []
    for row in rows:
        ip = row.get("ip")
        port = row.get("port")
        if not ip or not port:
            continue
        proxies.append({
            "ip": ip, "port": port, "protocol": row.get("protocol"), "country": row.get("country"), "anonymity": row.get("anonymity"), "speed": row.get("speed"),
        })
    print(f"[JSON1] proxies fetched: {len(proxies)}")
    return proxies


'''fetchjsonendpoint2'''
def fetchjsonendpoint2(ep):
    url = ep["url"]
    print(f"[JSON2] Fetching from {url}")
    try:
        resp = requests.get(url, timeout=25, headers=DEFAULT_HEADERS)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[JSON2] Error fetching JSON endpoint: {e}")
        return []
    rows = data or []
    proxies = []
    for row in rows:
        ip = row.get("ip")
        port = row.get("port")
        if not ip or not port:
            continue
        proxies.append({
            "ip": ip, "port": port, "protocol": row.get("protocol"), "country": row.get("geolocation", {}).get("country"), "anonymity": row.get("anonymity"), "speed": row.get("speed", 100),
        })
    print(f"[JSON2] proxies fetched: {len(proxies)}")
    return proxies


'''main'''
def main():
    all_proxies = []
    for ep in JSON_ENDPOINTS1:
        try:
            all_proxies.extend(fetchjsonendpoint1(ep))
        except Exception as err:
            print(f"[WARN] Failed to fetch JSON1 endpoint {ep}: {err}")
    for ep in JSON_ENDPOINTS2:
        try:
            all_proxies.extend(fetchjsonendpoint2(ep))
        except Exception as err:
            print(f"[WARN] Failed to fetch JSON2 endpoint {ep}: {err}")
    uniq = {}
    for p in all_proxies:
        key = (p["ip"], p["port"], p["protocol"])
        uniq[key] = p
    all_proxies = list(uniq.values())
    data = {"updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"), "count": len(all_proxies), "data": all_proxies}
    with open("proxies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[DONE] Saved {len(all_proxies)} proxies to proxies.json")


'''init'''
if __name__ == "__main__":
    main()