#　第四周作业
#　知识要求：学习了高阶函数
# 假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时要把现在的某个群组内的数字，放到群组外的那些数字之前，这个题考察如何把重要元素或
#　其他的事件优先显示在其他的内容前面。
# 提示：可以用高阶函数来实现，如：
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {2, 3, 5, 7}
# sort_priority(numbers,group)
# print(numbers)
#
# #　结果
# [2,3,5,7,1,4,6,8]
import datetime

numbers = [8, 3, 1, 2, 5, 4, 7,7, 6]
group = {3, 2, 5, 7, 9}
start = datetime.datetime.now()


def sort_priority(numbers,group):

    def sort_group():
        lstg =[]
        for x in group:
            for i,y in enumerate(lstg):
                if x < y:
                    lstg.insert(i,x)
                    break
            else:
                lstg.append(x)
        return sort_list(lstg)

    def sort_list(lst):
        lstl = []
        grp = set(numbers) - group
        for x in grp:
            for i,y in enumerate(lstl):
                if x < y:
                    lstl.insert(i,x)
                    break
            else:
                lstl.append(x)
        return lst+lstl

    return sort_group

t=sort_priority(numbers,group)
print(t())
print(datetime.datetime.now()-start)

# 逻辑上是没有什么问题的，但还有优化的空间，想想
