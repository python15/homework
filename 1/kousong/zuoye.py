data={'red':["15","111"],'green':["10","222"]}
do= input("what do u do ?")
if do=="delete":
    user=input("user please")
    result=data.pop(user,'no this user')
    if result=='no this user':
        print(result)
    
elif do=="update":
    newdata=input("user:age:tel")
    newuser,newage,newtel=newdata.split(':')
    result=data.get(newuser,'no have this user')
    print(result)
    if result!='no have this user':
        data[newuser]=[newage,newtel]

elif do=="find":
    usr=input("user")
    newdata=data.get(usr,"no")
    print(newdata)
    
elif do=="list":
    print("--user------age---tel--")
    for item in data.items():
        print(item)
        
elif do=="exit":
    print("u will exit")
    exit()