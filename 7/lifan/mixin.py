'''
知识要求：至少需要学到30章的内容
写个mixin类，并在这个类里面实现一个to_dict的方法：这个方法是把对象的属性序列化成字典的形式。
其他类通过继承这个mixin来继承这个方法。注意：写之前，需要了解mixin是什么，它和子类继承有什么区别。
'''

import json


class MiXin:
    def ToDict(self):
        with open('dict.json', 'w+') as f:
            json.dump(self.stInfo, f)


class StInfo:
    def __init__(self):
        self.stInfo = {}

    def __repr__(self):
        return str(self.stInfo)

    def __setitem__(self, key, value):
        self.stInfo[key] = value




class DictMiXin(MiXin, StInfo): pass


st = DictMiXin()
st['name'],st['age'],st['discipline'] = 'zs',16,'IT'
st.ToDict()

# todict 是把属性转化成字典