# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 15:09
# @Author  : Yanlin
# @Email   : 952735981@163.com
# @File    : MyMixin.py
# @Software: PyCharm

# 第七周作业(11.5-11.11）
# 本周作业如下：
# 知识要求：至少需要学到30章的内容
# 写个mixin类，并在这个类里面实现一个to_dict的方法：这个方法是把对象的属性序列化成字典的形式。
# 其他类通过继承这个mixin来继承这个方法。注意：写之前，需要了解mixin是什么，它和子类继承有什么区别。

import pickle
import json
import msgpack

class SuperToDictMixin:
    def to_dict(self):
        print('*'*10+'Welcome to use Mixin!'+'*'*10)


class ToDictMixin(SuperToDictMixin):
    def to_dict(self, ftype='pickle'):
        super().to_dict()
        if ftype == 'pickle':
            return pickle.dumps(self.__dict__)
        elif ftype == 'json':
            return json.dumps(self.__dict__)
        elif ftype == 'msgpack':
            return msgpack.packb(self.__dict__)
        else:
            return 'error'


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def eat(cls):
        cls.commoneat = 'common eat'

    @staticmethod
    def static_method():
        print('cls static method')


class Man(ToDictMixin,People):
    pass


man1 = Man('zhoulinji',25)
m1 = man1.to_dict('pickle')
print(pickle.loads(m1))


