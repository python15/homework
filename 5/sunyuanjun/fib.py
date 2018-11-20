import datetime
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        timeuse = (datetime.datetime.now() - start).total_seconds()
        print(timeuse)
        return ret
    return wrapper

def cache(fn):
    caches = {}
    @wraps(fn)
    def wrapper(*args,**kwargs):
        for i in args:
            if i in caches.keys():
                return caches[i]
            else:
                ret = fn(*args,**kwargs)
                caches[i] = ret
                return ret
    return wrapper

@timeit
@cache
def fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

while True:
    num = int(input('请输入一个整数:'))
    if num > 0:
        print(fib(num))
    else:
        print('程序结束')
        break


# 可以，功能上没有什么问题了