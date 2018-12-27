#!/bin/env python
'''
写个mixin类，并在这个类里面实现一个to_dict的方法：
这个方法是把对象的属性序列化成字典的形式。其他类通过继承这个mixin来继承这个方法。
注意：写之前，需要了解mixin是什么，它和子类继承有什么区别。 
'''
import json
class ToMixin:
	def todict_dict(self):
		return json.dumps(self.__dict__)#可传入参数，选择可序列化的方法，可支持pickle,msgpack

class Animal:
    """基类"""
	def __init__(self,name,color,size,ani_type):
		self.name = name
		self.color  = color
		self.size = size
		self.ani_type = ani_type
	def cry(self):
		pass
	
class Cat(ToMixin,Animal):
	def cry(self):
		print("miao")

cat = Cat('xiaomiaomi','grey','small','miaomi')
print(cat.to_dict())	

# 没有什么问题~