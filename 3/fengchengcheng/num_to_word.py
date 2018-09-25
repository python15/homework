# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengchengcheng
#  commit_day:   2018-09-18
'''
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，
单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元"
数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
'''

import sys,os
import re
num = {"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖","10":"拾","三":"佰","四":"仟","五":"万"}
#for k,v in num.items():
#    print (k,v)
while True:
    money = input("please input your money:")
    if money == 'exit':
        sys.exit("good bye,sir")
    else:
        if not re.findall('[1-9]+',money):
            print ("零元")
        else:
            money = money.lstrip("0")
    
            if len(money) == 1:
                print ("%s元"%num[money])
            if len(money) == 2:
                if re.match('[1-9][0]',money):
                    print ("%s拾元"%num[money[0]])
                else:
                    print ("%s拾%s元"%(num[money[0]],num[money[1]]))
            if len(money) == 3:
                if re.match('[1-9][1-9][0]',money):
                    print ("%s佰%s拾元"%(num[money[0]],num[money[1]]))
                elif re.match('[1-9][0][1-9]',money):
                    print ("%s佰零%s元"%(num[money[0]],num[money[2]]))
                elif re.match('[1-9][0]+',money):
                    print ("%s佰元"%num[money[0]])
                else:
                    print ("%s佰%s拾%s元"%(num[money[0]],num[money[1]],num[money[2]]))
            if len(money) == 4:
                if re.match('[1-9][1-9][1-9][0]',money):
                    print ("%s仟%s佰%s拾元"%(num[money[0]],num[money[1]],num[money[2]]))
                elif re.match('[1-9][1-9][0][1-9]',money):
                    print ("%s仟%s佰零%s元"%(num[money[0]],num[money[1]],num[money[3]]))
                elif re.match('[1-9][0][1-9][1-9]',money):
                    print ("%s仟零%s拾%s元"%(num[money[0]],num[money[2]],num[money[3]]))
                elif re.match('[1-9][1-9][0][0]',money):
                    print ("%s仟%s佰元"%(num[money[0]],num[money[1]]))
                elif re.match('[1-9][0][0][1-9]',money):
                    print ("%s仟零%s元"%(num[money[0]],num[money[3]]))
                elif re.match('[1-9][0][1-9][0]',money):
                    print ("%s仟零%s拾元"%(num[money[0]],num[money[2]]))
                else:
                    print ("%s仟元"%(num[money[0]]))

# 功能上没有什么问题，不过print是个函数，中间没有空格，优化下：考虑下写成函数。