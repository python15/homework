#!/usr/bin/python
# -*- coding:utf-8 -*-


def userFind(user_name):
	for key in userinfo:
		if key == user_name:
			print "User Finded: \nName:%s-%s\n" %(key, userinfo[key])
				
def userUpdate(name, nage, ntel):
	for key in userinfo:
		if key == name:
			print "User: \nName:%s-%s\n" %(key, userinfo[key])
			userinfo[key]="{'age':%d, 'tel':%s}" %(int(nage), ntel)
			print "User Info Update to:\nName:%s-%s\n" %(key, userinfo[key])
			return 1 
	return 0
		
def userDelete(user_name):
	for key in userinfo:
		if key == user_name:
			del userinfo[key]
			return 1
	return 0

def userList():
	id=1
	print "All User Info:\n"
	for key in userinfo:
		print "%d. Name:%s-%s\n" %(id, key, userinfo[key])
		id +=1

if __name__=='__main__':
	userinfo={'gs':{'age':18,'tel':'12345678900'}, 
                  '张三':{'age':27, 'tel':'18017172233'},
		  '小翠':{'age':16, 'tel':'19199223300'},
		  '无名':{'age':70, 'tel':''}
		}


	while True:
		print('**********************************************\n')
		print('\t Welcome to UserManagement System!\t')
		print('\n**********************************************')

		print('Please choose a menu:')

		print('1. userFind; \n2. userUpdate; \n3. userDelete; \n4. userList；\n5. exit')

		selection=raw_input('\nPlease enter your selection:')

		if selection == '1': 
			user_name = raw_input('\nPlease input the username:')
			userFind(user_name)

		elif selection == '2':
			info = raw_input('\nPlease input userinfo, format like "gs:18:18017456823":')
			if ':' in info:
				try:
					name,age,tel=info.split(':')
					res = userUpdate(name, age, tel)
					if res == 0:
						print "No user named %s, please check it.\n" %name
				except ValueError, Argument:
					print "Error: %s\n" %Argument 
			else:
				print "format not right.\n"

		elif selection == '3':
			user_name = raw_input('\nPlease input the username:')
			res = userDelete(user_name)
			if res == 1:
				print "Delete Success, Name: %s" %user_name
			else:
				print "User: %s not exist\n" %user_name

		elif selection == '4':
			userList()

		elif selection == '5':
			print 'exit...'
			exit()
