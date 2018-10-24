# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengchengcheng
#  commit_day:   2018-10-24
'''
第六周作业：作业继续啊小伙伴们（10.22-10.28）
知识要求：至少需要学到30章的内容
编写一个学生管理系统类—Gradebook:
要求能动态的添加学生-name 和学生成绩grades(一个学生可以有个多科的科目成绩)，并
且根据学生名字能算出学生的平均成绩：
提示：可以预先初始化一个字典，用实例字典存储相应的信息
'''

import sys,os
import getpass

login_info = {"user":"admin","passwd":"123"}
stu_info = {"meimei":{"语文":77,"数学":77,"英语":77},"lilei":{"语文":88,"数学":76,"英语":90},"xiaoming":{"语文":99,"数学":75,"英语":80}}

class GradeBook:    
    def menu(self):
        print("1.delete\n2.update\n3.list\n4.menu\n5.find\n6.avr\n7.exit")
        comand = input("你的选项是:")
        return int(comand)
            
    def delete(self):
        user = str(input("请选择要删除的学生姓名:"))
        answer = str(input("%s 的信息将要被删除,是/否?:"%user))
        if answer == "是":
            stu_info.pop("%s"%user)
    
    def avr(self):
        user = str(input("计算哪位同学的平均成绩:"))
        total_grade = stu_info[user]["语文"]+stu_info[user]["英语"]+stu_info[user]["数学"]
        print("%s 的语文数学英语三科平均成绩为:%d"%(user,total_grade/3))
    
    def update(self):
        
        info = input(" 姓名:语文:数学:英语\n请按照如上格式添加学生信息:").split(":")
        
        m = info[0]
        try:
            stu_info[m]["语文"] = int(info[1])
            stu_info[m]["数学"] = int(info[2])
            stu_info[m]["英语"] = int(info[3])
            print("%s 已修改"%info[0])
        
        except Exception as e:
            stu_info.update(m={"语文":int(info[1]),"数学":int(info[2]),"英语":int(info[3])})
            print("学生 <%s> 信息已添加"%e)
    
    def find(self):
        username = str(input("请输入要查询的学生姓名:"))
        if (username in stu_info.keys()):
    
                print("姓名:%s, 语文:%d, 数学:%d 英语:%s"%(username,stu_info[username]["语文"],stu_info[username]["数学"],stu_info[username]["英语"]))
        else:
            print("%s 学生姓名不正确"%username)
    
    def select(self):
        
        vote = str(input("按照指定科目成绩排序,默认按照姓名:"))
        user_tmp = {}
        if vote == "数学":
            for k in stu_info:
                user_tmp[k] = stu_info[k]["数学"]
            for k1 in sorted(user_tmp.items(),key = lambda x:x[1],reverse = True):
                    for k2 in stu_info:
                        if k1[0] == k2:
                            print("姓名:%s  语文:%d  数学:%d  英语:%s"%(k2,stu_info[k2]["语文"],stu_info[k2]["数学"],stu_info[k2]["英语"]))
        elif vote == "英语":
            for k in stu_info:
                user_tmp[k] = stu_info[k]["英语"]
            for k1 in sorted(user_tmp.items(),key = lambda x:x[1],reverse = True):
                for k2 in stu_info:
                    if k1[0] == k2:
                        print("姓名:%s  语文:%d  数学:%d  英语:%s"%(k2,stu_info[k2]["语文"],stu_info[k2]["数学"],stu_info[k2]["英语"]))
        elif vote == "语文":
            for k in stu_info:
                user_tmp[k] = stu_info[k]["语文"]
            for k1 in sorted(user_tmp.items(),key = lambda x:x[1],reverse = True):
                for k2 in stu_info:
                    if k1[0] == k2:
                        print("姓名:%s  语文:%d  数学:%d  英语:%s"%(k2,stu_info[k2]["语文"],stu_info[k2]["数学"],stu_info[k2]["英语"]))
        else:
            for k1 in sorted(stu_info.items(),key = lambda x:x[0],reverse = True):
                for k in stu_info:
                    if k1[0] == k:
                        print("姓名:%s  语文:%d  数学:%d  英语:%s"%(k,stu_info[k]["语文"],stu_info[k]["数学"],stu_info[k]["英语"]))
    #    menu()
    def login(self):
        num = 3
        while True:
            
            user = str(input("请输入登录用户:"))
            passwd = getpass.getpass("请输入密码:")
            if user == login_info['user'] and passwd == login_info['passwd']:
                print("----登录成功，欢迎进入学生成绩管理系统------")
                break
            else:
                print("密码错误,还有 %d 机会")%num
                if num < 1:
                   sys.exit("登录超过三次,请联系管理员" )
                num = num - 1
                continue
        
if __name__ == '__main__':
    gb = GradeBook()
    gb.login()
    while True:
        print("--------返回首页----------------")
        res = gb.menu()
        if res == 1:
            gb.delete()
        elif res == 2:
            gb.login()
            gb.update()
        elif res == 3:
            gb.select()
        elif res == 4:
            continue
        elif res == 5:
            gb.find()
        elif res == 6:
            gb.avr()
        else:
            sys.exit("再见！！！")
