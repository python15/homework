'''
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
'''

"""定义一种数据类型user_info"""

user_info={
    "alax":{"age":"19", "address":"beijing"},
    "bob":{"age":"30", "address":"shangghai"}
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

def add(name,age,address):
    if name in user_info.keys():
        print("The name are exsit,Please input another name\n")
    else:
        user_info[name]={"age":age,"address":address}

def delete(name):
    """check the name exist or not"""
    if name in user_info.keys():
        del user_info[name]
    else:
        print("The name is not exist\n")

def update(name,age,address):
    if name in user_info.keys():
        user_info[name]={"age":age,"address":address}
    else:
        print("This username is not find\n")

def find(name):
    if name in user_info.keys():
        value=user_info.get(name)
        age=value.get("age")
        address=value.get("address")

        print("{} age is {} and address is {}".format(name,age,address))
    else:
        print("The name is not found\n")

def list():
    print("name    age   address")
    for k in user_info:
        value=user_info.get(k)
        age=value.get("age")
        address=value.get("address")
        print("{:<8}{:<6}{:<8}".format(k,age,address))

if __name__ == '__main__':
    welcome()
    flag=False
    while not flag:
        choice = input("\nPlease choice \nadd | delete | update | find | list | exit  \n >>>")
        if choice =="add":
            name = input("name:>>>")
            age = input("age:>>>")
            address = input("address:>>>")
            add(name,age,address)
            continue
        elif choice == "delete":
            name = input("name:>>>")
            delete(name)
            continue
        elif choice == "update":
            name = input("name:>>>")
            age = input("age:>>>")
            address = input("address:>>>")
            update(name,age,address)
            continue
        elif choice == "find":
            name = input("name:>>>")
            find(name)
            continue
        elif choice == "list":
            list()
            continue
        elif choice == "exit":
            print("bye")
            break