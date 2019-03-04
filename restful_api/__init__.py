#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '__init__.py'
__author__ = 'JieYuan'
__mtime__ = '19-3-4'
"""

from collections import OrderedDict

from vibora import Vibora, Request
from vibora.responses import JsonResponse


class Api(object):

    def __init__(self, fields, routing, predict, app=Vibora()):
        self.fields = fields
        self.input = OrderedDict()
        self.output = OrderedDict()
        self.app = app
        self.predict = predict
        self.app.route(routing, methods=['POST'])(self.home)

    async def home(self, request: Request):
        request = await request.stream.read()
        try:
            request = eval(request)
        except Exception as e:
            self.output['Request Error'] = str(e)

        try:
            for field in self.fields:
                self.input[field] = request.get(field)
            self.output['Probability'] = self.predict(*self.input.values())

        except Exception as e:
            self.output['Predict Error'] = str(e)
        finally:
            self.output['Request'] = request

        return JsonResponse(self.output)


if __name__ == '__main__':
    pred1 = lambda x, y: x + y
    pred2 = lambda x, y: x - y

    api = Api(['feat1', 'feat2'], '/post1', pred1)
    api = Api(['feat1', 'feat2'], '/post2', pred2, app=api.app)
    api.app.run()
