# 需求：
'''
第二次作业：
在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），
默认为name排序.
'''

dict_users = {'bhangsan': '59:26787656565:passwd', 'aisi': '78:1287867673:passwd2', 'cangwu': '12:4376020387:passwd3'}


def user_info_format(username, password, age, contracts):
    info = '''
---------用户%s信息------------
用户名称  ：%s
密码      ：%s
年龄      ：%s
联系方式  ：%s
---------end--------------------
''' % (username, username, password.__len__()*'*', age, contracts)
    print(info)


def re_sort(dict_name, n):
    print(dict_name)
    new_list = []
    for key in dict_name:
        value = dict_name[key].split(':')
        new_list.append([key] + value)
    new_list = sorted(new_list, key=lambda t: t[n], reverse=False)
    return new_list


while True:
    input_password = input('请输入你的管理密码(admin)：')
    if input_password != 'admin':
        print('密码输入错误，请重新输入：')
        continue
    operate_type = input('请输入操作类型（delete，upate，find，list，add,exit）:')
    if operate_type not in ['delete', 'update', 'find', 'list', 'add', 'exit']:
        continue
    else:
        if operate_type == 'delete':
            input_username = input('请输入需要删除的用户名：')
            if input_username in dict_users:
                del dict_users[input_username]
                print('已成功删除用户:', input_username)
            else:
                print('不存在用户：', input_username)
            continue
        elif operate_type == 'update':
            while True:
                input_str = input('请输入“用户名:年龄:联系方式：密码”：')
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
        elif operate_type == 'find':
            while True:
                input_username = input('请输入需要查找的用户名：')
                if input_username in dict_users:
                    user_info = dict_users[input_username].split(':')
                    user_info_format(input_username, user_info[2], user_info[0], user_info[1])
                    break
                else:
                    oprate_choice = input('不存在用户' + input_username + '是否重新输入Y/N:')
                    if oprate_choice in ['Y', 'y']:
                        continue
                    else:
                        print('返回操作列表>>>>>')
                        break
        elif operate_type == 'list':
            count = 0
            while 1:
                choice_of_sort = input('请输入排序方式：name/age/tel.默认按照用户名name顺序显示：')
                if choice_of_sort in ['', 'name']:
                    pass
                elif choice_of_sort == 'age':
                    count = 1
                elif choice_of_sort == 'tel':
                    count = 2
                else:
                    print('输入参数有误，请重新输入>>>>')
                    continue
                break
            user_info = re_sort(dict_users, 1)
            print(user_info)


            for i in user_info:
                j = []
                for k in i:
                    j.append(k)
                username = j[0]
                age = j[1]
                contracts = j[2]
                password = j[3]
                user_info_format(username, password, age, contracts)
                j.clear()
        elif operate_type == 'add':
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