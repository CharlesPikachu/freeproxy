'''
Function:
    Github star某项目的用户数据爬虫
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import pickle
import requests
from tqdm import tqdm
from freeproxy import freeproxy


'''Github star某项目的用户数据爬虫'''
class GithubStarPeople():
    def __init__(self, username='996icu', reponame='996.ICU', num_pages=5300, access_tokens=None, **kwargs):
        if access_tokens is None:
            access_tokens = []
        self.username = username
        self.reponame = reponame
        self.num_pages = num_pages
        self.access_tokens = access_tokens
        self.api_url = 'https://api.github.com/repos/{}/{}/stargazers?page={}'
        self.fp_client = freeproxy.FreeProxy()
    '''run'''
    def run(self):
        # 构造所有star的人的url
        star_urls = []
        for page in range(self.num_pages):
            url = self.api_url.format(self.username, self.reponame, page)
            star_urls.append(url)
        # 爬取所有用户链接
        user_info_urls, session = [], requests.Session()
        for url in tqdm(star_urls):
            while True:
                headers = self.getheaders()
                try:
                    response = session.get(url, headers=headers)
                    response_json = response.json()
                    break
                except:
                    session = requests.Session()
            if 'message' in response_json and \
                response_json['message'] == 'In order to keep the API fast for everyone, pagination is limited for this resource. Check the rel=last link relation in the Link response header to see how far back you can traverse.':
                break
            for item in response_json:
                if not isinstance(item, dict): 
                    continue
                if ('url' in item) and (item['url'] not in user_info_urls):
                    user_info_urls.append(item['url'])
        self.save(user_info_urls, 'user_info_urls')
        print(f'[INFO]: 共获得{len(user_info_urls)}条用户信息链接')
        # 爬取所有用户信息
        user_infos, session = [], requests.Session()
        for url in tqdm(user_info_urls):
            while True:
                headers = self.getheaders()
                try:
                    response = session.get(url, headers=headers)
                except:
                    session = self.getsession()
                    continue
                if response.status_code == 200 and 'id' in response.json(): 
                    break
                elif response.json()['message'] == 'Not Found':
                    response = None
                    break
                else:
                    session = self.getsession()
            if response is None: continue
            info = response.json()
            user_infos.append(info)
        print(f'[INFO]: 共获得{len(user_infos)}条用户数据')
        self.save(user_infos, 'user_infos')
    '''save'''
    def save(self, infos, savename=None):
        savename = self.reponame if savename is None else savename
        with open(savename+'.pkl', 'wb') as fp:
            pickle.dump(infos, fp)
        return True
    '''get headers'''
    def getheaders(self, with_access_token=True):
        if not self.access_tokens: 
            with_access_token, access_token = False, '微信公众号: Charles的皮卡丘'
        else:
            access_token = random.choice(self.access_tokens)
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {access_token}',
        }
        if not with_access_token: headers.pop('Authorization')
        return headers
    '''get session'''
    def getsession(self):
        if random.random() > 0.5: return requests.Session()
        while True:
            try:
                session = self.fp_client.getrandomproxysession()
                break
            except:
                continue
        return session


'''run'''
if __name__ == '__main__':
    client = GithubStarPeople()
    client.run()