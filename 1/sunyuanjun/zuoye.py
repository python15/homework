# encoding:utf-8
user_info = {
    'zhangsan':{'age':20,'phone_no':88888888,},
    'xiaoming':{'age':18,'phone_no':12345678},
    'xiaoli':{'age':25,'phone_no':85456999},
    'xiaozhang':{'age':65,'phone_no':955544}
}

def delete_user(username):
    if username in user_info.keys():
        user_info.pop(username)
    else:
        print("User {} is nor exist.".format(username))

def update_user(username,age,phone_no):
    if username in user_info.keys():
        user_info[username] = {'age':age,'phone_no':phone_no}
    else:
        print("User {} is not exist.".format(username))

def find_user(username):
    if username in user_info.keys():
        print(username,user_info.get(username),sep='\n')
    else:
        print("User {} is not exist.".format(username))

def list_user():
    for k,v in user_info.items():
        print(k,v,sep='\n')

def add_user(username,age,phone_no):
    if username in user_info.keys():
        print(f"User {username} is exist.")
    else:
        user_info[username] = {'age':age,'phone_no':phone_no}


while True:
    action = input('''Input "delete" to delete user
    Input "update" to update user
    Input "find" to select user info
    Input "list" to show all users
    Input "exit" to quit the program
    Input "add" to add user
    Please input the operator:''')
    if action == 'delete':
        user = input('input username:')
        delete_user(user)
        continue
    elif action == 'update':
        user = input('input username:')
        age = int(input('input age:'))
        phone_no = int(input('input phone number:'))
        update_user(user,age,phone_no)
        continue
    elif action == 'find':
        user = input('input username:')
        find_user(user)
        continue
    elif action == 'list':
        list_user()
        continue
    elif action == 'add':
        user = input('input username:')
        age = int(input('input age:'))
        phone_no = int(input('input phone number:'))
        add_user(user,age,phone_no)
        continue
    elif action == 'exit':
        print('Quit the program.')
        break
    else:
        print('Please input the right operator.')
        continue


# 代码看着没有什么问题，尝试加个add的操作，允许用户新增用户