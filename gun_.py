#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : gunicorn
# @Time         : 2019-11-21 11:00
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import os

os.system("gunicorn -w 4 -b 0.0.0.0:8899 example:app --worker-class sanic.worker.GunicornWorker")
