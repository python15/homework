'''
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万".
'''
num_dir={"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
unit={"0":"元","1":"拾","2":"佰","3":"仟","4":"万"}
def inputshuzi():
    while True:
        num=''
        num=input("请输入数字：").lstrip('0')
        if num.isdigit():
            if len(num) <= 5:
                szlist=list(str(num))
                count=0
                libiao=[]
                for i in reversed(szlist):
                    a=num_dir[i] + unit[str(count)]
                    libiao.append(a)
                    count+=1
                    #count=str(count)
                libiao.reverse()
                print(libiao)
                print(''.join(libiao))
                break
            else:
                print("input need less 6 digits")
        else:
            print("please input digit")
inputshuzi()

# 用1001 这个数字测试你的代码，看看会有什么问题



将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万".
'''
num_dir={"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
unit={"0":"元","1":"拾","2":"佰","3":"仟","4":"万"}
def inputshuzi():
    while True:
        num=''
        num=input("请输入数字：").lstrip('0')
        if num.isdigit():
            if len(num) <= 5:
                szlist=list(str(num))
                count=0
                paic=0
                libiao=[]
                fxl=list(reversed(szlist))
                for i in fxl:
                    if i == "0":
                        a="零"
                    else:
                        a=num_dir[i] + unit[str(count)]
                        #count+=1   
                        #continue
                    #a=num_dir[i] + unit[str(count)]
                    libiao.append(a)
                    count+=1
                    #count=str(count)
                libiao.reverse()
                libiao2=list(set(libiao))
                libiao2.sort(key=libiao.index)
                print(libiao2)
                print(''.join(libiao2))
                break
            else:
                print("input need less 6 digits")
        else:
            print("please input digit")
inputshuzi()
