#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-Python.
# @File         : demo
# @Time         : 2019-08-15 10:20
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from iapp import App
import time


class G:
    a = 0


def get_v():
    return G.a


def set_v(v):
    G.a = v


##############update
model_map = {}


def update(**kwargs):
    time.sleep(10)

    model_map.update(kwargs)

    return model_map


f1 = lambda **kwargs: model_map
f2 = lambda **kwargs: 666


def api(**kwargs):
    print(kwargs)
    print(kwargs.get('method')[0])
    a = eval(kwargs.get('method')[0])(**kwargs)
    return a


##############

app = App()
# update
app.add_route("/update", update, time=time.ctime())

app.add_route("/f1", f1, time=time.ctime())

app.add_route("/f2", f2, time=time.ctime())

app.add_route("/api", api, time=time.ctime())

app.run(workers=1)
