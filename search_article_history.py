# -*- coding: utf-8 -*-
import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()

# 搜索特定的一组微信公众号
wx_list = ["医美圈",  "医美视界", "皮秒"]


# 根据关键词搜索公众号的文章
def search_article():
    for l in wx_list:
        res = ws_api.get_gzh_article_by_history(l)
        article = res['article']
        for a in article:
            print('公众号:' + l)
            print('标题：' + a['title'])
            print('摘要：' + a['abstract'] + "...")
            print('文章链接：' + a['content_url'])
            if a['source_url'] == "":
                print('阅读原文链接：无')
            print('\n')


search_article()
