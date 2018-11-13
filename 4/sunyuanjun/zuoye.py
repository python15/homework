numbers = [2,1,3,5,8,7]
group = {8,3,1}


def sort_priority(numbers,group=None):
    if group == None:
        group = []
    target1 = []
    target2 = []
    for i in numbers:
        target1.append(i) if i in group else target2.append(i)
    target1.sort()
    target2.sort()
    new_num = [i for i in target1]
    for i in target2:
        new_num.append(i)
    return new_num

print(sort_priority(numbers,group))



