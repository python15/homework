print("欢迎来到用户管理系统")
print("="*50)
users_info = []
while 1:
    key = input("请输入您要选择的功能")
    if key == 'delete':
        find_name = input("请输入用户名：")
        for i in users_info:
            if i['name'] == find_name:
                users_info.remove(i)
                print("删除用户数据成功")
                break
        else:
            print("用户数据不存在")
    elif key == 'update':
        name = input("请输入用户名：")
        age = input("请输入年龄：")
        tel = input("请输入联系方式")
        if len(users_info) == 0:
            new_info = {}
            new_info['name'] = name
            new_info['age'] = age
            new_info['tel'] = tel
            users_info.append(new_info)
        else:
            for i in users_info:
                if i['name'] == name:
                    i['name'] = name
                    i['age'] = age
                    i['tel'] = tel
                else:
                    new_info = {}
                    new_info['name'] = name
                    new_info['age'] = age
                    new_info['tel'] = tel
                    users_info.append(new_info)
    elif key == 'find':
        find_name = input("请输入用户名：")
        for i in users_info:
            if i['name'] == find_name:
                for key, value in i.items():
                    print(key, value)
                break
        else:
            print("用户不存在")
    elif key == 'list':
        print("name\tage\ttel")
        for i in users_info:
            for value in i.values():
                print(value,end="\t")
            print()
    elif key == 'exit':
        break
    else:
        print("输入错误，请重新输入")




# 最好有个初始化的用户信息好点，顺便考虑增加个add的操作，还有增删改查可以写成独立的函数




