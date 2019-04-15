# -*- coding: utf-8 -*-
import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()


# 根据关键词搜索公众号
def search_name():
    name = input("请输入你想搜索的公众号：\n")
    res = ws_api.search_gzh(name)
    for x in res:
        print(x,'\n')

search_name()