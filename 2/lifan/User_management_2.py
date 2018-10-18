#!/usr/bin/env python
import random

def generation(digital):
    return ''.join([str(random.choice(list(range(1, digital + 1)))) for _ in range(10)])

userInfo = {
    "d1": {"age": 18, "mobile": generation(9), 'passwd': '2525118'},
    "b2": {"age": 33, "mobile": generation(9), 'passwd': '2525128'},
    "a3": {"age": 27, "mobile": generation(9), 'passwd': '2525138'}
}

print("Welcome to use the user management system.")
while True:
    userAction = input(
        "Please enter delete | update | find | list | add for user management or Enter exit exit program: ").strip()

    if userAction == 'list':
        sortAction = input("Please enter age | mobile sort and default name sort:  ").strip()
        if sortAction == 'age':
            sortName = sorted(userInfo, key=lambda value: userInfo[value]['age'], reverse=False)
        elif sortAction == 'mobile':
            sortName = sorted(userInfo, key=lambda value: userInfo[value]['mobile'], reverse=False)
        else:
            sortName = sorted(userInfo, key=lambda value: value, reverse=False)

        [print("username:{}\nage:{}\nmobile:{}\npasswd:{}\n".format(i, userInfo[i]['age'], userInfo[i]['mobile'],
                                                                    len(str(userInfo[i]['passwd'])) * '*')) for i in
         sortName]

    elif userAction == 'find':
        userName = input("Please enter a user name: ").strip()
        if userInfo.get(userName):
            [print("username:{}\nage:{}\nmobile:{}\npasswd:{}\n".format(i, userInfo[i]['age'], userInfo[i]['mobile'],
                                                                        len(str(userInfo[i]['passwd'])) * '*')) for i in
             userInfo if i == userName]
        else:
            print("The user could not be found.")

    elif userAction == 'update':
        userName = input("Please enter the user to modify: ").strip()
        if userInfo.get(userName):
            userPwd = input("Please enter the user password: ").strip()
            if userPwd == userInfo[userName]['passwd']:
                userUpdate = input("Please input 'age:mobile:passwd' information format to modify: ").split(":")
                userInfo[userName]['age'], userInfo[userName]['mobile'], userInfo[userName]['passwd'] = int(
                    userUpdate[0]), int(userUpdate[1]), userUpdate[2]
                print("{}的密码修改为{}！".format(userName, userUpdate[2]))
            else:
                print("Input password error")
        else:
            print("The user could not be found.")

    elif userAction == 'add':
        userAdd = input("Please input 'name:age:mobile:passwd' information format to add: ").strip().split(":")
        if not userInfo.get(userAdd[0]):
            userInfo[userAdd[0]] = {'age': int(userAdd[1]), 'mobile': int(userAdd[2]), 'passwd': userAdd[3]}
        else:
            print('User already exists. ')

    elif userAction == 'delete':
        userName = input("Please enter a user name: ").strip()
        if userInfo.get(userName):
            del userInfo[userName]
        else:
            print("The user could not be found.")

    elif userAction == 'exit':
        print('bye~~')
        break

# 看着没有什么问题，少个认证，再加个持久化存储下试试