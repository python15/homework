#!/bin/python3.6
import getpass
import sys


administrator = {}
users = {'Tom':['18','13457561423','123456'],
         'Jerry':['20','17641378980','123456'],
         'Elsa':['23','13510498726','123456']}
commands = ['delete','add','update','find','list','exit']
listformat = '%-10s%-10s%-15s%-10s'

#functions
#authentication
def authenticate(loginUser):
    print('input administator\'s password:')
    pwd = input('>>>')
    if pwd == administrator[loginUser]:
        return True
    else:
        return False

def delete(username):
    if not users.get(username):
        print('{} is not in the dict!'.format(username))
    else:
        print('Are you sure to delete the user from the dic? y/n')
        flag = input('>>>')
        if flag == 'y':
            users.pop(username)
            print('delete the user {} from the dict'.format(username))

def update(username, age, tel, pwd):
    if users.get(username):
        tempage = users[username][0]
        temptel = users[username][1]
        temppwd = users[username][2]
        print('Are you sure to update this user\'s information? y/n')
        flag = input('>>>')
        if flag == 'y':
            users[username][0] = age
            users[username][1] = tel
            users[username][2] = pwd
            print('user {} is upgraded!'.format(username))
            if tempage != age:
                print('modify age {} to {}'.format(tempage,age))
            if temptel != tel:
                print('modify tel {} to {}'.format(temptel,tel))
            if temppwd != pwd:
                print('modify password {} to {}'.format(temppwd,pwd))
    else:
        print('user {} is not in the dict! '.format(username))

def add(username, age, tel, pwd):
    if users.get(username):
        print('user {} is in the dict.\n'
              ' if you want to update user information, please input command \'update\''.format(username))
    else:
        print('Are you sure to add the user into dict? y/n')
        flag = input('>>>')
        if flag == 'y':
            users[username] = []
            users[username].append(age)
            users[username].append(tel)
            users[username].append(pwd)
            print('user {} is added!\n'
                  'age: {}\n'
                  'Tel:{}'.format(username,users[username][0],users[username][1]))

def find(username):
    if not users.get(username):
        print('user {} is not in the dict!'.format(username))
    else:
        print('username: {}'.format(username))
        print('age: {}'.format(users[username][0]))
        print('tel: {}'.format((users[username][1])))
        print('pwd: '+'*'*len(users[username][2]))

def list():
    print('1 -- list users according to \'name\'\n'
          '2 -- list users according to \'age\'\n'
          '3 -- list users according to \'tel\'')
    flag = input('>>>')
    print(listformat%('name','age','tel','pwd'))
    if flag != '2' and flag != '3':
        keys = sorted(users.keys())
        for key in keys:
            print(listformat%(key,users[key][0],users[key][1],'*'*len(users[key][2])))
    else:
        if flag == '2':
            keys = sorted(users.items(), key = lambda value:value[1][0],reverse=False)
        elif flag == '3':
            keys = sorted(users.items(), key = lambda obj:obj[1][1], reverse=False)
        for i in range(len(keys)):
            print(listformat%(keys[i][0], keys[i][1][0],keys[i][1][1], '*'*len(keys[i][1][2])))

def exit():
    print('exit this program!')


#create administrator
print('Please create administrator at first!')
admin = input('name of administrator >>>')
adminPwd = input('password >>>')
administrator[admin] = adminPwd
print('create administrator successfully!\n'
      'press any key to login!\n'
      'input "exit" to exit the program!')
excute = input('>>>')
if excute == commands[5]:
    exit()
    sys.exit(0)

#login
while True:
    print('Login:')
    loginUser = input('name >>>')
    loginPwd = input('password >>>')
    if loginUser != admin or loginPwd != adminPwd:
        print('Login Error! User or password is not incorrect!\n'
              'Input "exit" to exit this program. Press any key to try again!')
        login = input('>>>')
        if login == commands[5]: #exit
            exit()
            sys.exit(0)
        else:
            continue
    else:
        break


print('Command:\n'
      'delete -- delete one user\n'
      'add -- add one user\n'
      'update -- update user\'s information\n'
      'find -- print one user\'s information\n'
      'list -- print all the information\n'
      'exit -- exit this program')

while True:
    cmd = input('Input the command >>>')
    if cmd not in commands:
        print('invalid command, try again!')
        continue
    #delete
    if cmd == commands[0]:
        print('input user name:')
        username = input('>>>')
        delete(username)
        continue

    #add or update
    if cmd == commands[1] or cmd == commands[2]:
        print('input user information:')
        username = input('user name: ').strip()
        age = input('user age: ')
        age = age.strip().lstrip('0')
        tel = input('user Tel: ')
        pwd = input('user password: ')
        if int(age) < 1 or int(age) > 120:
            print('age is invalid!')
            continue

        print(username,age,tel,pwd)
        if not authenticate(admin):
            print('Password Error!')
            continue
        if cmd == commands[1]: #add
            add(username,age,tel,pwd)
        else: #update
            update(username,age,tel,pwd)
        continue

    #find
    if cmd == commands[3]:
        print('which user you want to find? input user name:')
        username = input('>>>')
        find(username)
        continue

    #list
    if cmd == commands[4]:
        list()
        continue

    #exit
    if cmd == commands[5]:
        exit()
        break

# 不错，可以考虑增加密码错误的验证次数，比如大于三次就强制退出