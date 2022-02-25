'''
Function:
    Github star某项目的用户数据分析
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import pickle
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType


'''画饼图'''
def drawpie(title, infos, savepath):
    pie = Pie(init_opts=dict(theme='westeros', page_title=title)).add(title, data_pair=tuple(zip(infos.keys(), infos.values())), rosetype='area')
    pie.set_global_opts(title_opts=opts.TitleOpts(title=title))
    pie.render(savepath)


'''画柱状图'''
def drawbar(title, data, savepath):
    bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
          .add_xaxis(list(data.keys()))
          .add_yaxis('', list(data.values()))
          .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-25)),
                           title_opts=opts.TitleOpts(title=title, pos_left='center'), legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%')))
    bar.render(savepath)


'''run'''
if __name__ == '__main__':
    user_infos = pickle.load(open('user_infos.pkl', 'rb'))
    # 反对996的人主要是什么公司的
    companies_record = {}
    for user_info in user_infos:
        company = user_info['company']
        if not company: continue
        company = company.lower().replace('@', '')
        if company == 'null' or company == 'none' or company == 'china': continue
        if '腾讯' in company or 'tencent' in company: company = '腾讯'
        if '字节' in company or 'bytedance' in company: company = '字节'
        if '阿里' in company or 'alibaba' in company or 'alipay' in company: company = '阿里'
        if '网易' in company or 'netease' in company: company = '网易'
        if '京东' in company or 'jd' in company: company = '京东'
        if '百度' in company or 'baidu' in company: company = '百度'
        if '微软' in company or 'microsoft' in company: company = '微软'
        if '美团' in company or 'meituan' in company: company = '美团'
        if 'university' in company or 'uestc' in company or 'ustc' in company: company = '高校学生'
        if '滴滴' in company or 'didi' in company: company = '滴滴'
        if '小米' in company or 'xiaomi' in company: company = '小米'
        if '谷歌' in company or 'google' in company: company = '谷歌'
        if 'B站' in company or 'bilibili' in company: company = 'B站'
        if company in companies_record:
            companies_record[company] += 1
        else:
            companies_record[company] = 1
    companies_record = dict(sorted(companies_record.items(), key=lambda x: x[1], reverse=True)[:10])
    drawbar('反对996的员工数量TOP10所在公司', companies_record, '反对996的员工数量TOP10所在公司.html')
    # 反对996的人里有多少是在社区是有影响力的
    influence_power_record = {'粉丝数量100-200': 0, '粉丝数量200-300': 0, '粉丝数量300-400': 0, '粉丝数量400-500': 0, '粉丝数量500-1000': 0, '粉丝数量1000以上': 0}
    for user_info in user_infos:
        if user_info['followers'] >= 100 and user_info['followers'] < 200:
            influence_power_record['粉丝数量100-200'] += 1
        elif user_info['followers'] >= 200 and user_info['followers'] < 300:
            influence_power_record['粉丝数量200-300'] += 1
        elif user_info['followers'] >= 300 and user_info['followers'] < 400:
            influence_power_record['粉丝数量300-400'] += 1
        elif user_info['followers'] >= 400 and user_info['followers'] < 500:
            influence_power_record['粉丝数量400-500'] += 1
        elif user_info['followers'] >= 500 and user_info['followers'] < 1000:
            influence_power_record['粉丝数量500-1000'] += 1
        elif user_info['followers'] >= 1000:
            influence_power_record['粉丝数量1000以上'] += 1
    drawpie('反对996的人里有多少是在社区是有影响力的', influence_power_record, '反对996的人里有多少是在社区是有影响力的.html')
    # 点赞用户都是什么时候注册的
    created_year_record = {}
    for user_info in user_infos:
        created_at = user_info['created_at'].split('-')[0]
        if created_at in created_year_record:
            created_year_record[created_at] += 1
        else:
            created_year_record[created_at] = 1
    created_year_record = dict(sorted(created_year_record.items(), key=lambda x: x[0], reverse=False))
    drawbar('点赞用户都是什么时候注册的', created_year_record, '点赞用户都是什么时候注册的.html')
    # 点赞用户的邮箱域名统计
    email_record = {}
    for user_info in user_infos:
        email = user_info['email']
        if email is None: continue
        email = email.split('@')[-1]
        if email in email_record:
            email_record[email] += 1
        else:
            email_record[email] = 1
    email_record = dict(sorted(email_record.items(), key=lambda x: x[1], reverse=True)[:10])
    drawbar('点赞用户的邮箱域名统计', email_record, '点赞用户的邮箱域名统计.html')