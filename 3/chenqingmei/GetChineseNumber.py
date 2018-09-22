#!/bin/python3.6


globalDict = {'0':'零', '1':'壹','2':'贰', '3':'叁', '4':'肆', '5':'伍',
              '6':'陆', '7':'柒', '8':'捌', '9':'玖'}
globalLenDict = {'2':'拾', '3':'佰', '4':'仟'}

def numberInfo(num):
    length = len(num)
    lst = [i for i in range(length) if num[i] == '0']
    return length,lst   #return one tuple which stores the length of number and the index of '0'

#number without '0'
def simpleFormat(len, number, strDict = globalDict, lenDict = globalLenDict, target = ''):
    while True:
        if len == 1:
            target = target + strDict[number[0]]
            break
        else:
            target = target + strDict[number[0]] + lenDict[str(len)]
        number = number[1:]
        len -= 1
        if not len:
            break
        else:
            simpleFormat(len, number,strDict,lenDict, target)
    return target

def complexDeal(info, number, strDict = globalDict, lenDict = globalLenDict, target = []):
    tmpStr= simpleFormat(info[0], number,strDict, lenDict)
    i = 0
    while True:
        if i >= len(tmpStr):
            break
        if tmpStr[i] == '零':
            if i == len(tmpStr) - 1:
                break
            else:
                if tmpStr[i] == tmpStr[i - 2]:
                    i += 2
                    continue
                target.append(tmpStr[i])
                i += 1
        else:
            target.append(tmpStr[i])
        i+=1
    if target[len(target) - 1] == '零':
        target.pop()
    return target



#number with '0'
def specialFormat(info, number, strDict = globalDict, lenDict = globalLenDict, target = ''):
    if number == '0':     #0
        target = strDict[number]
    elif info[0] == len(info[1]) + 1:  #10, 100, 1000
        target = strDict[number[0]] + lenDict[str(info[0])]
    else: #1110,1101,1011,1001,1010,1100
        tmp = complexDeal(info,number)
        target = ''.join(tmp)

    return target

def getChineseNumber(number, fn):
    info = fn(number)
    if not info[1]:
        numberStr = simpleFormat(info[0], number, globalDict, globalLenDict)
        return numberStr
    else:
        numberStr = specialFormat(info, number, globalDict, globalLenDict)
        return numberStr


number = input('>>>').rstrip().lstrip()
if len(number) != 1:
    number = number.lstrip('0')
print(number)
chNumber = getChineseNumber(number,numberInfo)
print(chNumber)

