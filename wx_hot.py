# -*- coding: utf-8 -*-
from pprint import pprint
from wechatsogou import WechatSogouAPI, WechatSogouConst

ws_api = WechatSogouAPI()
gzh_articles = ws_api.get_gzh_article_by_hot(WechatSogouConst.hot_index.food)
for i in gzh_articles:
    pprint(i)
    pprint('\n')
