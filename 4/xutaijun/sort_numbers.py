#!/bin/env python3


def is_set(source_list):
    if not isinstance(source_list,set):
        source_list=set(source_list)
    return source_list


def sort_numbers(numbers,is_set=is_set):
    def _sort_numbers(group):
        sort_all=[]
        sort_all_dict={}
        #create set numbers
        numbers_set=is_set(numbers)
        group_set=is_set(group)
        sort_numbers_set=numbers_set-group_set
        #create tuple
        sort_all.append(group_set)
        sort_all.append(sort_numbers_set)
        for k,v in enumerate(sort_all):
            sort_all_dict[k]=[ (k,i) for i in v]
        #sorted
        sort_source=[]
        for i in sort_all_dict.values():
            sort_source+=i
        result=[ i[1] for i in sorted(sort_source)]
        return result
    return _sort_numbers


numbers=[8,3,1,2,5,4,7,6]
group={2,3,5,7}

print(sort_numbers(numbers)(group))

# 还有优化的空间，再想想，看看能不能用15行之内写出来