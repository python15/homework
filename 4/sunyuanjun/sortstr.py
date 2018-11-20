s = 'Sorting1234'


def sortstr(src,target=None):
    if target == None:
        target = []
    for i in src:
        target.append(ord(i))
    #print(target)
    #抽取大写字母、小写字母、数字
    numbers = []
    lowers = []
    uppers = []
    for i in target:
        if i <= 57:
            numbers.append(i)
        elif i >= 90:
            lowers.append(i)
        else:
            uppers.append(i)
    #排序
    lowers.sort()
    uppers.sort()
    nums1 = []
    nums2 = []
    for i in numbers:
        nums1.append(i) if i % 2 else nums2.append(i)
    new_nums = sorted(nums1) + sorted(nums2)
    new_list = lowers + uppers + new_nums
    newstr = ''.join(chr(i) for i in new_list)

    return newstr


print(sortstr(s))
# 写出来已经很不错了，不过这个还有更好的方法，元组排序和lambda 函数