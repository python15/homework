num_dir={"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
unit=["元","拾","佰","仟","万"]


def get_num():
    while True:
        num=input("请输入数字：").lstrip('0')
        if num.isdigit() and len(num) <= 5:
            return num
            break
        else:
            print("Is the input correct！！！")

def convert_num():
    num=get_num()
    length=len(num)
    count=0
    flag=0
    convert_result=[]
    for i in str(num):
        if i == "0" and flag==0:
            convert_dx=num_dir[i]
            convert_result.append(convert_dx)
            flag=1
            count +=1              
        elif int(i):
            convert_dx=num_dir[i] + unit[length-1-count]
            convert_result.append(convert_dx)
            flag=0
            count +=1
        else:
            count +=1
    if (list(str(num))[length-1])=="0":
        convert_result[len(convert_result)-1]=unit[0]  
    #print(convert_result)    
    print(''.join(convert_result))

if __name__ == '__main__':
    convert_num()

# 写的很好，有个小问题是 return 和break的用法，你可以在思考下