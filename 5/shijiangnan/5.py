'''
知识要求：至少需要学到21章的内容
1.实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，先检测要运行的斐波那契数是否在缓存里面，如果在直接返回结果，否则计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)。
'''
#1
import datetime
def fhhs(fn):
    def jlruntime(*args,**kwargs):
        print("start")
        starttime=datetime.datetime.now()
        sumz=fn(*args,**kwargs)
        endtime=datetime.datetime.now()
        time_difference=(endtime - starttime).total_seconds()
        print("running times is {}".format(time_difference))
        return sumz
    return jlruntime
@fhhs #summationt=fhhs(summationt)
def summationt(x):
    sum=0
    for i in x:
        sum+=i
    return sum


print(summationt(range(10000)))


#2

from functools import wraps
def cachegnzs(hs):
    cache_storage={}
    @wraps(hs) #cache2=wraps(cache2)
    def cache2(*args,**kwargs):
        for i in args:
            if i in cache_storage.keys():
                print("%s is in cache!!!" % (cache_storage[i]))
                return cache_storage[i]
            else:
                result=hs(*args,**kwargs)
                cache_storage[i]=result
                print("%s is not in cache!!! write in!!!" % (cache_storage[i]))
                return result
    return cache2

@cachegnzs #fibgetvalue=cachegnzs(fibgetvalue)
def fibgetvalue(n):
    fib_nblist=[]
    def fibnum(n,a=0,b=1):
        if n>=1:
            #print(b)
            fib_nblist.append(b)
            a,b=b,a+b
            fibnum(n-1,a,b)
    fibnum(n)
    return fib_nblist[n-1]

while True:
    inputfibnum=input("请输入斐波那契数序号:")
    if inputfibnum=='q':
        break
    elif inputfibnum.isdigit():
        inputfibnumint=int(inputfibnum)
        print(fibgetvalue(inputfibnumint))
    else:
        print("Please check that the input is correct.")
