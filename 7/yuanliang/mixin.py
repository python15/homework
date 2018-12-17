'''
知识要求：至少需要学到30章的内容
写个mixin类，并在这个类里面实现一个to_dict的方法：这个方法是把对象的属性序列化成字典的形式。
其他类通过继承这个mixin来继承这个方法。注意：写之前，需要了解mixin是什么，它和子类继承有什么区别。
'''

import json
import msgpack
import pickle

class SerializationMixin:
    def to_dict(self,data,t='json'):
        if t == 'json':
            return json.dumps(data)
        if t == 'msgpack':
            return msgpack.packb(data)
        if t == 'pickle':
            return pickle.dumps(data)

class Students:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight =weight
    @property
    def test(self):
        return self.name,self.age,self.weight

class Printtest(SerializationMixin,Students):pass

pt=Printtest('JACK',14,89)
print(Printtest.mro())
print(pt.test)
print(pt.to_dict(pt.__dict__,t='json'))

# 这个没有什么问题