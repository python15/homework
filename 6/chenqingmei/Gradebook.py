#!/bin/python3.6

from week6.Student import Student

def printTitle(fn):
    def wrapper(*args, **kwargs):
        #print("Name\tChinese\tMath\tEnglish")
        print('{:<8}{:^10}{:^10}{:^10}'.format('Name', 'Chinese', 'Math', 'English'))
        ret = fn(*args, **kwargs)
        return ret
    return wrapper

class Gradebook:
    STUDENTS = {}

    @classmethod
    def add(cls, stu: Student):
        cls.STUDENTS[stu.name] = stu

    @classmethod
    def remove(cls, name):
        return(cls.STUDENTS.pop(name, None))

    @classmethod
    def show(cls, name):
        if not cls.STUDENTS.get(name):
            print('Cannot find this student!')
        else:
            print('{}: Chinese {}\t Math {}\t English {}'.format(name, cls.STUDENTS[name].ch,
                                                                 cls.STUDENTS[name].math, cls.STUDENTS[name].en))

    @classmethod
    @printTitle
    def showAll(cls):
        for key in cls.STUDENTS.keys():
            print('{:<8}{:^10}{:^10}{:^10}'.format(key, cls.STUDENTS[key].ch, cls.STUDENTS[key].math, cls.STUDENTS[key].en))

    @classmethod
    def average(cls, name):
        return name, (cls.STUDENTS[name].ch + cls.STUDENTS[name].math+ cls.STUDENTS[name].en) / 3

    @classmethod
    def changeCh(cls, name, ch):
        cls.STUDENTS[name].ch = ch

    @classmethod
    def changeMath(cls, name, math):
        cls.STUDENTS[name].math = math

    @classmethod
    def changeEn(cls, name, en):
        cls.STUDENTS[name].en = en

    @classmethod
    def batchChange(cls, name, ch, math, en):
        cls.STUDENTS[name].ch = ch
        cls.STUDENTS[name].math = math
        cls.STUDENTS[name].en = en

    @classmethod
    def changeName(cls, oldname, newname):
        if not cls.STUDENTS.get(oldname, None):
            print('Cannot find this student!')
        else:
            cls.STUDENTS[oldname].name = newname
            cls.STUDENTS[newname] = cls.STUDENTS[oldname]
            cls.STUDENTS.pop(oldname)

