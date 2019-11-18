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
r = {'0099fbdf13ff7db515f262e254c1320c': 0.18433604, '0099fbdf13ff7db515f262e254c1320d': 0.18433604,
     '0099fbdf13ff7db515f262e254c1320e': 0.18433604}


def rest1(**kwargs):
    kwargs.get('a')
    return r


def rest2(**kwargs):
    return r


app.add_route("/r1", rest1)
app.add_route("/r2", rest2)

app.run()
