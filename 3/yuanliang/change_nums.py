"""将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为
"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆",
"伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，"""

d = {'0': '零', '1': "壹", '2': '贰', '3': "叁", '4': '肆', '5': "伍", '6': '陆', '7': "柒", '8': '捌', '9': "玖"}
words = ["拾", "佰", "仟", "万", "元"]


def recever_numbers():
    while True:
        num = input("Enter a number>>>").strip()
        if num.isdigit():
            return num
            break
        print("Please enter the correct nums")

def change_num(num):
    length = len(num)
    m = 1
    chinese_num = []
    flag = True

    for i in num:
        if i == '0':
            if flag:
                chinese_num.append(d[i])
                flag = False
            m += 1
            continue
        chinese_num.append(d[i] + words[length - m - 1])
        m += 1
        flag = True

    if not flag:
        chinese_num[-1] = words[-1]
    print(''.join(chinese_num))


change_num(recever_numbers())

# 真的不错，你们太厉害了