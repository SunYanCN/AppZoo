#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '__init__.py'
__author__ = 'JieYuan'
__mtime__ = '19-3-4'
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'xiangkan_ctr'
__author__ = 'JieYuan'
__mtime__ = '19-1-24'
"""

from collections import OrderedDict

from vibora import Vibora, Request
from vibora.responses import JsonResponse


class RestfulApi(object):

    def __init__(self, fields, routing='/home'):
        self.fields = fields
        self.input = OrderedDict()
        self.output = OrderedDict()
        self.app = Vibora()
        self.app.route(routing, methods=['POST'])(self.home)

    async def home(self, request: Request):
        request = await request.stream.read()
        try:
            request = eval(request)
        except Exception as e:
            self.output['request error'] = str(e)

        try:
            for field in self.fields:
                self.input[field] = request.get(field)
            self.output['prob'] = self.predict(*self.input.values())

        except Exception as e:
            self.output['predict error'] = str(e)
        finally:
            self.output['request'] = request

        return JsonResponse(self.output)

    def predict(self, *args):
        pass
