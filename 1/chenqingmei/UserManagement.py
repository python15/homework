#!/bin/python3.6
#by chenqingmei

#create the default users dictionary
usersinformation = {'Tom':['18','13354629024'],'Jerry':['22','13590567782'],'Elsa':['21','1774724923']}
commands = ['delete','update','find','list','exit']  #valid commands

print('Command:\n'
      'delete -- delete one existed user\n'
      'update -- update users\' information\n'
      'find -- check user information\n'
      'list -- list information for all the users\n'
      'exit -- exit the program')

while True:
    cmd = input('Input conmmand >>>')
    if cmd not in commands:
        print('invalid command, try again!')
        continue

    #delete
    if cmd == commands[0]:
        print('input user name:')
        username = input('>>>')
        #method1: use for ... in to check whether the input name is in the dictionary
        for keyname in usersinformation.keys():
            if username == keyname: #user is in the dictionary
                usersinformation.pop(username)
                print('delete user {} from the dictionary!'.format(username))
                print(usersinformation)
                break
        else:
            print('user {} is not in the dictionary!'.format(username))
        continue  #delete command finish

    #update
    elif cmd == commands[1]:
        print('inpute user informaion, and use character tp seperate user name, age and Tel:')
        userinformation = input('>>>')
        temp = userinformation.partition(':') #get user name temp[0]
        #method2: use get(key) to check whether the name is in the dictionary
        if usersinformation.get(temp[0]) == None:
            print('user {} is not in the dictionary!'.format(temp[0]))
            continue
        #user is exsited
        data = temp[2].partition(':')
        age = data[0]
        tel = data[2]
        uservalue = []
        uservalue.append(age)
        uservalue.append(tel)
        usersinformation[temp[0]] = uservalue
        print('user dictionary was upgraded!\n'
              'user {} is upgraded'.format(userinformation))
        continue  #update command finish

    #find
    elif cmd == commands[2]:
        print('Which user do you want to find? input the user name:')
        username = input('>>>')
        uservalue = usersinformation.get(username)
        if uservalue == None:
            print('user {} is not in the dictionary!'.format(username))
            continue
        print('name: {}  age: {}  Tel: {}'.format(username, uservalue[0],uservalue[1]))
        continue  #find command finish

    #list
    elif cmd == commands[3]:
        print('%-10s%-10s%-13s' % ('name','age','Tel'))
        for user in usersinformation.keys():
            print('%-10s%-10s%-13s' % (user, usersinformation[user][0],usersinformation[user][1]))
        continue  #list command finish

    #exit
    else:
        print('Exit!')
        break  #exit the program




