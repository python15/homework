'''
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，
单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",
数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
'''

iNum = input("Please enter 5 digits or less: ")
dConvert = {"0": "零", "1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌", "9": "玖"}
dUnit = [None, None, "拾", "佰", "仟", "万"]
sum = len(iNum)


def convf(dConvert, dUnit, sum, flag=False):
    a = []
    for i in list(iNum):
        if i == '0':
            if not flag:
                a.append(dConvert.get(i))
                flag = True
            sum -= 1
            continue
        a.append(dConvert.get(i) + dUnit[sum]) if dUnit[sum]  else a.append(dConvert.get(i))
        sum -= 1

    if a[-1] == "零":
        a.pop()
    return ''.join(a) + "元" + "整"


print(convf(dConvert, dUnit, sum))
# 有问题哦，00011你测试下