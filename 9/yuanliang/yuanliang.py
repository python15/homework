"""
实现一个Property装饰器，可以把方法装饰成同一个属性名

"""
class Property:
    def __init__(self,fn,fset=None, fdel=None):
        self.fn = fn
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        if instance is not None:
            return self.fn(instance)
        return self
    def __set__(self, instance, value):
        if callable(self.fset):
            self.fset(instance,value)
        else:
            raise AttributeError('{}can not assign'.format(self.fset.__name__))
    def __delete__(self, instance):
        if callable(self.fset):
            self.fdel(instance)
    def setter(self,fn):
        self.fset = fn
        return self
    def deleter(self,fn):
        self.fdel = fn
        return self

class A:
    def __init__(self,data):
        self._data = data
    @Property#data = Property(data)
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        self._data = value
    @data.deleter
    def data(self):
        del self._data

if __name__ == "__main__":
    a= A('123')
    print(a.data)
    a.data='456'
    print(a.data)
    del a.data
    print(a.data)

