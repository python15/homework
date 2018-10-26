"""
    假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时，要把出现
    在的某个群组内的数字，放到群组外的那些数字之前，这个题考的是如何把重要
    的元素或者其他的事件优先显示在其他的内容前面。
"""

def sort_priority(numbers):
    numbers = sorted(numbers)
    def _sort(group):
        j = 0
        for i in range(len(numbers)):
            if numbers[i] in group:
                numbers.insert(j,numbers.pop(i))
                j +=1
        return numbers
    return _sort

numbers_List = [8,3,1,2,5,4,7,6]
group ={2,3,5,7}
print(sort_priority(numbers_List)(group))


