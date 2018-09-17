# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 14:02
# @Author  : Yanlin
# @Email   : 952735981@163.com
# @File    : TypeConvert.py
# @Software: PyCharm

# 第三周作业：
# 将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",
# “1001”转化成为"壹仟零壹元",数字的中文对应："零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖",,
#  "拾","佰", "仟", "万"，请试着实验一下

while True:
    input_number = input('请输入需要转换成大写的整数：').strip().lstrip('0')
    if not input_number.isdigit():
        print('格式错误！注意只能输入数字！请重试>>>>')
        continue

    dict_of_ZeroToNine = {'0': "零", '1': "壹", '2': "贰", '3': "叁",'4': "肆", '5': "伍", '6':"陆", '7': "柒", '8':"捌", '9': "玖"}
    dict_of_unit = {1: "元", 2: "拾", 3: "佰", 4: "仟", 5: "万"}
    new_list = []
    amount_in_words = ''
    length = len(input_number)

    for i in input_number:
        new_list.append(dict_of_ZeroToNine[i]+dict_of_unit[length])
        length -= 1

    amount_in_words=amount_in_words.join(new_list)
    print(amount_in_words)


