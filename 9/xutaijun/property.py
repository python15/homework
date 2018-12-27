#!/bin/env python

class Property:
    def __init__(self,fget,fset=None):
        self.fget = fget
        self.fset = fset
    def __get__(self,instance,owner):
        if instance is not None:
            print(instance)
            print(owner)
            return self.fget(instance)
        return self
    def __set__(self, instance, value):
        print(",",self.fset)
        self.fset(instance,value)
    def setter(self,fn):
        self.fset = fn
        return self
class A:
    def __init__(self,data):
        self._data = data
    @Property #data = Property(data)
    def data(self):
        return self._data

    @data.setter # data = data.setter(data)
    def data(self,value):
        self._data = value

a = A(100)
print(a.data)

print("="*59)
a.data = 200
# 没有什么太大的问题，少个del的方法，记得加上