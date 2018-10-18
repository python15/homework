#!/usr/bin/env python

print("Welcome to use the user management system.")
userInfo = {
    "z1": {"age": 18, "mobile": 112123118},
    "l2": {"age": 28, "mobile": 122123128},
    "w3": {"age": 38, "mobile": 132123138}
}

while True:
    userAction = input(
        "Please enter delete | update | find | list | add for user management or Enter exit exit program: ").strip()

    if userAction == 'list':
        [print("username:{}\nage:{:<4}mobile:{}\n".format(i, userInfo[i]['age'], userInfo[i]['mobile'])) for i in
         userInfo]

    elif userAction == 'find':
        userName = input("Please enter a user name: ").strip()
        if userInfo.get(userName):
            [print("username:{}\nage:{:<4}mobile:{}\n".format(i, userInfo[i]['age'], userInfo[i]['mobile'])) for i in
             userInfo if i == userName]
        else:
            print("The user could not be found.")

    elif userAction == 'update':
        userName = input("Please enter the user to modify: ").strip()
        if userInfo.get(userName):
            userUpdate = input("Please input 'age:mobile' information format to modify: ").split(":")
            userInfo[userName]['age'], userInfo[userName]['mobile'] = userUpdate[0], userUpdate[1]
        else:
            print("The user could not be found.")

    elif userAction == 'add':
        userAdd = input("Please input 'name:age:mobile' information format to add: ").strip().split(":")
        if not userInfo.get(userAdd[0]):
            userInfo[userAdd[0]] = {'age': userAdd[1], 'mobile': userAdd[2]}
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

# 很优雅不错，能否抽成独立的函数