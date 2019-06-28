#fifth week1

import datetime


def logger(fn):
    def _logger(*args,**kwargs):
        now = datetime.datetime.now()
        ret=fn(*args,**kwargs)
        
        dalta=(datetime.datetime.now() - now).total_seconds()
        
        return(dalta)
    return _logger

@logger
def add():
    a=0
    for i in range(10000000):
        a=a+i
    return(a)
print(add())

"""
def _logger(*args,**kwargs):
"""
