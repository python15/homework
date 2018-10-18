# !/usr/bin/env python
# -*- coding:utf-8 -*-

#  auth:         fengcheng
#  commit_day:   2018-09-26
'''
假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时，要把出现在的某个群组内的数字，放到群组外的那些数字之前，这个题考的是如何把重要的元素或者其他的事件优先显示在其他的内容前面。
提示：这个题可以用个高阶函数来实现

'''

import sys,os
import re
number = [3,1,4,5,2,9,6]
group = {4,7,6,1}
numbers = [(1,x) for x in number]
groups = [(0,y) for y in group]

def sort_pro(numbers,groups):
    res = []
    res1 = []
    for s in sorted(groups,key = lambda x:x[1]):
        res.append(s[1])
    for m in sorted(numbers,key = lambda x:x[1]):
        if m[1] in res:
            pass
        else:
            res1.append(m[1])
    return res+res1
print(sort_pro(numbers,groups))

'''
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面  亲爱的们 额外添加一个一题  给你们的国庆更加充实
'''

s = "So763ratiDMng14lLYy52hm98"
print('初始值:'+s)


def sort_str(m):
    str_lower = ''.join(re.findall(r'[a-z]+',s))
    str_upper = ''.join(re.findall('[A-Z]+',s))
    S = ''.join((lambda x:(x.sort(),x)[1])(list(str_lower)))
    S1 = ''.join((lambda x:(x.sort(),x)[1])(list(str_upper)))

    l = [int(x) for x in ''.join(re.findall('\d+',s))]
    data = sorted([y for y in filter(lambda x:int(x)%2 == 0,l)])
    
    data1 = sorted(list(set(l).difference(set(data))))
    data2 = ''.join(str(x) for x in data1)+''.join(str(y) for y in data)

    return S+S1+data2


print("排序后:"+sort_str(s))

# 两个都有优化的空间