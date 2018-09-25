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
dict={'zhangshan':[29,13838894578],'lisi':[28,13838894577],'wangwu':[27,13838894576],'maliu':[26,13838894575]}
def deletuser():
    yh=input("输入用户名:")
    if yh in dict:
        dict.pop(yh)
        print('delete sucess')
    else:
        print(str(yh)+" "+ "user name is nozai")
def updateuser():
    nr=input("请输入用户名:年龄:联系方式")
    updateinfo=nr.split(':')
    if updateinfo[0] in dict:
        dict[updateinfo[0]]=updateinfo[1:3]
    else:
        print(updateinfo[0]+' '+'is not exit')
def finduser():
    username=input("请输入用户名:")
    if username in dict:
        print(dict[username])
    else:
        print(username+'user is not exit')

def listuser():
    userinfo={'name':['age','num']}
    for k in userinfo:
        shuxing=userinfo[k]
        print(k.ljust(20),shuxing[0].ljust(20),shuxing[1])
    for m in dict:
        mshuxing=dict[m]
        print(m.ljust(20),str(mshuxing[0]).ljust(20),mshuxing[1])

print('Welcome user management system.')

while True:
    print('Please input operator:\n',
    '1.delete ------delete user\n',
    '2.update ------Update the user\n',
    '3.  find ------Lookup users\n',
    '4.  list ------Print all users\n',
    '5.  exit ------Exit system'
         )
    shuruxxinfo=input('请输入:')
    if shuruxxinfo=='delete':
        print('delete user')
        deletuser()
    elif shuruxxinfo=='update':
        print('update user')
        updateuser()
    elif shuruxxinfo=='find':
        print('Lookup user')
        finduser()
    elif shuruxxinfo=='list':
        print('Print all users')
        listuser()
    elif shuruxxinfo=='exit':
        print('exit system')
        break
    else:
        print('Invalid value entered. Please check.')


# 写的很不错，字典和列表 是我个人比较推荐的