# -*- coding: utf-8 -*-
import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()

# 搜索关键词的所有文章
def search_article():
    keyword = input("请输入要搜索的关键词:\n")
    res = ws_api.search_article(keyword)
    print('搜索结果如下:')
    for c in res:
        a = c['article']
        g = c['gzh']
        print('公众号：' + g['wechat_name'])
        print('标题：' + a['title'], '\n', '链接：' + a['url'], '\n', '摘要：' + a['abstract'], '\n')


search_article()
