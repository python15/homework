'''
假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时要把现在的某个群组内的数字，放到群组外的那些数字之前，这个题考察如何把重要元素或
其他的事件优先显示在其他的内容前面。
提示：可以用高阶函数来实现，如：
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers,group)
print(numbers)
结果
[2,3,5,7,1,4,6,8]
'''

import random

numbers = [random.randrange(1024) for i in range(8)]
group = {i: None for i in numbers[:4]}


def sotrNumber(numbers):
    numbers = sorted(numbers)

    def sortGroup(group):
        nonlocal numbers
        for i in group:
            if i in numbers:
                numbers.remove(i)
        return sorted(list(group)) + numbers

    return sortGroup


print("numbers:{}\ngroup:{}\n\n{}".format(numbers, group.keys(),sotrNumber(numbers)(group)))
