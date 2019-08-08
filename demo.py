#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : demo
# @Time         : 2019-08-08 11:15
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import socket
from sanic import Sanic, response

from collections import OrderedDict
from traceback import format_exc  # https://www.cnblogs.com/klchang/p/4635040.html

socket.SO_REUSEPORT = 15
app = Sanic()


# @app.route("/run", methods=["GET", "POST"])
async def handler(request):
    print(request.json)
    print(request.args)
    return response.json(request.json)



app.add_route(handler,"/run", frozenset({"GET", "POST"}))

app.run("0.0.0.0", 9999, debug=True)
