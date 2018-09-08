#用字典模拟初始数据库
dict1={
    "xiaozhi":{"passwd":123,"count":0},
    "xiaofang":{"passwd":123,"count":0},
    "xiaoming":{"passwd":123,"count":0}
}
#添加用户
def add1(uname,passwd):
    dict1[uname]=passwd

#删除用户，不存在做出提示
def del1(uname):
    print(dict1.pop(uname,"no exist"))

#查询有哪些用户，当然密码不能看
def query1():
    for i in dict1.keys():
        print(i)

#登入模块
def login():
    while 1:
        #输出账号
        uname=input(">>please input your uname:").strip()
        #输出账号不存在
        if uname not in dict1:
            print("uname is not exist")
            continue
        #输出账号存在，且判断是否超过三次，超过三次拒绝访问
        else:
            if dict1[uname]["count"]>2:
                print("you try too many,inject login!!!")
                continue

        passwd=int(input(">>please input your passwd:"))
        if passwd==dict1[uname]["passwd"]:
            print("login succeed")
            break
        else:
            print("用户名或密码错误")
            dict1[uname]["count"] += 1
while 1:
    print(" add\n query\n del\n login\n")
    i=input(">>Enter the action you need:")
    if i=="add":
        uname=input("unmae:")
        passwd=input("passwd:")
        add1(uname,passwd)
    elif i=="query":
        query1()
    elif i=="del":
        uname=input("uname:")
        del1(uname)
    elif i=="login":
        login()

# 增加，删除 查询和登录都做成的独立的模块了，不过还少个修改的函数，考虑增加先