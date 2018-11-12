#!/bin/python3.6
'''实现timeit装饰器，计算函数运行的时间'''


import datetime
import time

def timeit(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        timedelta = (datetime.datetime.now() - start).total_seconds()
        print('time cost:', timedelta)
        return ret
    return wrapper

@timeit
def add(a=10,b=20):
    time.sleep(2)
    return a+b

print(add())

# 其实这个用time 就足够了
# 可以尝试下写过认证的装饰器，把第二周的作业里面的认证改成装饰器的试试