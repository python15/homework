#second week

data={'blu':["10","6126","888"],'red':["15","8301","666"]}
lenth=len(data)
while True:
    do= input("what do u do?:update,change,find,list,delete,exit---:")
    if do=="update":
        try:
            newdata=input("user:age:tel:passwd---:")
        except exception as e:
            print(e)
        newuser,newage,newtel,newpasswd=newdata.split(':')
        result=data.get(newuser,None)
        if result:
            data[newuser]=[newage,newtel,newpasswd]
        else:print('no have this user')

    elif do=="change":
        try:
            usrpass=input("user:oldpasswd:newpasswd?----:")
        except exception as e:
            print(e)
        user,oldpasswd,newpasswd=usrpass.split(':')
        exist = data.get(user,None)
        if exist:
            if oldpasswd==(exist)[2]:
                data[user][2]=newpasswd
                print("{}{}{}{}".format("change passwd",oldpasswd,"to",newpasswd ))
            else:print(passwd is false)
        else:print('no have this user')

    elif do=="find":
        count=0
        usr=input("user---:")
        newdata=data.get(usr,None )
        if newdata:
            a=str(newdata[2])
            for i in a :
                count+=1
            print(newdata[0],newdata[1],"*"*count)
        else:print('no have this user')

    elif do=="list":
        a = True
        what=input("sort for name?age?tel?----:")
        if what=="name":
            data1=sorted(data.items(),key=lambda d:d[0])
        elif what=="age":
            data1=sorted(data.items(),key=lambda d:d[1][0])
        elif what=="tel":
            data1=sorted(data.items(),key=lambda d:d[1][1])
        else:
            try:
                a=False
                raise Exception('no this command')
            except Exception as e:
                print(e)
        if a:
            print("--user---age-----tel----passwd--")
            for i in range(0,lenth):
                strpasswd=str(data1[i][1][2])
                count=0
                for _ in strpasswd:
                    count+=1
                data1[i][1][2]="*"*count
                print(data1[i])
                data1[i][1][2]=strpasswd

    elif do=="delete":
        user=input("user please---:")
        result=data.pop(user,'no have this user')
        if result is not 'no have this user':
            lenth -= 1
        else:print(result)

    elif do=="exit":
        print("exit")
        break

    else:
        print('no have this command')