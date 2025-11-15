'''
Function:
    Test the effectiveness of each proxy source
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
from tqdm import tqdm
from freeproxy.modules import ProxiedSessionBuilder, BuildProxiedSession, printtable, colorize


'''main'''
def main():
    # proxy_sources
    proxy_sources = ProxiedSessionBuilder.REGISTERED_MODULES.keys()
    # iter to test
    print_titles, print_items = ['Source', 'Effectiveness', 'Retrieved Examples'], []
    for proxy_source in tqdm(proxy_sources):
        try:
            module_cfg = {'max_pages': 1, 'type': proxy_source}
            proxied_session = BuildProxiedSession(module_cfg=module_cfg)
            candidate_proxies = proxied_session.refreshproxies()
        except:
            candidate_proxies = []
        if len(candidate_proxies) > 0:
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('True', 'green'), ', '.join([f'{k.upper()}: {v}' for k, v in candidate_proxies[0].items()])])
        else:
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('False', 'red'), 'NULL'])
    # visualize test results
    print('The effectiveness test results of each proxy are as follows:')
    printtable(titles=print_titles, items=print_items)


'''tests'''
if __name__ == '__main__':
    main()