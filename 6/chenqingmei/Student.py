#!/bin/python3.6

class Student:
    def __init__(self, name, ch=0, math=0, en=0):
        self.__name = name
        self.__ch = ch
        self.__math = math
        self.__en = en

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def ch(self):
        return self.__ch

    @ch.setter
    def ch(self,value):
        self.__ch = value

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self,value):
        self.__math = value

    @property
    def en(self):
        return self.__en

    @en.setter
    def en(self, value):
        self.__en = value

    def average(self):
        return (self.ch + self.math + self.en) / 3

    def show(self):
        print('{}: Chinese: {} Math: {} English:{}'.format(self.name, self.ch, self.math, self.en))
