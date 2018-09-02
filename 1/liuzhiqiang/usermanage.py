usersData = [
    {'username':'tester01', 'age': 27, 'contact': 15200000001},
    {'username':'tester02', 'age': 28, 'contact': 15200000002},
    {'username':'tester03', 'age': 29, 'contact': 15200000003}
    ]
flag = True
while flag:
    print("""
    ===UserManage===
    
    Action:
    
    delete, to delete the specified user;
    update, to update specified user information;
    find, to find the specified user;
    list, to display all users information;
    exit, to exit system
    ================================================
    """)
    
    key  = input("请输入action：")
    if key == 'delete':
        delete_user = input("请输入将要删除的用户名：")
        for i in usersData:    #下文有类似重复代码，后续学了函数考虑优化
            if i['username'] == delete_user:
                usersData.remove(i)
                print("用户已删除！")
                break
        else:
            print("抱歉，用户数据不存在！")
    elif key == 'update':
        update_user = input("请输入'用户名:年龄:联系方式': ")
        update_username = update_user.split(':')
        for i in usersData:
            if i['username'] == update_username[0]:
                i['age'] = int(update_username[1])
                i['contact'] = int(update_username[2])
                print("更新成功！\n更改信息：%s" %i)
                break
        else:
            print("抱歉，用户数据不存在！")
    elif key == 'find':
        find_user = input("请输入查找的用户名：")
        for i in usersData:
            if i['username'] == find_user:
                print(i)
                break
        else:
            print("抱歉，用户数据不存在！")
    elif key == 'list':
        print(usersData)
    elif key == 'exit':
        flag = False
        print("系统已退出！")
    else:
        print("输入有误，请重新输入！")