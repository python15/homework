# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengcheng
#  commit_day:   2018-09-26
'''
知识要求：至少需要学到21章的内容
1.实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，先检测要运行的斐波那契数是否在缓存里面，如果在直接返回结果，否则计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)
'''

import sys,os
import re
import datetime,time
from functools import wraps
import inspect

def logger(fn):
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        x = fn(*args,**kwargs)
        
        dur = datetime.datetime.now() - start
        print("func {} token {}s".format(fn.__name__,dur.total_seconds()))
        return x
    return wrapper

def mag_cache(fn):
    local_cache = {}

    @wraps(fn)
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        
        params_names = [key for key in params.keys()]
        params_dict = {}
        
        for i,v in enumerate(args):
            k = params_names[i]
            params_dict[k] = v
        params_dict.update(kwargs)
        for k,v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default
        key = tuple(sorted(params_dict.items()))
        if key not in local_cache.keys():
            local_cache[key] = fn(*args,**kwargs)
        return local_cache[key]
    return wrapper

@logger
@mag_cache
def fib(x):
    a = 0
    b = 1
    n = 1
    c = []
    time.sleep(3)
    while n<=x:
        c.append(b)
        a,b = b,a+b
        n = n + 1
    return c  

print(fib(10))
print(fib(10))

# 逻辑上没有什么问题，用到了 inspect，看来对一些内置库很熟悉
# 可以尝试下写过认证的装饰器，把第二周的作业里面的认证改成装饰器的试试