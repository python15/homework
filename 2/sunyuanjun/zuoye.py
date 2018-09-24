# encoding:utf-8
user_info = {
    'zhangsan':{'passwd':'zhangsan','age':20,'tel':88888888,},
    'xiaoming':{'passwd':'xiaoming','age':18,'tel':12345678},
    'xiaoli':{'passwd':'xiaoli','age':25,'tel':85456999},
    'xiaozhang':{'passwd':'xiaozhang','age':65,'tel':955544}
}
count = 0

def sign_in(username,passwd=''):
    if username in user_info.keys():
        passwd = input('unput your password:')
        if passwd == user_info[username]['passwd']:
            return 0
        else:
            return 1
    else:
        return 2

def delete_user(username):
    if username in user_info.keys():
        passwd = input('input the password:')
        if passwd == user_info[username]['passwd']:
            user_info.pop(username)
        else:
            print('password is wrong')
    else:
        print("User {} is nor exist.".format(username))

def update_user(username):
    if username in user_info.keys():
        passwd = input('input the old password:')
        if passwd == user_info[username]['passwd']:
            passwd = input('input the new password')
            age = input('unput age:')
            tel = input('unput the telephone number:')
            user_info[username] = {'passwd':passwd,'age':age,'tel':tel}
        else:
            print('Password is wrong.')
    else:
        print("User {} is not exist.".format(username))

def find_user(username):
    if username in user_info.keys():
        print(username)
        for k,v in user_info[username].items():
            if k == 'passwd':
                print(k,'*'*len(v),sep=' ',end=' ')
            else:
                print(k,v,sep=' ',end=' ')
        print()
    else:
        print("User {} is not exist.".format(username))

def list_user():
    print('you can list info by username,age or tel')
    names = []
    passes = []
    ages = []
    tels = []
    for k in user_info.keys():
        names.append(k)
        passes.append(user_info[k]['passwd'])
        ages.append(user_info[k]['age'])
        tels.append(user_info[k]['tel'])
    role = input('role of the sorted[default username]:')

    if role == 'age':
        print(ages)
        for age in sorted(ages):
           print(names[ages.index(age)])
           print('passwd','*'*len(passes[ages.index(age)]),'age',age,'tel',tels[ages.index(age)])
    if role == 'tel':
        for tel in sorted(tels):
            print(names[tels.index(tel)])
            print('passwd','*'*len(passes[tels.index(tel)]),'age',ages[tels.index(tel)],'tel',tel)
    else:
        for name in sorted(names):
            print(name)
            print('passwd','*'*len(passes[names.index(name)]),'age',ages[names.index(name)],'tel',tels[names.index(name)])



def add_user(username,passwd,age,tel):
    if username in user_info.keys():
        print(f"User {username} is exist.")
    else:
        user_info[username] = {'passwd':passwd,'age':age,'tel':tel}



while True:
    username = input('Input username:')
    state_id = sign_in(username)
    if state_id == 1:
        print('password is wrong.')
        break
    elif state_id == 2:
        print(f'user {username} is not exist.')
        break
    else:
        print('login successful!')
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
                update_user(user)
                continue
            elif action == 'find':
                user = input('input username:')
                find_user(user)
                continue
            elif action == 'list':
                list_user()
                continue
            elif action == 'add':
                info = input('input user,password,age,tel use ":" between info:')
                info_list = info.split(':')
                user,passwd,age,tel = info_list
                add_user(user,passwd,int(age),int(tel))
                continue
            elif action == 'exit':
                print('Quit the program.')
                break
            else:
                print('Please input the right operator.')
                continue

    break

# 代码看着没有什么问题，尝试加个add的操作，允许用户新增用户