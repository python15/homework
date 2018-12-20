#!/bin/env python3
#auther ted
class Student:
    """学生信息类"""
    def __init__(self):
        self.name = ''
        self.id = ''
    #可增加学生信息

class GradesBook:
    """成绩管理类"""
    def __init__(self):
        self.scoredict = {}

    #学生成绩的增加
    def add_score(self):
        self.scoredict['English'] = input("Please input English Score:")
        self.scoredict['Math'] = input("Please input Math Score:")
        self.scoredict['Chinese'] = input("Please input Chinese Score:")

    #学生成绩的更改
    def change_score(self,scoredict):
        self.scoredict = scoredict
        while True:
            print("\n1.change English\n2.change Math\n3.change Chinese\nQ exit.")
            n_choose = input("do you want change ones:")
            if n_choose == '1':
                self.scoredict['English'] = input("Please input English Score:")
            elif n_choose == '2':
                self.scoredict['Math'] = input("Please input Math Score:")
            elif n_choose == '3':
                self.scoredict['Chinese'] = input("Please input Chinese Score:")
            else:
                break

    @property
    def get_score(self):
        return self.scoredict


class StudentMan:
    """学生管理类"""
    def __init__(self):
        self._student_man = {}

    def add_student(self,stu,sco):
        stu.name = input("Please input student's name:")
        if stu.name not in  self._student_man.keys():
            sco.add_score()
        else:
            print("student exists")
        self._student_man[stu.name]=sco.get_score
    
    def change_student(self,stu,sco):
        stu.name = input("Please input student's name:")
        if stu.name in  self._student_man.keys():
            sco.change_score(self._student_man[stu.name])
        else:
            print('!'*3,"student doesn't exists",'!'*3)

    def all_student(self,man):
        """格式化输出，简单实现"""
        for k,v in man.items():
            print(k,v)

    @classmethod
    def menu(cls):
        print("=" * 50, "\n",
              "1    add a student.\n",
              "2    change student info.\n",
              "3    show all.\n",
              "Q    exit")

    def main(self):
        """程序执行入口"""
        stu = Student()
        sco = GradesBook()
        man = self._student_man
        while True:
            self.menu()
            n_choose = input("please input your choose:")  # type: str
            if n_choose == "1":
                self.add_student(stu,sco)
            elif n_choose == "2":
                self.change_student(stu,sco)
            elif n_choose == "3":
                self.all_student(man)
            elif n_choose == "q" or "Q":
                break
            else:
                self.menu()

if __name__ == '__main__':
    grade = StudentMan()
    grade.main()
