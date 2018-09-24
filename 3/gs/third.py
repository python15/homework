#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
# Author: gs
# Date: 20180919

"""
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************
*********************** 还没写完，暂时先不看吧。中秋有事儿，回头再写完。 ************************


#第三周作业（9.17-9.23）：时间过得好快有木有，大家继续坚持哦 加油加油！
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
"""

def NumberMatch(num):
	if '0' in str(num):
		if (num.count('0')) == 3:
			print ("%s%s%s%s%s" %(number[int(num)//10000], unit[4], number[0], number[int(num)%10000], unit[0]))
		#elif ((num.count('0')) == 2) & ((num.index('0'), 1)>0):
		print ("HE", num.index('0', 1, 2))
			#print ("two 0")
	else: 
		print ("no 0")

	#if (num//10000 >0):
	#	five = 1
	#	print ("%s万" %(number[num//10000]))
	#	print "five"
	#	output = output + %s + %s %(number[num//10000], unit[4])	
	#	print "second five"
	#	num = num % 10000
	#	NumberMatch(num)
	#elif (num//1000 >0):
	#	four = 1	
	#	#output = output + (("%s万") %(number[num//10000]))
	#	print ("%s仟") %(number[num//1000])
	#	output = output + number[num//1000] + unit[3]	
	#	num = num % 1000
	#	NumberMatch(num)
	#elif (num//100 >0):
	#	three = 1
	#	print ("%s佰") %(number[num//100])
	#	output = output + number[num//100] + unit[2]	
	#	num = num % 100
	#	NumberMatch(num)
	#elif (num//10 >0):
	#	two = 1
	#	print ("%s拾") %(number[num//10])
	#	output = output + number[num//10] + unit[1]	
	#	num = num % 10
	#	NumberMatch(num)
	#else:
	#	print ("%s元") %(number[num])
	#	output = output + number[num//1] + unit[0]	


if __name__=='__main__':
	number = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
	unit = ["元", "拾", "佰", "仟", "万"]
	five=four=three=two=0
	output=''

	try:
		res = input("Please input a number less than five numbers:")
		#print ("1", type(res))
		if res.startswith('0'):
			print ("Number starts with 0, error. ")
			#print ("2", type(res))
		else:
			if isinstance(int(res), (int)) & (int(res) <= 99999):
				print ("res:%s" %(res))
				#print ("3", type(res))
				NumberMatch(res)
			else:
				print ("type error or number is too big, retry")
	except ValueError:
		print ("except: input error, retry")

