#!/bin/python3.6

group = {2, 3, 5, 7, 0}
numbers = [8, 3, 1, 2, 5, 4, 7, 0, 6]

def separateGroupNum(group, src):
    part1 = []
    part2 = []
    for i in range(len(src)):
        part1.append(src[i]) if src[i] in group else part2.append(src[i])

    for i in range(len(part2)):
        part1.append(part2[i])
    return part1

def sortList(src, group, key = separateGroupNum):
    lst = sorted(src)
    return key(group, lst)

lst = sortList(numbers,group,separateGroupNum)
print(lst)

# 还有优化的空间，想想
