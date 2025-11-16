'''
Function:
    Proxies update for proxy.json in https://github.com/CharlesPikachu/freeproxy
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import requests
import json
from datetime import datetime


# APIs
JSON_ENDPOINTS = [
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=1&start=0&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=2&start=100&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=3&start=200&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=4&start=300&length=100"},
    {"url": "https://proxy-daily.com/api/serverside/proxies?draw=5&start=400&length=100"},
]
TEXT_ENDPOINTS = [
    {"url": "https://www.proxy-list.download/api/v1/get?type=http",   "protocol": "Http"},
    {"url": "https://www.proxy-list.download/api/v1/get?type=https",  "protocol": "Https"},
    {"url": "https://www.proxy-list.download/api/v1/get?type=socks4", "protocol": "Socks4"},
    {"url": "https://www.proxy-list.download/api/v1/get?type=socks5", "protocol": "Socks5"},
]


'''fetchtextendpoint'''
def fetchtextendpoint(ep):
    print(f"[TEXT] Fetching {ep['protocol']} from {ep['url']}")
    resp = requests.get(ep["url"], timeout=25)
    resp.raise_for_status()
    text = resp.text
    proxies = []
    for line in text.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        ip, port = line.split(":", 1)
        ip = ip.strip()
        port = port.strip()
        if not ip or not port:
            continue
        try:
            port_val = int(port)
        except ValueError:
            port_val = port
        proxies.append({"ip": ip, "port": port_val, "protocol": ep["protocol"], "country": None, "anonymity": None, "speed": None})
    print(f"[TEXT] {ep['protocol']} proxies fetched: {len(proxies)}")
    return proxies


'''fetchjsonendpoint'''
def fetchjsonendpoint(ep):
    url = ep["url"]
    print(f"[JSON] Fetching from {url}")
    try:
        resp = requests.get(url, timeout=25)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[JSON] Error fetching JSON endpoint: {e}")
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
    print(f"[JSON] proxies fetched: {len(proxies)}")
    return proxies


'''main'''
def main():
    all_proxies = []
    for ep in JSON_ENDPOINTS:
        try:
            all_proxies.extend(fetchjsonendpoint(ep))
        except Exception as e:
            print(f"[WARN] Failed to fetch JSON endpoint: {e}")
    for ep in TEXT_ENDPOINTS:
        try:
            all_proxies.extend(fetchtextendpoint(ep))
        except Exception as e:
            print(f"[WARN] Failed to fetch {ep['protocol']}: {e}")
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