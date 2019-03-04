#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
__title__ = 'example'
__author__ = 'JieYuan'
__mtime__ = '19-3-4'
"""

from .restful import RestfulApi

class Model(RestfulApi):

    def predict(self, feat1, feat2):
        return feat1*feat2

if __name__ == '__main__':
    rest = Model(['feat1', 'feat2'])
    rest.app.run()