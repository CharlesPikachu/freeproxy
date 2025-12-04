# -*- coding: utf-8 -*-
"""
Flask API for the freeproxy library.

Endpoints
---------
GET /proxies
    Return the list of cached proxies.
    Query parameters (all optional):
        - type:          name of the source module (e.g. KuaidailiProxiedSession)
        - country_code:  ISO country code (e.g. CN, US)
        - protocol:      http / https / socks5 …
        - anonymity:     elite / anonymous / transparent
        - min_delay:     minimum delay in ms
        - max_delay:     maximum delay in ms
"""

from flask import Flask, jsonify, request
from .freeproxy import ProxiedSessionClient

app = Flask(__name__)

# Initialise the client once (you can tweak the sources / filter rules)
client = ProxiedSessionClient(
    proxy_sources=None,                     # use all registered sources
    init_proxied_session_cfg={
        "max_pages": 2,                    # crawl a couple of pages per source
        "filter_rule": None,               # no filter at crawl time
    },
)

def refresh_proxies_task():
    """Background task to refresh proxies and save to Redis."""
    print("Starting scheduled proxy refresh...")
    try:
        # Re-initialize sessions to trigger a fresh crawl
        # Note: In a more complex setup, we might want a dedicated method to refresh existing sessions
        # but re-instantiating ensures we pick up fresh configurations and clear stale state.
        # However, ProxiedSessionClient.__init__ triggers the crawl.
        # To avoid re-creating the 'client' object which is global, we can just manually trigger
        # a refresh on the existing sessions or re-create the internal sessions.
        # For simplicity and robustness given the current class design, let's just
        # iterate over existing sessions and call refreshproxies() if available,
        # or better yet, re-run the logic that populates self.proxied_sessions.
        
        # Actually, the cleanest way with the current class is to just create a NEW client instance
        # temporarily to do the crawling, then update the Redis cache.
        # The API reads from Redis, so it doesn't matter if the 'client' object in memory
        # has the latest proxies, as long as Redis does.
        
        temp_client = ProxiedSessionClient(
            proxy_sources=None,
            init_proxied_session_cfg={
                "max_pages": 2,
                "filter_rule": None,
            },
        )
        temp_client.save_to_file()
        print("Scheduled proxy refresh complete.")
    except Exception as e:
        print(f"Error during scheduled proxy refresh: {e}")

# Populate Redis cache on start‑up
# We run this in a separate thread or just let the scheduler handle the first run if we want faster startup,
# but usually we want data immediately. Let's keep the initial sync.
print("Performing initial proxy crawl...")
client.save_to_file()

# Setup Scheduler
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=refresh_proxies_task, trigger="interval", minutes=10)
scheduler.start()

# Shut down the scheduler when exiting the app
import atexit
atexit.register(lambda: scheduler.shutdown())


def _apply_query_filters(proxies, args):
    """Filter a list of ProxyInfo dicts according to request args.
    
    Supports comma-separated values for 'type', 'country_code', 'protocol', and 'anonymity'.
    Example: ?protocol=http,https&country_code=US,CN
    """
    result = proxies
    
    # Helper to parse comma-separated list
    def get_list(key):
        val = args.get(key)
        if not val:
            return None
        return [x.strip().lower() for x in val.split(',')]

    # Filter by Source Type
    types = get_list("type")
    if types:
        # Source names are case-sensitive usually, but let's be flexible or strict?
        # The internal source names are CamelCase (e.g. KuaidailiProxiedSession).
        # Let's keep strict matching for source names but handle the list logic.
        # Actually, let's just split the raw string without lower() for 'type' to preserve case.
        raw_types = [x.strip() for x in args.get("type").split(',')]
        result = [p for p in result if p["source"] in raw_types]

    # Filter by Country Code
    countries = get_list("country_code")
    if countries:
        # Proxy country codes are usually uppercase (CN, US), but let's compare case-insensitively
        result = [p for p in result if p.get("country_code", "").lower() in countries]

    # Filter by Protocol
    protocols = get_list("protocol")
    if protocols:
        result = [p for p in result if p.get("protocol", "").lower() in protocols]

    # Filter by Anonymity
    anonymities = get_list("anonymity")
    if anonymities:
        result = [p for p in result if p.get("anonymity", "").lower() in anonymities]

    # Filter by Delay
    if "min_delay" in args:
        try:
            min_d = int(args["min_delay"])
            result = [p for p in result if p.get("delay", 0) >= min_d]
        except ValueError:
            pass
    if "max_delay" in args:
        try:
            max_d = int(args["max_delay"])
            result = [p for p in result if p.get("delay", 0) <= max_d]
        except ValueError:
            pass
    return result


@app.route("/proxies", methods=["GET"])
def get_proxies():
    """
    Return cached proxies (JSON) with optional filtering.
    """
    # Load from Redis (or fallback to empty dict)
    data = client.load_from_file()
    # Flatten: {source: [proxy_dict, ...]} -> list of dicts with a `source` field
    flat = []
    for src, lst in data.items():
        for p in lst:
            p["source"] = src
            flat.append(p)

    # Apply query‑string filters
    filtered = _apply_query_filters(flat, request.args)

    return jsonify({"total": len(filtered), "proxies": filtered})


if __name__ == "__main__":
    # Run the API on 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=5000, debug=False)
