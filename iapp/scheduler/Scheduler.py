#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : Scheduler
# @Time         : 2019-12-10 13:50
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler(object):
    """learning: https://blog.csdn.net/somezz/article/details/83104368"""

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_job(self, func, trigger='interval', args=None, kwargs=None, **trigger_args):
        """
        The ``trigger`` argument can either be:
          #. the alias name of the trigger (e.g. ``date``, ``interval`` or ``cron``), in which case
            any extra keyword arguments to this method are passed on to the trigger's constructor
          #. an instance of a trigger class

        :param func: callable (or a textual reference to one) to run at the given time
        :param str|apscheduler.triggers.base.BaseTrigger trigger: trigger that determines when
            ``func`` is called
        :param list|tuple args: list of positional arguments to call func with
        :param dict kwargs: dict of keyword arguments to call func with
        """
        assert callable(func), "TODO: callable function"

        self.scheduler.add_job(func, trigger, args, **trigger_args)

    def start(self):
        self.scheduler.start()


if __name__ == '__main__':
    def task1(x):
        print(x)
        import logging
        import time
        logging.warning(f'Task1: {time.ctime()}')


    def task2():
        import logging
        import time
        logging.warning(f'Task2: {time.ctime()}')


    scheduler = Scheduler()
    scheduler.add_job(task1, 'interval', seconds=3, args=('定时任务',))
    scheduler.add_job(task2, 'interval', seconds=10)
    scheduler.start()

    while 1:
        pass
