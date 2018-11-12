"""
1.实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，先
  检测要运行的斐波那契数是否在缓存里面，如果在直接返回结果，否则
  计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)。
"""

import inspect
from functools import wraps
import datetime

def timeit(fn):
    @wraps(fn)
    def wapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now()-start).total_seconds()
        print(delta)
        return ret
    return wapper

def cache(fn):
    local_cache = {}
    @wraps(fn)
    def wapper(*args,**kwargs):
        sig = inspect.signature(fn)
        param = sig.parameters   #只读有序字典
        param_names = [key for key in param.keys()]
        param_dict = {}

        #参数处理，构建key
        for i,x in enumerate(args):
            k = param_names[i]
            param_dict[k] = x
        param_dict.update(kwargs)     #此函数无关键字参数
        key = tuple(sorted(param_dict.items()))   #对key进行排序

        #判断是否需要缓存
        if key not in local_cache.keys():
            local_cache[key] = fn(*args,**kwargs)
        #ret = fn(*args,**kwargs)
        return local_cache[key]
    return wapper

@timeit
@cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(40))

# 可以,可以尝试下写过认证的装饰器，把第二周的作业里面的认证改成装饰器的试试