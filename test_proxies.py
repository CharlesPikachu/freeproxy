import requests
import random
import concurrent.futures
import time

API_URL = "http://localhost:5000/proxies?protocol"
TEST_URL = "https://facebook.com"
TIMEOUT = 30

def get_proxies():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("proxies", [])
    except Exception as e:
        print(f"Error fetching proxies from API: {e}")
        return []

def check_proxy(proxy_info):
    # Construct proxy string for requests
    protocol = proxy_info.get('protocol', 'http')
    ip = proxy_info.get('ip')
    port = proxy_info.get('port')
    
    if not ip or not port:
        return False, "Invalid proxy data"

    # Determine scheme based on protocol
    scheme = "http"
    if "socks4" in protocol:
        scheme = "socks4"
    elif "socks5" in protocol:
        scheme = "socks5"
    
    # Construct proxy URL with correct scheme
    proxy_url = f"{scheme}://{ip}:{port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    start_time = time.time()
    try:
        # We verify against Facebook
        resp = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT, verify=False)
        elapsed = time.time() - start_time
        if resp.status_code == 200:
            return True, f"Success ({elapsed:.2f}s)"
        else:
            return False, f"Status {resp.status_code} ({elapsed:.2f}s)"
    except Exception as e:
        # Shorten error message
        err_msg = str(e)
        if "connect timeout" in err_msg.lower():
            err_msg = "Connect Timeout"
        elif "read timeout" in err_msg.lower():
            err_msg = "Read Timeout"
        elif "proxy error" in err_msg.lower():
            err_msg = "Proxy Error"
        return False, f"Failed: {err_msg}"

def main():
    print(f"Fetching proxies from {API_URL}...")
    all_proxies = get_proxies()
    print(f"Total proxies found: {len(all_proxies)}")

    # Filter out proxies from China
    all_proxies = [
        p for p in all_proxies 
        if p.get('country_code') != 'CN' and p.get('in_chinese_mainland') is not True
    ]
    print(f"Proxies after removing China: {len(all_proxies)}")

    if not all_proxies:
        print("No proxies available to test.")
        return

    # Sort by 'delay' (lowest first) and take top 100
    # Filter out proxies with None delay first
    valid_proxies = [p for p in all_proxies if p.get('delay') is not None]
    # If delay is missing, treat as high delay
    others = [p for p in all_proxies if p.get('delay') is None]
    
    valid_proxies.sort(key=lambda x: x['delay'])
    sorted_proxies = valid_proxies + others
    
    num_to_test = min(100, len(sorted_proxies))
    selected_proxies = sorted_proxies[:num_to_test]
    print(f"Selected top {num_to_test} proxies with lowest delay for testing against {TEST_URL}...")

    success_count = 0
    
    # Use threads to speed up checking
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_proxy = {executor.submit(check_proxy, p): p for p in selected_proxies}
        
        for i, future in enumerate(concurrent.futures.as_completed(future_to_proxy)):
            proxy_info = future_to_proxy[future]
            proxy_str = f"{proxy_info.get('ip')}:{proxy_info.get('port')}"
            
            try:
                is_success, msg = future.result()
                status = "✅" if is_success else "❌"
                print(f"[{i+1}/{num_to_test}] {status} {proxy_str} - {msg}")
                if is_success:
                    success_count += 1
            except Exception as exc:
                print(f"[{i+1}/{num_to_test}] ❌ {proxy_str} - Exception: {exc}")

    print("-" * 30)
    print(f"Testing complete.")
    print(f"Success rate: {success_count}/{num_to_test} ({success_count/num_to_test*100:.1f}%)")

if __name__ == "__main__":
    main()
