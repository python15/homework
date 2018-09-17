#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
# Author: gs
# Date: 20180907

import getpass

def userLogin(user_name, user_pwd):
	if user_name in userinfo:
		if user_pwd == userinfo[user_name]['pwd']:
			return 1
		else:
			return 0

def userFind(user_name):
	if user_name in userinfo:
		print ('UserInfo-- Name: %s Age: %d Phone: %s PWD: ******\n' %(user_name, int(userinfo[user_name]['age']), userinfo[user_name]['tel']))
	else:
		print ('UserInfo Not Exist.\n')
				
def userUpdate(name, nage, ntel):
	for key in userinfo:
		if key == name:
			print ("User: \nName:%s-%s\n" %(key, userinfo[key]))
			userinfo[key]="{'age':%d, 'tel':%s}" %(int(nage), ntel)
			print ("User Info Update to:\nName:%s-%s\n" %(key, userinfo[key]))
			return 1 
	return 0
		
def userDelete(user_name):
	for key in userinfo:
		if key == user_name:
			del userinfo[key]
			return 1
	return 0

def userAdd(nname, nage, ntel):
	userinfo[nname]="{'age':%d, 'tel':%s}" %(int(nage), ntel)
	return 0

def userList():
	id=1
	user_tmp = {} 

	ctype = input("\nPlease Choose Sort Type: 1. Username(Default) 2. Age 3. Phone : ")


	if ctype == '1' or ctype == '':
		print ('Sorted by Username:')
		sort_un = sorted(userinfo.keys())
		for key in sort_un:
			print ("%d. Name: %s Age: %d Phone: %s PWD: ******\n" %(id, key, int(userinfo[key]['age']), userinfo[key]['tel']))
			id +=1

	elif ctype == '2':
		print ('Sorted by Age:\n')
		for key in userinfo:
			user_tmp[key] = userinfo[key]['age']
		for name in sorted(user_tmp.items(), key=lambda x:x[1]):
			for key1 in userinfo:
				if name[0] == key1:
					print ("%d. Name: %s Age: %d Phone: %s PWD: ******\n" %(id, key1, int(userinfo[key1]['age']), userinfo[key1]['tel']))
					id += 1

	elif ctype == '3':
		print ('Sorted by Phone:\n')
		for key in userinfo:
			user_tmp[key] = userinfo[key]['tel']
		for name in sorted(user_tmp.items(), key=lambda x:x[1]):
			for key1 in userinfo:
				if name[0] == key1:
					print ("%d. Name: %s Age: %d Phone: %s PWD: ******\n" %(id, key1, int(userinfo[key1]['age']), userinfo[key1]['tel']))
					id += 1
	
	else:
		print ('\n Type Error.\n')

if __name__=='__main__':
	userinfo={'gs':{'age':18,'tel':'12345678900', 'pwd':'123abc'}, 
                  'zhangsan':{'age':27, 'tel':'18017172233', 'pwd':'123abc'},
		  'xiaocui':{'age':16, 'tel':'19199223300', 'pwd':'123abc'},
		  'wuming':{'age':70, 'tel':'', 'pwd':'123abc'}
		}


	user = input('Please enter login username:')
	pwd = getpass.getpass('password:')
	login = userLogin(user, pwd)

	#login = 1

	if login:
		print ("\n\nLogin as %s .\n\n" %user)

		while True:
			print('**********************************************\n')
			print('\t Welcome to UserManagement System!\t')
			print('\n**********************************************')

			print('Menu:')

			print('1. userFind; \n2. userUpdate; \n3. userDelete; \n4. userList；\n5. userAdd；\n6. exit')

			selection = input('\nPlease enter your selection:')

			if selection == '1': 
				user_name = input('\nPlease input the username:')
				userFind(user_name)

			elif selection == '2':
				info = input('\nPlease input userinfo, format like "gs:18:18017456823":')
				if ':' in info:
					try:
						name,age,tel=info.split(':')
						res = userUpdate(name, age, tel)
						if res == 0:
							print ("No user named %s, please check it.\n" %(name))
					except ValueError:
						print ("Input Error, Please try again")
				else:
					print ("format not right.\n")

			elif selection == '3':
				user_name = input('\nPlease input the username:')
				res = userDelete(user_name)
				if res == 1:
					print ("Delete Success, Name: %s" %user_name)
				else:
					print ("User: %s not exist\n" %user_name)

			elif selection == '4':
				userList()

			elif selection == '5':
				info = input('\nPlease input userinfo, format like "gs:18:18017456823":')
				if ':' in info:
					try:
						name,age,tel=info.split(':')
						res = userAdd(name, age, tel)
						if res == 0:
							print ("User %s Add Success." %(name))
					except ValueError:
						print ("Input Error, Please try again")
				else:
					print ("format not right.\n")

			elif selection == '6':
				print ('exit...')
				exit()

	else:
		print ("Password Error!")

# 写的很好，有登录验证，不过有个小问题，print 是个函数，一般函数是个方法，print() 直接最好不要有括号，新增用户的时候，我出现异常了，麻烦检出下