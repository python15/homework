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
	print ("")
	print ("\nAll User Info:\n")
	for key in userinfo:
		print ("%d. Name: %s 年龄: %d 电话: %s 密码: ******\n" %(id, key, int(userinfo[key]['age']), userinfo[key]['tel']))
		id +=1

if __name__=='__main__':
	userinfo={'gs':{'age':18,'tel':'12345678900', 'pwd':'123abc'}, 
                  '张三':{'age':27, 'tel':'18017172233', 'pwd':'123abc'},
		  '小翠':{'age':16, 'tel':'19199223300', 'pwd':'123abc'},
		  '无名':{'age':70, 'tel':'', 'pwd':'123abc'}
		}


	user = input('Please enter login username:')
	pwd = getpass.getpass('password:')
	login = userLogin(user, pwd)

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
