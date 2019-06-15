#third homework:翻译阿拉伯数字
num=(input("give me a four-number please:"))
data={"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
lstt=[]#待判断数据
lst=[]#最终真实数据
#将数分成字符写入列表
for i in str(num):
    lstt.append(i)

#首数字为0的情况
while lstt[0]=="0":
    lenth=len(lstt)
    if lenth>1:
        lstt.pop(0)
    else:
        break
    


#最终数据列表形成，开始分析

lst=lstt
lenth=len(lst)

#一位数
if lenth<2:
    print(data[lst[0]]+" "+"元")

#两位数
elif lenth<3:
    if lst[1]=="0":
        print(data[lst[0]]+"十"+" "+"元")
    else:
        print(data[lst[0]]+"十"+data[lst[1]]+" "+"元")

#三位数
elif lenth<4:
    if lst[1]=="0":
        if lst[2]=="0":
            print(data[lst[0]]+"佰"+" "+"元")
        else:
            print(data[lst[0]]+"佰零"+data[lst[2]]+" "+"元")
    elif lst[2]=="0":
        print(data[lst[0]]+"佰"+data[lst[1]]+"十"+" "+"元")
    else:
        print(data[lst[0]]+"佰"+data[lst[1]]+"十"+data[lst[2]]+" "+"元")
#四位数
else:
    if lst[1]=="0":
        if lst[2]=="0":
            if lst[3]=="0":
                print(data[lst[0]]+"仟"+"元")
            else:
                print(data[lst[0]]+"仟零"+data[lst[3]]+"元")
        elif lst[3]=="0":
            print(data[lst[0]]+"仟零"+data[lst[2]]+"十"+" "+"元")
        else:
            print(data[lst[0]]+"仟零"+data[lst[2]]+"十"+data[lst[3]]+" "+"元")
    elif lst[2]=="0":
        if lst[3]=="0":
            print(data[lst[0]]+"仟"+data[lst[1]]+"佰"+" "+"元")
        else:
            print(data[lst[0]]+"仟"+data[lst[1]]+"佰零"+data[lst[3]]+" "+"元")
    else:
        if lst[3]=="0":
            print(data[lst[0]]+"仟"+data[lst[1]]+"佰"+data[lst[2]]+"十"+" "+"元")
        else:
            print(data[lst[0]]+"仟"+data[lst[1]]+"佰"+data[lst[2]]+"十"+data[lst[3]]+" "+"元")


# 我这边看到的是乱码，可以的话 私聊我下
