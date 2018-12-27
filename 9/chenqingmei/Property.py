#!/bin/python3.6
class Property:
    def __init__(self, fget = None, fset = None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def setter(self, value):
        self.fset = value
        return self



class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @Property   # age = Property(age)
    def age(self):
        return self.__age

    @Property    #  name = Property(name)
    def name(self):
        return self.__name

    @age.setter  # age = age.setter(age)  =>  age = Property(age).setter(age)
    def age(self, value):
        self.__age = value



s = Student('Lily', 18)

print(s.name)
print(s.age)
s.age = 10
print(s.__dict__)

# 少个del的方法 加上



