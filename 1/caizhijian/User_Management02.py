#!/bin/python

#by caizhijian

#default users info

usersinfo = {'zhangsan':['20','13800138001'],'lisi':['21','13800138002'],'wangmazi':['53','13800138003']}
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
        print('Name:{} Age:{} Phone:{}'.format(x, usersinfo[x][0], usersinfo[x][0]))

def list(x=1):
    print('%-10s%-10s%-13s' % ('name', 'age', 'Tel'))
    for user in usersinfo.keys():
        print('%-10s%-10s%-13s' % (user, usersinfo[user][0], usersinfo[user][1]))

def add(x):
    age = input('input age:')
    phone = input('input phone:')
    usersinfo.update({x:[age,phone]})


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