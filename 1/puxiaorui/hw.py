#!/usr/bin/env python
# *- coding: utf-8 - *
#

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
d1 = {'abc': {'age':12,'tel':'123456-123'}, 'bcd':{'age':11,'tel':'123-12345'}}

while True:
    lst = ['delete', 'update','find','list', 'add', 'exit', (None,),None]
    s = input('{} >>> '.format(lst[:-2]))
    
    if s not in lst[:-2]:
        print('input error')
        
    if s == 'delete':
        s1 = input('input a username >>> ').strip().lower()
        d1.pop(s1,'no user {} '.format(s1))
    elif s == 'update':
        s2 = input('input format: user:age:tel >>> ').strip().lower()
        user,age,tel = s2.split(':')
        if d1.get(user):
            d1.update({user: {'age': age, 'tel': tel}})
        else:
            print('no user {} '.format(user))
    elif s == 'find':
        s3 = input('input a username >>> ').strip().lower()
        print(d1.get(s3,'no user {} '.format(s1)))
    elif s == 'list':
        print(d1)
    elif s == 'add':
        s2 = input('input format: user:age:tel >>> ').strip().lower()
        user,age,tel = s2.split(':')
        if d1.get(user):
            print('user {} exist!'.format(user))
        else:
            d1.update({user: {'age': age, 'tel': tel}})
    elif s == 'exit':
        break
