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
        return "User {} is nor exist.".format(username)

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


while True:
    action = input('''Input "delete" to delete user
    Input "update" to update user
    Input "find" to select user info
    Input "list" to show all users
    Input "exit" to quit the program
    Please input the operator:''')
    if action == 'delete':
        user = input('请输入用户名:')
        delete_user(user)
        continue
    elif action == 'update':
        user = input('请输入用户名:')
        age = int(input('请输入年龄:'))
        phone_no = int(input('请输入联系电话:'))
        update_user(user,age,phone_no)
        continue
    elif action == 'find':
        user = input('请输入用户名:')
        find_user(user)
        continue
    elif action == 'list':
        list_user()
        continue
    elif action == 'exit':
        print('Quit the program.')
        break
    else:
        print('Please input the right operator.')
        continue