# -*- coding:UTF-8 -*-

num_chinese = {
    0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆',
    5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'
}
decimal_unit = ['元', '拾', '佰', '仟', '万']

def get_num():
    while True:
        orig_num = input("Please enter the original number >>>").lstrip('0')
        if not orig_num.isdigit():
            print("Please enter the digit, try again.")
        elif len(orig_num) > 5:
            print("The received number is less than 6, try again.")
        else:
            break
        # orig_num = '10101'
        
    return orig_num.lstrip('0')

def count_number(num):
    num = str(num)
    n_tuple = num.partition('.')
    count_int = len(n_tuple[0])
    # count_decimal = len(n_tuple[2])
    # if count_int == 1 and n_tuple(0) == '0':
    #     return 0
    # 小数点后几位暂时不作考虑，后续增加完成
    return count_int

def trans(number):
    number = str(number)
    counts = count_number(number)
    # print(counts)
    flag = 0
    for i in range(counts):
        if number[i] == '0':
            flag = 1
            if i == counts-1:
                print("{}".format(decimal_unit[0]))
            else:
                continue
        elif flag:
            print("{}".format(num_chinese[0]), end='')
            print("{}{}".format(num_chinese[int(number[i])], decimal_unit[counts-1-i]), end='')
            flag = 0
        else:
            print("{}{}".format(num_chinese[int(number[i])], decimal_unit[counts-1-i]), end='')

if __name__ == '__main__':
    original_num = get_num()
    trans(original_num)
