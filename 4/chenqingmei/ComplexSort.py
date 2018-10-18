#!/bin/python3.6

string = 'HelpSorting179062345'

def complexSort(src: str):
    oddNum = []
    evenNum = []
    lowerLetter = []
    upperLetter = []
    for i in range(len(src)):
        if src[i].isdigit():
            oddNum.append(src[i]) if (int.from_bytes(src[i].encode(), 'big')) % 2 else evenNum.append(src[i])
        elif src[i].isalpha():
            lowerLetter.append(src[i]) if src[i].islower() else upperLetter.append(src[i])
    oddNum = sorted(oddNum)
    evenNum = sorted(evenNum)
    lowerLetter = sorted(lowerLetter)
    upperLetter = sorted(upperLetter)
    return ''.join(oddNum)+''.join(evenNum)+''.join(lowerLetter)+''.join(upperLetter)

print(complexSort(string))
# 这个方法可以，想下如果我只用一句代码如何实现？