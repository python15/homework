'''
1.实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，先检测要运行的斐波那契数是否在缓存里面，
如果在直接返回结果，否则计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)。
'''

import datetime, time, inspect, random
from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        x = fn(*args, **kwargs)
        stop = (datetime.datetime.now() - start).total_seconds()
        print("The function runs at {}".format(stop))
        return x

    return wrapper


def lCache(overdue):
    def _Cache(fn):
        localCache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):
            def cacheOverdue(overdue):
                timeCache = []
                for k, (_, tm) in localCache.items():
                    if datetime.datetime.now().timestamp() - tm > overdue:
                        timeCache.append(k)
                for k in timeCache:
                    localCache.pop(k)

            cacheOverdue(overdue)

            def makeKey(args, kwargs):
                sig = inspect.signature(fn)
                params = sig.parameters
                param_name = [key for key in params.keys()]
                param_dict = {}
                for i, v in enumerate(args):
                    k = param_name[i]
                    param_dict[k] = v
                else:
                    param_dict.update(kwargs)
                for k, v in params.items():
                    if k not in param_dict.keys():
                        param_dict[k] = v.default
                key = tuple(sorted(param_dict.items()))
                return key

            key = makeKey(args, kwargs)

            if key not in localCache.keys():
                localCache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())

            return localCache[key]

        return wrapper

    return _Cache


@logger
@lCache(8)
def fib(indexC, index=1):
    lst0 = [0, 1]
    while True:
        if index == indexC: break
        sum = lst0[-2] + lst0[-1]
        lst0.append(sum)
        index += 1
    return len(lst0)


while True:
    number = input("Please enter a number to start calculation or enter q to exit: ")
    if number == 'q': break
    print("First computation: {}\n".format(fib(int(number))))
    time.sleep(6)
    print("Second cache calculation: {}\n".format(fib(int(number))))

'''
Please enter a number to start calculation or enter q to exit: 300000
The function runs at 9.303034
First computation: (300001, 1542189841.096914)

The function runs at 0.00181
Second cache calculation: (300001, 1542189841.096914)
'''
