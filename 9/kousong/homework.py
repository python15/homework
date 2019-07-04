#nineth week
class Descriptor:
    def __init__(self, fget=None,fset=None,fdeleter=None):
        self.fget = fget
        self.fset = fset
        self.fdeleter = fdeleter

    def __get__(self, instance, owner):return self.fget(instance)
    def __delete__(self,instance):del instance._addr
    def __set__(self,instance,value):
        instance._addr= value
        self.fset(instance,value)

    def setter(self,fdata):
        self.fset = fdata
        return self
    def deleter(self,fdata):
        self.fdeleter = fdata
        return self

class Student:
    def __init__(self,name, addr):
        self._name = name
        self._addr = addr
    @Descriptor #data=Descriptor(data)
    def data(self):
        print(self._name)
        print(self._addr)
    @data.setter
    def data(self,value):pass
    @data.deleter
    def data(self):pass


zs = Student('张三', '武汉')
zs.data
zs.data = '北京'
zs.data
del zs.data
#zs.data