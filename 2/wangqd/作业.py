def add():
    while True:
        user=str(input("Enter the username:"))
        flag = False
        while True:
            flag = True
            if user in userpassword:
                print("Please enter the user already exists and Change this user password\n")
                oldpassword=str(input("Please enter the old password:"))

                if oldpassword==userpassword[user]:
                    print("Password pass.\n")
                    newpassword=str(input("Please enter a new password:"))
                    userpassword[user]=newpassword
                    break

            else:

                print("Please enter a user that does not exist and Create this user")
                newpassword=str(input("Enter new user's password:"))
                userpassword.update({user:newpassword})
                break

        if flag:
            print("Change the password %s to %s" % (userpassword[user],newpassword))
            break

            
def find():

    while True:
        name=str(input("Please enter the username you are looking for:"))
        
        if name in userpassword:
            print("name:%s\tage:%s\ttel:%s\tpassword:%s\t" % (name,age[name],tel[name],len(userpassword[name])*'*'))
        
        else:
            print("The search user does not exist.\n")
        
        return
            
            
            
def list():
    
    while True:
        field=str(input("Enter the fields for sorting:"))
        flag = False
        def insert_sort(age):
            ary=list(age.items())
            for i in range(1,len(ary)):
                if ary[i][1] < ary[i-1][1]:
                    temp=ary[i]
                    while i > 0 and ary[i-1][1] > ary[i][1]:
                        ary[i] =ary[i-1]
                        i-=1
                        ary[i] = temp
            return ary

        if field == 'name':
            print("name:%s\t\t age:%s\t tel:%s\t password:%s"% (name,age[name],tel[name],len(userpassword[name])*'*'),end="\n")
            flag = True
        if field == 'age':
            newage=insert_sort(age)
            newage=dict(newage)
            print("age:%s\tname:%s\ttel:%s\tpassword:%s" % (age[name],name,phone[name],len(userpassword[name]*"*")),end="\n")
            flag = True
        if field =='tel':
            newtel=insert_sort(tel)
            newtel=dict(newtel)
            print("age:%s\tname:%s\ttel:%s\tpassword:%s" % (tel[name],name,age[name],len(userpassword[name]*"*")),end="\n")
            flag = True
        return flag
            


userpassword={'tom':'@123','xw':'123','xm':'33'}

age={'xm':'10','xw':'10','tom':'20'}

tel={'xm':'123','xw':'421','tom':'135'}

while True:
    action = str(input("please enter(add,update,list,find,quit):"))
    if  action == 'update'or action == 'add':
        add()
    if action == 'find':
        find()
    if action == 'list':
        list()
    if action == 'quit':
        break

