#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""程序片函数运行时间测量模块
usage:
    from timer import Timer
    ...
    with Timer():
        ...
"""
import gc
import timeit


class Timer(object):

    def __init__(self, timer=None, disable_gc=False,
                 verbose=False, program=None):
        if timer is None:
            timer = timeit.default_timer
        self.timer = timer
        self.disable_gc = disable_gc
        self.verbose = verbose
        self.start = self.end = self.interval = None
        self.program = program

    def __enter__(self):
        if self.disable_gc:
            self.gc_state = gc.isenabled()
            gc.disable()
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        self.end = self.timer()
        if self.disable_gc and self.gc_state:
            gc.enable()
        self.interval = (self.end - self.start)*1000
        if self.verbose:
            if self.program:
                s = ''.join([self.program, 'takes {0} ms'.format(
                    self.interval)])
            else:
                s = 'Takes {0} ms'.format(self.interval)
            print(s)
