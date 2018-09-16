#!/bin/python

#by caizhijian

#default users info

usersinfo = {'zhangsan':['20','13800138001'],'lisi':['21','13800138002'],'wangmazi':['53','13800138003']}
command = ['delete','update','find','list','exit','help']

info = '''
     Command:
      delete -- delete one existed user
      update -- update users information
      find -- check user information
      list -- list information for all the users
      exit -- exit the program
'''

while True:
    cmd = input('Enter command:')

    #delete
    if cmd == command[0]:
        username = input('input user name:')
        for k in usersinfo.keys():
            if username == k:
                usersinfo.pop(username)
                print('Delete user {}'.format(username))
                continue
            else:
                print('No such user {}'.format(username))

    #update
    elif cmd == command[1]:
        username = input('input name:')
        age = input('input age:')
        phone = input('input phone:')
        if usersinfo.get(username) == None:
            print('No such user {}'.format(username))
            continue
        usersinfo[username] = [age,phone]
        continue

    #find
    elif cmd == command[2]:
        username = input('input name:')
        if usersinfo.get(username) == None:
            print('Name:{} Age:{} Phone:{}'.format(username,usersinfo[username][0],usersinfo[username][0]))
            continue
        print('No such user {}'.format(username))
        continue

    #list
    elif cmd == command[3]:
        print('%-10s%-10s%-13s' % ('name','age','Tel'))
        for user in usersinfo.keys():
            print('%-10s%-10s%-13s' % (user, usersinfo[user][0],usersinfo[user][1]))
        continue

    #exit
    elif cmd == command[5]:
        print(info)

    #help
    else:
        print('Exit!')
        break  #exit the program