'''
在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），默认为name排序. 
'''
import getpass
dict={'zhangshan':[29,13838894578,'passwordzs'],'lisi':[28,13838894577,'passwordls'],'wangwu':[27,13838894576,'passwordww'],'maliu':[26,13838894575,'passwordml']}

def logint():
    logintest=input("请输入登录用户名：")
    if logintest in dict:
        mima=input("请输入用户密码：")
        if dict[logintest][2]==mima:
            return 1
        else:
            return 0
def adduser():
    sryhxx=input("请输入用户名:年龄:联系方式:密码")
    yhxx=sryhxx.split(':')
    if yhxx[0] not in dict: 
        dict[yhxx[0]]=yhxx[1:4]
    else:
        print(yhxx[0] + "Already existed")
def deletuser():
    yh=input("输入用户名:")
    if yh in dict:
        dict.pop(yh)
        print('delete sucess')
    else:
        print(str(yh)+" "+ "user name is nozai")
def updateuser():
    nr=input("请输入用户名:年龄:联系方式:密码")
    updateinfo=nr.split(':')
    if updateinfo[0] in dict:
        dict[updateinfo[0]]=updateinfo[1:4]
    else:
        print(updateinfo[0]+' '+'is not exit')
def finduser():
    username=input("请输入用户名:")
    userinfo={'name':['age','num','password']}
    if username in dict:
        for k in userinfo:
            shuxing=userinfo[k]
            print(k.ljust(20),shuxing[0].ljust(20),shuxing[1].ljust(20),shuxing[2]) 
        shux=dict[username]
        print(username.ljust(20),str(shux[0]).ljust(20),str(shux[1]).ljust(20),'*'*6)        
    else:
        print(username+'user is not exit')

def listuser():
    userinfo={'name':['age','num','password']}
    px=input('请输入排序关键词,如：name, age:')
    if px=='name' or px=='':
        print('orderbyname')
        for k in userinfo:
            shuxing=userinfo[k]
            print(k.ljust(20),shuxing[0].ljust(20),shuxing[1].ljust(20),shuxing[2])        
        for m in sorted(dict.keys()):
            mshuxing=dict[m]
            print(m.ljust(20),str(mshuxing[0]).ljust(20),str(mshuxing[1]).ljust(20),'*'*6)
    elif px=='age':
        print('orderbyage')
        for k in userinfo:
            shuxing=userinfo[k]
            print(k.ljust(20),shuxing[0].ljust(20),shuxing[1].ljust(20),shuxing[2])       
        for i in sorted(dict.values()):
            #pxkey=list(dict.keys())[list(dict.values()).index(i)]
            pxkey=list (dict.keys()) [list (dict.values()).index (i)]
            mshuxing=dict[pxkey]
            print(pxkey.ljust(20),str(mshuxing[0]).ljust(20),str(mshuxing[1]).ljust(20),'*'*6)
if logint():
    print('Welcome user management system.')
    while True:
        print('Please input operator:\n',
        '1.delete ------delete user\n',
        '2.update ------Update the user\n',
        '3.  find ------Lookup users\n',
        '4.  list ------Print all users\n',
        '5. adduser-----add user\n',    
        '6.  exit ------Exit system'
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
        elif shuruxxinfo=='adduser':
            print('Add users')
            adduser()
        elif shuruxxinfo=='exit':
            print('exit system')
            break
        else:
            print('Invalid value entered. Please check.')
else:
    print('mima error or name error')