"""编写一个学生管理系统类—Gradebook:
要求能动态的添加学生-name 和学生成绩grades(一个学生可以有个多科的科目成绩)，
并且根据学生名字能算出学生的平均成绩：
提示：可以预先初始化一个字典，用实例字典存储相应的信息"""
from functools import wraps
login_infomation = {'jack':'yuanliang','mage':'123456'}

class Student:
    def __init__(self,name,english,math,chinese,history,science):
        self.name = name
        self.english = english
        self.math = math
        self.chinese = chinese
        self.history = history
        self.science = science

def login(fn):
    #登录验证
    @wraps(fn)
    def wraper(*args,**kwargs):
        userinfo = input('Please enter your username and password').strip().split(' ')
        for k,v in login_infomation.items():
            if userinfo[0] == k and userinfo[1] == v:
                ret = fn(*args, **kwargs)
                return ret
        else:
            print('wrong username or password')
            return
    return wraper

@login
class Gradebook:
    def __init__(self):
        self.info={}
    # 添加信息
    def add_info(self,student:Student):
        self.info[student[0]] = student[1:]
    # 求平均数
    #get_averagegrade=lambda self,name:sum(self.info[name])/len(self.info[name])

    def get_averagegrade(self,name):
        value = sum(self.info[name]) / len(self.info[name]) if name in self.info else  NameError("没有该学生")
        return value



gb = Gradebook()
student = ('jack',90,56,88)
student1 = ('bob',88,97,87,90)

gb.add_info(student)
gb.add_info(student1)


print(gb.get_averagegrade('dog'))
print(gb.get_averagegrade('bob'))

# 看下可以用一个类来实现吗？