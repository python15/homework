'''
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面
'''

s = input("Enter a character with case and number: ")

def strSort(s, digit, lower, capital):
    for i in s:
        if i.isdigit():
            digit.append(i)
        elif i.islower():
            lower.append(i)
        elif i.isupper():
            capital.append(i)

    return "{} {} {}".format(' '.join(sorted(lower)), ' '.join(sorted(capital)),
                             ' '.join(sorted(digit, key=lambda x: int(x) % 2 == 0)))


print(strSort(s,digit=[], lower=[], capital=[]))

# 能写出来 已经是不错了这个，不过用元组排序的方法可能会更好