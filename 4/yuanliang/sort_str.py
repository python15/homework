"""s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面"""

def sort_str(s):
    def separate(s):
        capital = []
        lower = []
        number = []
        for i in s:
            numbers = ord(i)
            if 47 < numbers < 58:
                number.append(i)
            elif 64 < numbers < 91:
                capital.append(i)
            else:
                lower.append(i)
        return capital, lower, number

    def sort_number(number):
        odd_number = []
        even = []
        for j in sorted(number):
            if int(j) % 2 == 0:
                even.append(j)
            else:
                odd_number.append(j)
        return (odd_number + even)

    capital, lower, number = separate(s)
    number = sort_number(number)
    str_list = ''.join(sorted(lower)+sorted(capital)+number)
    print(str_list)





s = "Sorting1234"
sort_str(s)