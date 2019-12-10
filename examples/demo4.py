#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-Python.
# @File         : demo
# @Time         : 2019-08-15 10:20
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
import time
import logging
from datetime import datetime
from iapp import App

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

dic = {}


@scheduler.scheduled_job('interval', seconds=3)
def task():
    """更新变量"""
    logging.warning('Tick! The time is: %s' % datetime.now())
    dic['t'] = time.ctime()


scheduler.start()





# App
f1 = lambda **kwargs: dic
f2 = lambda **kwargs: dic

app = App()
app.add_route("/f1", f1, time=time.ctime())
app.add_route("/f2", f2, time=time.ctime())

if __name__ == '__main__':
    app.run(workers=1, debug=True, access_log=True, port=9955)
