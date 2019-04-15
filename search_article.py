# -*- coding: utf-8 -*-
import wechatsogou
import datetime

ws_api = wechatsogou.WechatSogouAPI()
week = datetime.datetime.now()
day = week.weekday()
day_wordkey = {0: "美容干货", 1: "明星整形", 2: "涨点姿势", 3: "明星整形", 4: "涨点姿势", 5: "团建", 6: "抗衰"}


# 搜索关键词的所有文章
def search_article():
    res = ws_api.search_article(day_wordkey[day])
    print('搜索结果如下:')
    for c in res:
        a = c['article']
        g = c['gzh']
        print('公众号：' + g['wechat_name'])
        print('标题：' + a['title'], '\n', '链接：' + a['url'], '\n', '摘要：' + a['abstract'], '\n')


search_article()
