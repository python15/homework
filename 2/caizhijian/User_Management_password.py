#!/bin/python

#by caizhijian

#default users info


usersinfo = {'zhangsan':['20','13800138001','abc123'],'lisi':['21','13800138002','abc123'],'wangmazi':['53','13800138003','abc123']}
command = ['delete','update','find','list','add','exit','help']

info = '''
     Command:
      delete -- delete one existed user
      update -- update users information
      find -- check user information
      list -- list information for all the users
      add -- user add 
      exit -- exit the program
      help/(ALL) -- print help 
'''

def delete(x):
    for k in usersinfo.keys():
        if x == k:
            usersinfo.pop(x)
            print('Delete user {}'.format(x))
            break

def update(x):
    age = input('input age:')
    phone = input('input phone:')
    if usersinfo.get(x) == None:
        print('No such user {}'.format(x))
    usersinfo[x] = [age, phone]

def find(x):
    if usersinfo.get(x) == None:
        print('No such user {}'.format(x))
    else:
        print('Name:{} Age:{} Phone:{} passwd:{}'.format(x, usersinfo[x][0], usersinfo[x][1],usersinfo[x][2].replace(usersinfo[x][2],'*'*len(usersinfo[x][2]))))

def list(x=1):
    print('%-10s%-10s%-13s%-13s' % ('name', 'age', 'Phone','passwd'))
    for user in usersinfo.keys():
        print('%-10s%-10s%-13s%-13s' % (user, usersinfo[user][0], usersinfo[user][1],usersinfo[user][2].replace(usersinfo[user][2],'*'*len(usersinfo[user][2]))))

def add(x):
    age = input('input age:')
    phone = input('input phone:')
    while True:
        passwd = input('enter you passwd:')
        passwd02 = input('confirm passwd:')
        if passwd != passwd02:
            print('twice enter passw Different!!!')
        elif passwd == passwd02:
            break
    usersinfo.update({x:[age,phone,passwd]})

def logint():
    login_user=input("请输入登录用户名：")
    if login_user in usersinfo:
        mima=input("请输入用户密码：")
        if usersinfo[login_user][2]==mima:
            return 1
        else:
            return 0


if logint():
    print('Welcome user management system.\n',info)

    while True:
        cmd = input('Enter command:')

        if cmd == command[0]:
            username = input('input user name:')
            delete(username)

        elif cmd == command[1]:
            username = input('input user name:')
            update(username)

        elif cmd == command[2]:
            username = input('input user name:')
            find(username)

        elif cmd == command[3]:
            list()

        elif cmd == command[4]:
            username = input('input user name:')
            add(username)

        elif cmd == command[5]:
            break

        else:
            print(info)