# -*- coding: utf-8 -*-
"""新能测试模块

usage:
    import profiler
    ...
    @profiler.profile
    def func(*args, **kwargs):
        ....
"""
import tempfile
import cProfile
import pstats


def profile(column='time', list=5):
    def _profile(function):
        def __profile(*args, **kw):
            s = tempfile.mktemp()
            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            p.sort_stats(column).print_stats(list)
        return __profile
    return _profile
