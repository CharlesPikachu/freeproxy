'''
Function:
    Naive scraping proxies from specified proxy sources
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import json
import random
from tqdm import tqdm
from freeproxy.modules import BaseProxiedSession, ProxyInfo, BuildProxiedSession, printtable, colorize


'''main'''
def main():
    # proxy_sources
    proxy_sources = ['ProxiflyProxiedSession', 'KuaidailiProxiedSession', 'QiyunipProxiedSession', 'ProxylistProxiedSession']
    # iter scraping
    free_proxies = {}
    print_titles, print_items = ['Source', 'Retrieved Examples', 'HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5', 'Chinese IP', 'Elite', 'Total'], []
    for proxy_source in tqdm(proxy_sources):
        try:
            module_cfg = {'max_pages': 1, 'type': proxy_source, 'disable_print': False}
            proxied_session: BaseProxiedSession = BuildProxiedSession(module_cfg=module_cfg)
            candidate_proxies: list[ProxyInfo] = proxied_session.refreshproxies()
        except:
            candidate_proxies = []
        if len(candidate_proxies) > 0:
            example_proxy = random.choice(candidate_proxies).proxy
            count_http = sum([(p.protocol.lower() in ['http']) for p in candidate_proxies])
            count_https = sum([(p.protocol.lower() in ['https']) for p in candidate_proxies])
            count_socks4 = sum([(p.protocol.lower() in ['socks4']) for p in candidate_proxies])
            count_socks5 = sum([(p.protocol.lower() in ['socks5']) for p in candidate_proxies])
            count_cn = sum([p.in_chinese_mainland for p in candidate_proxies])
            count_elite = sum([(p.anonymity.lower() in ['elite']) for p in candidate_proxies])
            print_items.append([
                proxy_source.removesuffix('ProxiedSession'), colorize(example_proxy, 'green'), colorize(count_http, 'number'), colorize(count_https, 'number'), 
                colorize(count_socks4, 'number'), colorize(count_socks5, 'number'), colorize(count_cn, 'number'), colorize(count_elite, 'number'),
                colorize(len(candidate_proxies), 'number'),
            ])
        else:
            print_items.append([
                proxy_source.removesuffix('ProxiedSession'), 'NULL', colorize('0', 'number'), colorize('0', 'number'), 
                colorize('0', 'number'), colorize('0', 'number'), colorize('0', 'number'), colorize('0', 'number'),
                colorize(len(candidate_proxies), 'number'),
            ])
        free_proxies[proxy_source] = [p.todict() for p in candidate_proxies]
    # visualize scraping results
    print("The proxy distribution for each source you specified is as follows:")
    printtable(titles=print_titles, items=print_items, terminal_right_space_len=1)
    # save scraping results
    json.dump(free_proxies, open('free_proxies.json', 'w'), indent=2)


'''tests'''
if __name__ == '__main__':
    main()