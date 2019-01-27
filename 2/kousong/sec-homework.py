data={'blu':["10","6126","888"],'red':["15","8301","666"]}
lenth=len(data)
while True:
    do= input("what do u do?:change,delete,update,find,list,exit")
    if do=="delete":
        user=input("user please")
        result=data.pop(user,'no this user')
        if result=='no this user':
            print(result)

    elif do=="update":
        newdata=input("user:age:tel:passwd")
        newuser,newage,newtel,newpasswd=newdata.split(':')
        result=data.get(newuser,'no have this user')
        print(result)
        if result!='no have this user':
            data[newuser]=[newage,newtel,newpasswd]

    elif do=="find":
        count=0
        usr=input("user")
        newdata=data.get(usr,"no")
        a=str(newdata[2])
        for i in a :
            count+=1
        print(newdata[0],newdata[1],"*"*count)

    elif do=="exit":
        print("exit")
        break

    elif do=="change":
        usrpass=input("user:oldpasswd:newpasswd?")
        user,oldpasswd,newpasswd=usrpass.split(':')
        if oldpasswd==(data.get(user,"no"))[2]:
            data[user][2]=newpasswd
            print("{}{}{}{}".format("change passwd",oldpasswd,"to",newpasswd ))

    elif do=="list":
        what=input("sort for name?age?tel?")
        print("--user---age-----tel----passwd--")
        if what=="name":
            data1=sorted(data.items(),key=lambda d:d[0])
        elif what=="age":
            data1=sorted(data.items(),key=lambda d:d[1][0])
        elif what=="tel":
            data1=sorted(data.items(),key=lambda d:d[1][1])

        for i in range(0,lenth):
            strpasswd=str(data1[i][1][2])
            count=0
            for _ in strpasswd:
                count+=1
            data1[i][1][2]="*"*count
            print(data1[i])
# 代码还可以在优化下，等学到后面，记得回头看再来看下这个代码哈
