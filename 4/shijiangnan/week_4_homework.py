'''假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时，要把出现在的某个群组内的数字，放到群组外的那些数字之前，这个题考的是如何把重要的元素或者其他的事件优先显示在其他的内容前面。
提示：这个题可以用个高阶函数来实现。如图所示：

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers,group)
print(numbers)

[2,3,5,7,1,4,6,8]
'''


'''
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
[2,3,5,7,1,4,6,8]
numbers_set=set(numbers)
jiaoji=group & numbers_set
chaji=numbers_set - (group & numbers_set)

jiaojilist=list(jiaoji)
group_in=sorted(jiaojilist)

chajilist=list(chaji)
group_out=sorted(chajilist)

for i in group_out:
    group_in.append(i)
print(group_in)

'''

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_numbers=[]
def sort_priority(numbers):
    set_numbers=set(numbers)
    jiaoji=set_numbers & group
    chaji=set_numbers-jiaoji
    def sort_resault(group):
        sort_numbers=sorted(list(jiaoji))
        group_out=sorted(list(chaji))
        for i in group_out:
            sort_numbers.append(i)
        return sort_numbers
    return sort_resault
sort_priority(numbers)(group)

'''
s = "Sorting1234" 
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面

'''

def get_type_list():
    daxiezm=[]
    xiaoxiezm=[]
    jishu=[]
    oushu=[]
    slist=list(s)
    for i in slist:
        if i.isupper():
            daxiezm.append(i)
        elif i.islower():
            xiaoxiezm.append(i)
        elif str(i).isdigit():
            if int(i) % 2 == 0:
                oushu.append(i)
            else:
                jishu.append(i)
    return daxiezm,xiaoxiezm,jishu,oushu
def type_sort():
    upper_dx,lower_xx,digit_js,digit_os=get_type_list()
    hblist=[]
    hblist.append(sorted(upper_dx))
    hblist.append(sorted(lower_xx))
    hblist.append(sorted(digit_js))
    hblist.append(sorted(digit_os))
    for i in hblist:
        for b in i:
            print("".join(b) ,end="")
if __name__=="__main__":
    s = "Sorting1234"    
    type_sort()

# 还有更简单的方法，麻烦想想 ，高阶函数，元组比较




