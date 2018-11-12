def monetary_unit(nums,unit=0):
    nums_dict = {0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
    unit_dict = {0:'',1:'元',2:'拾',3:'佰',4:'仟'}
    return nums_dict[nums]+unit_dict[unit]

def cn(number,count=1,result=''):
    x,y = divmod(number,10)
    if y == 0:
        if count == 1:
            result = '元'+result
        else:
            result = monetary_unit(y) + result
    else:
        result = monetary_unit(y,count) + result

    if '零零' in result:
        result = result.replace('零零','零')

    if '零元' in result:
        result = result.replace('零元','元')

    if x > 0:
        return cn(x,count+1,result)

    return result


while 1:
    strs = input('请输入10000以内数字或输入exit退出:')
    if strs == 'exit':
        print('退出程序')
        break
    elif not strs.isdigit():
        print('您的输入有误!')
        continue
    else:
        number = int(strs)
        if number >= 10000:
            print('您输入的数字过大!')
            continue
        else:
            print(cn(number))

# 代码测试了没有什么问题，写的不错，继续加油~