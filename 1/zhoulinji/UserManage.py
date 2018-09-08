# 需求：
'''
第一次作业：
实现用户管理：
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
dict_users = {'zhangsan':'59:16787656565','lisi':'78:1287867673','wangwu':'12:1376020387'};
user_info_format = '''
---------用户%s信息------------
用户名称  ：%s
年龄      ：%s
联系方式  ：%s
---------end--------------------
'''
#print(user_info_format % (1, 11, 1, 1))
while True:
    oprate_type = input('请输入操作类型（delete，upate，find，list，add,exit）:')
    if oprate_type not in ['delete', 'update', 'find', 'list', 'add', 'exit']:
        continue
    else:
        if oprate_type == 'delete':
            input_username = input('请输入需要删除的用户名：')
            if input_username in dict_users:
                del dict_users[input_username]
                print('已成功删除用户:', input_username)
            else:
                print('不存在用户：', input_username)
            break
        elif oprate_type == 'update':
            while True:
                input_str = input('请输入“用户名:年龄:联系方式”：')
                input_username = input_str.split(':', 1)
                if input_username[0] in dict_users:
                    dict_users[input_username[0]] = input_username[1]
                    print('更新用户信息成功！')
                    break
                else:
                    oprate_choice = input('不存在用户'+input_username[0]+'是否重新输入用户信息:[Y/N]')
                    if oprate_choice in ['Y', 'y']:
                        continue
                    else:
                        print('返回操作列表>>>>>')
                        break
        elif oprate_type == 'find':
            while True:
                input_username = input('请输入需要查找的用户名：')
                if input_username in dict_users:
                    user_info = dict_users[input_username].split(':')
                    print(user_info_format % (input_username, input_username, user_info[0], user_info[1]))
                    break
                else:
                    oprate_choice = input('不存在用户'+ input_username+ '是否重新输入Y/N:')
                    if oprate_choice in ['Y', 'y']:
                        continue
                    else:
                        print('返回操作列表>>>>>')
                        break
        elif oprate_type == 'list':
            for key in dict_users:
                user_info = dict_users[key].split(':')
                print(user_info_format % (key, key, user_info[0], user_info[1]))
        elif oprate_type == 'add':
            while True:
                input_username = input('请输入需要增加的用户信息（用户名：年龄：联系方式）：')
                if input_username.count(':') != 2:
                    print('输入格式错误：')
                    continue
                else:
                    part_of_userinfo = input_username.split(':', 1)
                    dict_users[part_of_userinfo[0]] = part_of_userinfo[1]
                    print('添加成功！')
                    break
        else:
            print('退出程序')
            break






