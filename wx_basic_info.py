# -*- coding: utf-8 -*-
import wechatsogou


ws_api = wechatsogou.WechatSogouAPI()


# 搜索指定公众号基本信息
def search_basic_info():
    name = input("请输入你想搜索的公众号：\n")
    res = ws_api.get_gzh_info(name)
    print(res)
search_basic_info()