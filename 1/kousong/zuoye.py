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
# 在进入if 之前，最好有个提示，比如提示用户可以做什么，还有你的这个代码是单次运行就结束了，while True 里面有没有办法让用户选择结束呢？