"""
week03
第三周作业（9.17-9.23）
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",
“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖",
"拾", "佰", "仟", "万"，请试着实验一下。
"""

#Exchage Function
def exchange(n):
    D={0:"零",1:"壹",2:"贰",3:"叁",4:"肆",5:"伍",6:"陆",7:"柒",8:"捌",9:"玖"}
    return D.get(n)

if __name__ == '__main__':
    number = int(input("number:>>>"))
    if number < 10000:
        n1=number//1000
        n2=number//100%10
        n3=number//10%10
        n4=number%10

        if n1 != 0:
            if n2 != 0:
                if n3 != 0:
                    if n4 != 0:
                        print("{}仟{}佰{}拾{}圆整".format(exchange(n1),exchange(n2),exchange(n3),exchange(n4)))
                    else:
                        print("{}仟{}佰{}拾圆整".format(exchange(n1),exchange(n2),exchange(n3)))
                else:
                    if n4 != 0:
                        print("{}仟{}佰{}圆整".format(exchange(n1),exchange(n2),exchange(n4)))
                    else:
                        print("{}仟{}佰圆整".format(exchange(n1),exchange(n2)))
            else:
                if n3 != 0:
                    if n4 != 0:
                        print("{}仟{}拾{}圆整".format(exchange(n1),exchange(n3),exchange(n4)))
                    else:
                        print("{}仟{}拾圆整".format(exchange(n1),exchange(n3)))
                else:
                    if n4 != 0:
                        print("{}仟零{}圆整".format(exchange(n1),exchange(n4)))
                    else:
                        print("{}仟圆整".format(exchange(n1)))
        else:
            print("The number should more than 1000")

    else:
        print("Please Input a number bettween 1000 to 10000")