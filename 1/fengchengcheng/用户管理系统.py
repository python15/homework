# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengchengcheng
#  commit_day:   2018-08-28


import sys,os

login_info = {"user":"admin","passwd":"123"}
user_info = {"meimei":{"age":18,"tel":18883524069},"lilei":{"age":22,"tel":18776542526}}

def menu():
    print ("1.delete\n2.update\n3.list\n4.menu\n5.find\n6.exit")
    comand = input("give me a num:")
    return comand
    
def delete():
    user = raw_input("plese input which user will be deleted:")
    answer = raw_input("%s record will be remove,y/n?:"%user)
    if answer == "y":
        user_info.pop("%s"%user)
        print user_info
#        menu()
#    else:
#        menu()
def update():
    info = raw_input(" user:age:tel\nplease In accordance with the above format input:").split(":")
    m = info[0]
    try:

        user_info[m]["age"] = int(info[1])
        user_info[m]["tel"] = int(info[2])
        print user_info
    except KeyError,e:
        print ("user <%s> does not exists,return to menu")%e
        menu()
def find():
    username = raw_input("please input your want to find name:")
    for k,v in user_info.items():
        if username == k:
            print ("%s,%s,%s")%(k,v["age"],v["tel"])
#    menu()
def select():
    for k,v in user_info.items():
        print "    name:%s\nage:%s tel:%s"%(k,v["age"],v["tel"])
#    menu()
def login():
    num = 3
    while True:
        
        user = raw_input("input your login-user:")
        passwd = raw_input("input your login-passwd:")
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
            update()
        elif res == 3:
            select()
        elif res == 4:
            continue
        elif res == 5:
            find()
        else:
            sys.exit("good bye,sir")
            
# 这个是python2的代码吧，咱们学的是python3，麻烦用python3改写下
# 你的这个python的python3有点混乱了