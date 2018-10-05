#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
# Author: gs
# Date: 20180919
# UpdateDate: 20181005

"""
#第三周作业（9.17-9.23）：时间过得好快有木有，大家继续坚持哦 加油加油！
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
"""

def NumberMatch(digit, length):
	chinese = [] 
	output = ''
	flag = 0
	for i in range(length):
		chinese.append(number[int(digit[i])])
	for j in range(len(chinese)):	
		if (chinese[j] != '零'):
			output += chinese[j] + unit[len(chinese)-j-1]
		elif ((chinese[j] == '零') & (output[-1] == '零')) | (j==(len(chinese))-1): 
			output += ''
		else:
			output += '零'

	if (output[-1] == '零'):
		output = output[:-1]+ unit[0] + '整'
	elif (output[-1] == '元'):
		output += '整'
	else:
		output += '元整'

	print (output)

if __name__=='__main__':
	number = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
	unit = ["元", "拾", "佰", "仟", "万"]

	try:
		res = input("Please input a number less than five numbers:")
		if res.startswith('0'):
			print ("Number starts with 0, error. ")
		else:
			if isinstance(int(res), (int)) & (int(res) <= 99999):
				NumberMatch(res, len(res))
			else:
				print ("type error or number is too big, retry")
	except ValueError:
		print ("except: input error, retry")

