# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 15:11
# @Author  : Yanlin
# @Email   : 952735981@163.com
# @File    : Gradebook.py
# @Software: PyCharm

# 第六周作业：
# 知识要求：至少需要学到30章的内容
# 编写一个学生管理系统类—Gradebook:
# 要求能动态的添加学生-name 和学生成绩grades(一个学生可以有个多科的科目成绩)，并
# 且根据学生名字能算出学生的平均成绩：
# 提示：可以预先初始化一个字典，用实例字典存储相应的信息

class Gradebook:
    def __init__(self):
        self.dict_of_grades = {}

    def set_grades(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade
        self.dict_of_grades[(name,subject)] = grade

    def gradeavg(self, name):
        sum_of_grades = 0
        subjects = 0
        for k,v in self.dict_of_grades.items():
            a, b = k
            if a == name:
                sum_of_grades += v
                subjects += 1
        if subjects > 0:
            return sum_of_grades/subjects
        else:
            return "Student not exist!"


if __name__ == '__main__':
    gr = Gradebook()
    gr.set_grades('zansan','math',78.5)
    gr.set_grades('zansan','english',88)
    print('学生平均成绩为：{}'.format(gr.gradeavg('zansan')))

# 有个property 装饰方法，你可以看看，
# 可以加个认证部分，结合下咱们的装饰器试试