#!/bin/env python

import datetime
from functools import wraps
import inspect
#count the run-date
def timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        after = datetime.datetime.now()
        res = fn(*args,**kwargs)
        timeit = (datetime.datetime.now()-after).total_seconds()
        print("the run-date is :{}".format(timeit))
        return res
    return wrapper

#cache fib_number , beacuse only have a location parameter.so just only cache location parameter.
def cache_fib(fn):
    cache_dict={}
    def wrapper(*args,**kwargs):
        key=0
        for i in args:
            key=i
        if key not in cache_dict.keys():
            res = fn(*args,**kwargs)
            cache_dict[key] = res,datetime.datetime.now().timestamp()
        return cache_dict[key][0]
    return wrapper

#fib generation function
@timeit
@cache_fib
def fib(n:int):
    st_list=[1,1]
    for i in range(2,n):
        st_sum=st_list[i-1]+st_list[i-2]
        st_list.append(st_sum)
    return st_list
#call function
def show_fib(n):
    print("{}:{}".format(n,fib(n)))

#main function
if __name__=="__main__":
    while(True):
        input_num=input("===============================\nplease input your fib number\n and if the 'q' is quit \n>>>>>")
        if input_num == 'q':
            break
        else:
            input_num=int(input_num)
        show_fib(input_num)
