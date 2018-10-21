#!/bin/python3.6
'''实现斐波那契数列的缓存装饰器'''


import inspect
import datetime
import time
from functools import wraps

local_cache = {}

def fibCache(timeout):
    def _fibCache(fn):
        global local_cache
        @wraps(fn)
        def wrapper(*args,**kwargs):
            #清除缓存
            delete_cache = []
            for k,(_,time) in local_cache.items():
                now = datetime.datetime.now()
                if (now - time).seconds > timeout:
                    delete_cache.append(k)
            for k in delete_cache:
                local_cache.pop(k)

            sig = inspect.signature(fn)
            fn_params = sig.parameters

            param_names = [key for key in fn_params.keys()]
            param_value_dict = {}

            #参数处理
            for i, v in enumerate(args): #args 位置参数
                k = param_names[i]
                param_value_dict[k] = v
            param_value_dict.update(kwargs)

            #缺省值处理
            for k,v in fn_params.items():
                if k not in param_value_dict.keys():
                    param_value_dict[k] = v.default

            key = tuple(sorted(param_value_dict.items()))

            start = datetime.datetime.now()
            if key not in local_cache.keys():
                ret = fn(*args,**kwargs)
                local_cache[key] = (ret,datetime.datetime.now())
            timedelta = (datetime.datetime.now() - start).total_seconds()
            print('time cost:',timedelta)
            return local_cache[key]
        return wrapper
    return _fibCache

@fibCache(3)
def createFibList(n):
    lst = []
    def fibGernerator(n):
        a,b = 0,1
        while n > 0:
            a,b = b,a+b
            n -= 1
            yield a
    time.sleep(1)
    for i in fibGernerator(n):
        lst.append(i)
    return lst

print(createFibList(10))
print(createFibList(10))
time.sleep(4)
print(createFibList(10))
