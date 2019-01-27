'''
知识要求：至少需要学到30章的内容
写个mixin类，并在这个类里面实现一个to_dict的方法：这个方法是把对象的属性序列化成字典的形式。
其他类通过继承这个mixin来继承这个方法。注意：写之前，需要了解mixin是什么，它和子类继承有什么区别。
'''

import json


class MiXin:
    def ToDict(self):
        return json.dumps(self.__dict__)


class StInfo:
    def __init__(self,name,age,discipline):
        self.name = name
        self.age = age
        self.discipline = discipline

    def __repr__(self):
        return str(self.__dict__)

class DictMiXin(MiXin, StInfo): pass


st = DictMiXin('zs',16,'IT')
print(st)                       #{'name': 'zs', 'age': 16, 'discipline': 'IT'}
print(st.ToDict())              #{"name": "zs", "age": 16, "discipline": "IT"}


# 这个没有问题~