# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengchengcheng
#  commit_day:   2018-09-11
'''
在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），默认为name排序. '''

import sys,os
import getpass

login_info = {"user":"admin","passwd":"123"}
user_info = {"meimei":{"age":18,"tel":18883524069,"passwd":"123"},"lilei":{"age":22,"tel":18776542526,"passwd":"1234"},"abc":{"age":10,"tel":15776542526,"passwd":"12345"}}

    
def menu():
    print ("1.delete\n2.update\n3.list\n4.menu\n5.find\n6.exit")
    comand = input("give me a num:")
    return int(comand)
        
def delete():
    user = str(input("plese input which user will be deleted:"))
    answer = str(input("%s record will be remove,y/n?:"%user))
    if answer == "y":
        user_info.pop("%s"%user)
#        print (user_info)
#        menu()
#    else:
#        menu()
def update():
    
    info = input(" user:age:tel\nplease In accordance with the above format input:").split(":")
    info1 = getpass.getpass("new passwd:")
    
    m = info[0]
    try:
        old_pass = user_info[m]["passwd"]
        user_info[m]["passwd"] = info1
        print ("%s has been changed %s"%(old_pass.__len__()*'*',user_info[m]["passwd"].__len__()*'*'))
        user_info[m]["age"] = int(info[1])
        user_info[m]["tel"] = int(info[2])
        print ("%s has update"%info[0])
    
    except Exception as e:
        print ("user <%s> does not exists "%e)
#        menu()

def find():
    username = str(input("please input your want to find name:"))
    if (username in user_info.keys()):
        for k,v in user_info.items():
            print ("name:%s, age:%d, tel:%d passwd:%s"%(k,v["age"],v["tel"],v["passwd"].__len__()*'*'))
    else:
        print ("%s does not exists"%username)
#    menu()
def select():
    
    vote = str(input("sort by tel/age,default by name:"))
    user_tmp = {}
    if vote == "age":
        for k in user_info:
            user_tmp[k] = user_info[k]["age"]
        for k1 in sorted(user_tmp.items(),key = lambda x:x[1]):
                for k2 in user_info:
                    if k1[0] == k2:
                        print ("name:%s  age:%d  tel:%d  passwd:%s"%(k2,user_info[k2]["age"],user_info[k2]["tel"],user_info[k2]["passwd"].__len__()*'*'))
    elif vote == "tel":
        for k in user_info:
            user_tmp[k] = user_info[k]["tel"]
        for k1 in sorted(user_tmp.items(),key = lambda x:x[1]):
            for k2 in user_info:
                if k1[0] == k2:
                    print ("name:%s  age:%d  tel:%d  passwd:%s"%(k2,user_info[k2]["age"],user_info[k2]["tel"],user_info[k2]["passwd"].__len__()*'*'))
    else:
        for k1 in sorted(user_info.items(),key = lambda x:x[0]):
            for k in user_info:
                if k1[0] == k:
                    print ("name:%s  age:%d  tel:%d  passwd:%s"%(k,user_info[k]["age"],user_info[k]["tel"],user_info[k]["passwd"].__len__()*'*'))
#    menu()
def login():
    num = 3
    while True:
        
        user = str(input("input your login-user:"))
        passwd = getpass.getpass("input your login-passwd:")
        if user == login_info['user'] and passwd == login_info['passwd']:
            print ("----login success,welcome to use the proream------")
            break
        else:
            print ("user or passwd incorrect,just %d chance")%num
            if num < 1:
               sys.exit("login more than three times,pelase contact the administrator" )
            num = num - 1
            continue
    
if __name__ == '__main__':
    login()
    while True:
        print ("--------return to menu----------------")
        res = menu()
        if res == 1:
            delete()
        elif res == 2:
            login()
            update()
        elif res == 3:
            select()
        elif res == 4:
            continue
        elif res == 5:
            find()
        else:
            sys.exit("good bye,sir")



# 不错，增加了密码验证的次数