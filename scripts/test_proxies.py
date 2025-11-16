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
    print_titles, print_items = ['Source', 'Effectiveness', 'Retrieved Examples', 'Total'], []
    for proxy_source in tqdm(proxy_sources):
        try:
            module_cfg = {'max_pages': 1, 'type': proxy_source}
            proxied_session = BuildProxiedSession(module_cfg=module_cfg)
            candidate_proxies = proxied_session.refreshproxies()
        except:
            candidate_proxies = []
        if len(candidate_proxies) > 0:
            print_items.append([
                proxy_source.removesuffix('ProxiedSession'), colorize('True', 'green'), [f'{v}' for v in candidate_proxies[0].values()][0],
                colorize(str(len(candidate_proxies)), 'number'),
            ])
        else:
            print_items.append([proxy_source.removesuffix('ProxiedSession'), colorize('False', 'red'), 'NULL', colorize(str(len(candidate_proxies)), 'number')])
    # visualize test results
    print('The effectiveness test results of each proxy are as follows:')
    printtable(titles=print_titles, items=print_items, terminal_right_space_len=1)


'''tests'''
if __name__ == '__main__':
    main()