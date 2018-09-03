def delete(action):
    while True:
        flag=False
        name=str(input('Please enter a name:'))
        
        while True:    
            if name in age:
                age.pop(name)
                phone.pop(name)
                flag = True
                break
            else:
                print("The user does not exist")
                name=str(input('Please enter a name:'))
                continue
        if flag:
            print("%s has been deleted." % (name),end=(""))
            break
            
            
def update(action):
    while True:
        updates=str(input("Please enter username:xx age:xx phone:xxx"))
        strings=updates.split(':')
        falg = False

        if strings[0] in age:
            flag = True
            print("Data update:\t name:%s age:%s phone:%s" % (strings[0],strings[1],strings[2]),end="\n")

        else:
            print("User data does not exist")
            flag = True
            print("Data added:\t name:%s age:%s phone:%s" % (strings[0],strings[1],strings[2]),end="\n")

        if flag:
            x={strings[0]:strings[1]}
            y={strings[0]:strings[2]}
            age.update(x)
            phone.update(y)
            break

            
def find(action):
    
    while True:
        name=str(input("Please enter a user name:"))
        flag=False
        
        if name in age:
            print("name:%s\t\t name:%s\t phone:%s"% (name,age.get(name),phone.get(name)),end="")
            flag=True
        else:
            name=str(input("Please enter a user name:"))
        
        if flag:
            break
            

def list(action):
    while True:
        flag = False
        for name in age:
            print("name:%s\t\t name:%s\t phone:%s"% (name,age.get(name),phone.get(name)),end="\n")
            flag=True
        if flag:
            break

            
##def operation(action):

age={'xm':'10','xw':'10','tom':'20'}
phone={'xm':'123','xw':'421','tom':'135'}

while True:
    action=str(input("Enter:delete,update,find,list,exit>>>"))
    if action == 'delete':
        delete(action)
    elif action == 'update':
        update(action)
    elif action == 'find':
        find(action)
    elif action == 'list':
        list(action)
    elif action == 'exit':
        break


# 代码的逻辑很清晰，大体的功能没有啥问题，加个add的操作，顺便可以考虑下用户信息 持久化存储