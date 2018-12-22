'''
week02
在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），默认为name排序.

dict2=sorted(dict1.items)
from collections import OrderedDict

week01
#User Manager
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

D=dict(name="Bob",age=33)
D[eggs]
D['food']['ham']
'eggs' in D     #成员测试
D.keys()
D.values()
D.items()
D.copy()
D.get(key,default)
D1.update(D2)   #字典合并
D1.pop(key)     #删除元素
len(D1)         #
D1(key)=xx      #修改值
del D(key)      #删除条目
list(D(keys))   #字典视图
for k in d:
    print(k)    #key遍历

for k in d:
    print(d[k]) #value遍历

from collections it OrderempordDict
od=OrderDict()
for key in keys:
    od[key]=d[key]
print(od)
print(od.keys())
'''
from collections import OrderedDict

"""定义一种数据类型user_info"""

user_info={
    "root":{"age":"19", "address":"beijing","password":"123456"},
    "admin":{"age":"30", "address":"shangghai","password":"123456"},
    "administrator":{"age":"90", "address":"nanjing","password":"123456"},
    "sys":{"age":"40", "address":"wuhan","password":"123456"}
}

def welcome():
    print("*"*40)
    print("\n",
          "add       #add a new user\n",
          "delete    #delete a exsit user\n",
          "update    #Update a user's info\n",
          "find      #find a user is't exsit\n",
          "list      #list all user\n",
          "exit      #exit program\n",
          "\n"
    )
    print("*"*40)


def login():
    n = 3
    r = 0
    while n != 0:
        login_name = input("Please input login name:>>>").strip()
        if login_name in user_info.keys():
            login_pwd = input("Please input password:>>>").strip()
            user=user_info.get(login_name)
            pwd=user.get("password")
            if login_pwd == pwd:
                print("welcome")
                work()
                break
            else:
                print("Passord is wrong")
                r += 1
                n -= 1
                print("rest {} times".format(3 - r))
        else:
            print("Username is wrong")
            n -= 1
            r += 1
            print("rest {} times".format(3 - r))

def add(name,age,address,password):
    if name in user_info.keys():
        print("The name are exsit,Please input another name\n")
    else:
        user_info[name]={"age":age,"address":address,"password":password}

def delete(name):
    """check the name exist or not"""
    if name in user_info.keys():
        del user_info[name]
        print("User {} is deleted".format(name))
    else:
        print("The name is not exist\n")

def update(name,age,address,password):
    if name in user_info.keys():
        user_info[name]={"age":age,"address":address,"password":password}
    else:
        print("This username is not find\n")

def find(name):
    if name in user_info.keys():
        value=user_info.get(name)
        age=value.get("age")
        address=value.get("address")
        password=value.get("password")

        print("{} age is {} and address is {},password is {}".format(name,age,address,"*"*len(password)))
    else:
        print("The name is not found\n")

def list_user():
    choice=input("Ordered by which ? Please choice:>>> name | age | address\nDefault order by 'Name'\n>>> ")
    if choice == "name":
        print("name:          age:  address:      password:")
        od=OrderedDict()
        keys=sorted(list(user_info.keys()))
        for key in keys:
            od[key]=user_info[key]

        for k in od.keys():
            value=od.get(k)
            age=value.get("age")
            address=value.get("address")
            password=value.get("password")
            print("{:<15}{:<6}{:<14}{:<8}".format(k,age,address,"*"*len(password)))
    elif choice == "age":
        user_sorted = sorted(user_info, key=lambda value: user_info[value]["age"], reverse=False)
        print(user_sorted)
    elif choice == "address":
        user_sorted=sorted(user_info,key=lambda value:user_info[value]["address"],reverse=False)
        print(user_sorted)
    else:
        print("name:          age:  address:      password:")
        od=OrderedDict()
        keys=sorted(list(user_info.keys()))
        for key in keys:
            od[key]=user_info[key]

        for k in od.keys():
            value=od.get(k)
            age=value.get("age")
            address=value.get("address")
            password=value.get("password")
            print("{:<15}{:<6}{:<14}{:<8}".format(k,age,address,"*"*len(password)))

#    print("{:<15}{:<6}{:<14}{:<8}".format(i,user_sorted[i]["age"], user_sorted[i]["address"], "*" * len(user_sorted[i]["password"])) for i in user_sorted)

def work():
    while True:
        choice = input("\nPlease choice \nadd | delete | update | find | list | exit  :\n>>>")
        if choice =="add":
            name = input("name:>>>")
            age = input("age:>>>").strip()
            address = input("address:>>>")
            password = input("password:>>>")
            add(name,age,address,password)
            continue
        elif choice == "delete":
            name = input("name:>>>")
            delete(name)
            continue
        elif choice == "update":
            name = input("name:>>>")
            age = input("age:>>>")
            address = input("address:>>>")
            password = input("password:>>>")
            update(name,age,address,password)
            continue
        elif choice == "find":
            name = input("name:>>>")
            find(name)
            continue
        elif choice == "list":
            list_user()
            continue
        elif choice == "exit":
            print("bye")
            break


if __name__ == '__main__':
    login()