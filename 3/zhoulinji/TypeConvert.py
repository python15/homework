# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 14:02
# @Author  : Yanlin
# @Email   : 952735981@163.com
# @File    : TypeConvert.py
# @Software: PyCharm
import re

# 第三周作业：
# 将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",
# “1001”转化成为"壹仟零壹元",数字的中文对应："零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖",,
#  "拾","佰", "仟", "万"，请试着实验一下  1111 0111  0011 0001  0000  0001 0011 01111  101101

while True:

    input_number = input('请输入需要转换成大写的整数：').strip()
    length = len(input_number)
    if not input_number.isdigit() and input_number != '':
        print('格式错误！注意只能输入数字！请重试>>>>')
        continue
    if length > 10:
        print('只能输入十位以内的整数>>>>')

    ZeroToNine = {'0': "零", '1': "壹", '2': "贰", '3': "叁",'4': "肆", '5': "伍", '6':"陆", '7': "柒", '8':"捌", '9': "玖"}
    unit = {1: "元", 2: "拾", 3: "佰", 4: "仟", 5: "万", 6: "十万", 7: "百万", 8: "千万", 9: "亿", 10: "十亿"}

    if re.findall('^0+$',input_number) :
        print('零元')
        continue


    for i in range(0,length,+1):
        if 5 < length < 9 :
            print(ZeroToNine[input_number[i]] + unit[length].replace('万',''),end='')
        else:
            print(ZeroToNine[input_number[i]] + unit[length], end='')
        length -= 1
    print('\n')
