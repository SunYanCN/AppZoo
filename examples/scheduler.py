#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : scheduler
# @Time         : 2019-09-02 13:17
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import asyncio

from datetime import datetime, time, timedelta
from iapp.scheduler import SanicScheduler, task

import jieba
from iapp import App

app = App(debug=True)
scheduler = SanicScheduler(app.app, False)  # CST 非 UTC

c1 = {}
c2 = {}


@task(timedelta(seconds=3))  # 实现初始化
def hello1(app):
    c1['n'] = c1.get('n', 0) + 1

    print(c1)
    print("Hello, {0}".format(app), datetime.now())



@task(timedelta(minutes=2), timedelta(seconds=10))  # 实现初始化
def hello2(app):
    """Runs the function every 2 minutes after 10 seconds."""
    print(c2)
    c2['n'] = c2.get('n', 0) + 1
    print("Hello, {0}".format(app), datetime.now())


pred1 = lambda **kwargs: c1
pred2 = lambda **kwargs: c2

app.add_route("/f1", pred1, version="1")
app.add_route("/f2", pred2, version="2")
if __name__ == '__main__':
    app.run()
