# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 15:13
# @Author  : Yanlin
# @Email   : 952735981@163.com
# @File    : mydecorator.py
# @Software: PyCharm

# 第五周作业：
# 知识要求：至少需要学到21章的内容
# 1.实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
# 2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，先检测要运行的斐波那契数是否在缓存里面，
# 如果在直接返回结果，否则计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)。
import datetime,inspect
import time
from functools import wraps

# 1.timeit装饰器


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        time_use = (datetime.datetime.now()-start).total_seconds()
        print('函数{}耗时{}s'.format(fn.__name__, time_use))
        return ret
    return wrapper


@timeit
def sum_recursion(nu):
    time.sleep(2)
    its_sum = 0
    for i in range(nu + 1):
        its_sum += i
    return its_sum

# 2.cache装饰器


def cache(fn):
    local_cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        params_name = [key for key in params.keys()]
        params_dict = {}
        for i,v in enumerate(args):
            k = params_name[i]
            params_dict[k] = v
        params_dict.update(kwargs)
        start = datetime.datetime.now()
        for k, v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default
        key = tuple(sorted(params_dict.items()))
        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs)
        delta = (datetime.datetime.now()-start).total_seconds()
        return local_cache[key],delta
    return wrapper


@cache  # fib = cache(fib))
def fib(n):
    time.sleep(1)
    lst =[]
    def fib1(n, pre=0, cur=1):
        lst.append(cur)
        pre, cur = cur, pre+cur
        if n == 2:
            return
        fib1(n-1, pre, cur)
    fib1(n)
    return lst

print(fib(10))
print(fib(10))





