#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : example
# @Time         : 2019-08-08 14:30
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import sys

print(sys.argv)
import jieba
from iapp import App

pred1 = lambda **kwargs: kwargs['x'] + kwargs['y']
pred2 = lambda x=1, y=1: x - y
pred3 = lambda text='小米是家不错的公司': jieba.lcut(text)

app = App(debug=True)
app.add_route("/f1", pred1, version="1")
app.add_route("/f2", pred2, version="2")
app = app.app
if __name__ == '__main__':
    app.run(access_log=True)
