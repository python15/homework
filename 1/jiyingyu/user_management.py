#!/usr/bin/env python3

#用户管理
#如果输入 delete， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据， 若
#存在数据则将该数据移除， 若用户数据不存在， 则提示不存在;
#如果输入 update， 则让用户输入” 用户名:年龄:联系方式” 格式字符串， 并使用:分隔用户
#数据， 根据用户名查找 dcit 中数据， 若存在数据则将改数据更新数据， 若用户数据不存在，
#则提示不存在;
#如果用户输入 find， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据包
#含输入字符串的用户信息， 并打印;
#如果用户输入 list， 则打印所有用户信息;
#打印用户第一个行数据为用户信息描述， 从第二行开始为用户数据;
#如果用户输入 exit， 则打印退出程序， 并退出 ;   

I=input("delete|update|find|list|exit \n")

def memu():
    print("memu")
    exit

def input_delete():
    print("delete")
    exit

def input_update():
    print("update")

def input_find():
    print("find")
    exit

def input_list():
    print("list")
    exit
def input_exit():
    print("exit")
    exit

def main():
    print(memu())
    if I == 'delete':
        input_delete()
        exit
    elif I == 'update':
        input_update()
        exit
    elif I == 'find':
        input_find()
        exit
    elif I == 'list':
        input_list()
    elif I =='exit':
        input_exit()
        exit
    else:
        print("Input is not defined")

main()
