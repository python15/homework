#auth: mgtv-yys
users = {'Bob':'M','Lily':'F','Lucy':'F'}

def deleteUser():
    dUser=input('输入要删除的用户名:')
    if users.__contains__(dUser):
        users.pop(dUser)
        listUser()
    else:
        print('用户不存在')


def listUser():
    for key in users:
        print('姓名:' + key);
        print('性别:' + users[key]);

def addUser():
    name=input('请输入要添加的用户名字:')
    gender=input('请输入要添加用户的性别（F/M):')
    users.update({name:gender})
    listUser()

def findUser():
    name=input('请输入想查找的用户名:')
    if users.__contains__(name):
        print("查找的用户名：%s" %(name))
        print("查找的用户性别：%s" %(users.get(name)))
    else:
        print('用户不存在')

def updateUser():
    name = input('请输入想更新信息的用户名:')
    if users.__contains__(name):
        name = input('请输入要更新的用户名字:')
        gender = input('请输入要更新用户的性别（F/M):')
        users.update({name: gender})
        listUser()
    else:
        print('用户名不存在，将输入的信息添加到数据')
        name = input('请输入要更新的用户名字:')
        gender = input('请输入要更新用户的性别（F/M):')
        users.update({name: gender})
        listUser()

#主函数
count=1
while True:
    print('\n')
    result = input("请输入指令:")
    if result == 'delete':
        deleteUser()
    elif result == 'find':
        findUser()
    elif result == 'list':
        listUser()
    elif result == 'update':
        updateUser()
    elif result == 'add':
        addUser()
    elif result == 'exit':
        print("退出程序")
        break
    else:
        print("错误指令，不知道你要干嘛，还有 %d 输入机会" %(3-count))
        if count == 3:
            break
        else:
            count+=1

