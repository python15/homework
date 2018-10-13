#!/bin/python

#by caizhijian

'''
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，
单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",
数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
'''


number = {'0':"零",'1':"壹", '2':"贰", '3':"叁", '4':"肆", '5':"伍", '6':"陆", '7':"柒", '8':"捌", '9':"玖"}
unit = ["元","拾", "佰", "仟", "万"]

def conversion(x=1):
    capital = []
    m = 0
    count = 1
    for i in str(x):
        if i=='0' and m == 0:
            capital.append(number[i])
            m = 1
            count += 1
            #continue
        elif i != '0':
            capital.append(number[i])
            if len(str(x)) > count:
                capital.append(unit[len(str(x)) - count])
            m = 0
            count += 1
        else:
            count +=1

    #capital[-1] = unit[0] if capital[-1] == number['0'] else capital.append(unit[0])    #这个三元表达式else时输出值为None

    if capital[-1] == number['0']:
        capital[-1] = unit[0]
    else:
        capital.append(unit[0])

    return capital

x = input('Enter money:')
cc = conversion(x)
print(cc)
print(''.join(cc))

