'''
第六周作业：
知识要求：至少需要学到30章的内容
编写一个学生管理系统类—Gradebook:
要求能动态的添加学生-name 和学生成绩grades(一个学生可以有个多科的科目成绩)，并
且根据学生名字能算出学生的平均成绩：
提示：可以预先初始化一个字典，用实例字典存储相应的信息
'''

from functools import wraps
import getpass


class login:
    loginInfo = {'张三': '12345', '王二': '111111'}

    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        if self.loginInfo.get(args[0]) == args[1]:
            print('验证通过!')
            ret = self.fn(*args, **kwargs)
            return ret

        print('验证失败!')


@login  # Gradebook = login(Gradebook)
class Gradebook:
    '''
    Student management system
    '''
    stInfo = {}

    def __init__(self, name, passwd):
        self.nameInfo = {}
        self.name = name
        self.passwd = passwd

    def __setitem__(self, key, value):
        self.nameInfo[key] = value
        self.stInfo[self.name] = self.nameInfo

    def __getitem__(self, item):
        try:
            return self.stInfo[item]
        except:
            return self.__missing__(self)

    def __missing__(self, key):
        return '{} 目前没有课程成绩！'.format(self.name)

    def __repr__(self):
        return self.__doc__

    @property
    def avgScores(self):
        k = [v for _, v in self.nameInfo.items()]
        if k:
            return sum(k) // len(k)
        return '{} 目前没有课程成绩！'.format(self.name)


name = input('用户：')
passwd = getpass.getpass('密码: ')

st = Gradebook(name, passwd)
if st:
    print(st)
    while True:
        select = input('1.查看成绩\n2.设置成绩\n3.平均成绩\n4.退出\n>>>>>>>>>>:')
        if select == '1':
            if isinstance(st[name], dict):
                [print(i, v) for i, v in st[name].items()]
            else:
                print(st[name])
        elif select == '2':
            course = input('课程名：')
            results = int(input('成绩：'))
            st[course] = results
        elif select == '3':
            print('{}平均成绩为:{}'.format(name, st.avgScores))
        elif select == '4':
            break

'''
localhost:6 Fan$ python3.6 Gradebook.py
用户：张三
密码:
验证通过!

    Student management system

1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:1
张三 目前没有课程成绩！
1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:2
课程名：语文
成绩：100
1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:2
课程名：数学
成绩：60
1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:1
语文 100
数学 60
1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:3
张三平均成绩为:80
1.查看成绩
2.设置成绩
3.平均成绩
4.退出
>>>>>>>>>>:4
'''
