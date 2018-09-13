'''
用户管理
如果输入 delete， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据， 若
存在数据则将该数据移除， 若用户数据不存在， 则提示不存在;
如果输入 update， 则让用户输入” 用户名:年龄:联系方式” 格式字符串， 并使用:分隔用户
数据， 根据用户名查找 dcit 中数据， 若存在数据则将改数据更新数据， 若用户数据不存在，
则提示不存在;
如果用户输入 find， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据包
含输入字符串的用户信息， 并打印;
如果用户输入 list， 则打印所有用户信息;
打印用户第一个行数据为用户信息描述， 从第二行开始为用户数据;
如果用户输入 exit， 则打印退出程序， 并退出 ;  
'''
#数据初始化
user_dict = {'zhangsan': [26,139000000],'lisi': [30,1392000001]}
#删除用户函数
def delete_user():
    username = ''
    print('Please enter the username:')
    username = input()
    if username in user_dict:
        user_dict.pop(username)
        print('Delete susscced')
    else:
        print('User not exist in dict')
#打印所有用户
def list_user():
    user_title = {'Name': ['Age','Number']}
    for key in user_title:
        temp_list = user_title[key]
        print(key.ljust(20),temp_list[0].ljust(20),temp_list[1])
    for key in user_dict:
        temp_list = user_dict[key]
        print(key.ljust(20),str(temp_list[0]).ljust(20),str(temp_list[1]))

#打印指定用户
def find_user():
    username = ''
    print('Please enter the username:')
    username = input()
    if username in user_dict:    
        user_title = {'Name': ['Age','Number']}
        for key in user_title:
            temp_list = user_title[key]
            print(key.ljust(20),temp_list[0].ljust(20),temp_list[1])
        temp_list = user_dict[username]
        print(username.ljust(20),str(temp_list[0]).ljust(20),str(temp_list[1]))
    else:
        print('User not exist in dict')
#更新指定用户
def update_user():
    print('Please enter update information\(Format is martin:23:1381302323 \)：')
    #lst1 = input().split(':')
    temp_list= input().split(':')
    if temp_list[0] in user_dict:
        user_dict[temp_list[0]] = temp_list[1:3]
        print('Update susscced')
    else:
        print('User not exist in dict')   

#主程序    
print (r'***User Mangement System***')
while True:
    print('Please input keyword for operating:\n',
          '1.delete --- Delete a user from system\n',
          '2.update --- Update user information\n',
          '3.find --- Print the user information which match the username you input\n',
          '4.list --- List all user informations\n',
          '5.exit --- Quit from system')
    choice = input()
    if choice == 'delete':
        print('delete user')
        delete_user()
    elif choice == 'exit':
        print('system exit')
        break
    elif choice == 'list':
        print('list all user information:')
        list_user()
    elif choice == 'find':
        print('Find one user information:')
        find_user()
    elif choice == 'update':
        print('Update a user information:')
        update_user()
    else:
        print('Invalid input,please enter the correct keyword!')


# 逻辑上没有上啥问题，不过既然有序号了，那么再选择功能的时候，是不是可以直接输入序号呢？顺便增加个add的操作哈