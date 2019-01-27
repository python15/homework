'''
实现一个Property装饰器，可以把方法装饰成同一个属性名
'''


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def setter(self, fn):
        self.fset = fn
        return self

    def __set__(self, instance, value):
        self.fset(instance, value)

    def deleter(self, fn):
        self.fdel = fn
        return self

    def __delete__(self, instance):
        self.fdel(instance)


class Student:
    '''
       Student management
    '''

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    @MyProperty
    def mg(self):
        return self.name, self.addr

    @mg.setter
    def mg(self, value):
        self.age = value

    @mg.deleter
    def mg(self):
        del self.age


zs = Student('张三', '武汉')
print(zs.__doc__)
print(zs.mg)
zs.mg = 26
print(zs.__dict__)
del zs.mg
print(zs.__dict__)

'''
localhost:lifan Fan$ python3.6  Property.py

       Student management

('张三', '武汉')
{'name': '张三', 'addr': '武汉', 'age': 26}
{'name': '张三', 'addr': '武汉'}
'''
# 很棒~