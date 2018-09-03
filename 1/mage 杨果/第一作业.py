import time

dict_data = {'cat': '15,123456', 'dog':'16,789654', 'pig':'12,1000000', 'admin':'24,18812345678'}
operation = ['delete', 'updata', 'find', 'list', 'exit']
print('欢迎使用简单用户管理系统！')

while 1:
    input_str = input('请输入下列命令执行操作！\ndelete、updata、find、list、exit\n')
    if input_str in operation:
        if input_str == 'updata':
            while 1:
                user_data = input("请输入'用户名:年龄:联系方式'格式的字符串\n")
                data_list = user_data.split(':')
                if len(data_list) == 3:
                    if data_list[0] not in dict_data:
                        flag = input('此用户不存在！\n按A重新输入，按其他回到主选项\n')
                        if flag not in ['A', 'a']:
                            break
                    else:
                        dict_data[data_list[0]] = data_list[1] + ',' + data_list[2]
                        print('输入完成！\n')
                        break
                else:
                    print('输入有误！')
        elif input_str == 'delete':
            while 1:
                username = input("请输入'用户名'格式的字符串\n")
                if username in dict_data:
                    del dict_data[username]
                    print('删除完成！\n')
                    break
                else:
                    flag = input('此用户不存在！\n按A重新输入，按其他回到主选项\n')
                    if flag not in ['A', 'a']:
                        break
        elif input_str == 'find':
            while 1:
                username = input("请输入'用户名'格式的字符串\n")
                if username in dict_data:
                    data_infomation = dict_data[username].split(',')
                    print('用户名：' + username)
                    print('年龄：' + data_infomation[0])
                    print('联系方式：' + data_infomation[1])
                    print('打印完成!\n')
                    break
                else:
                    flag = input('此用户不存在！\n按A重新输入，按其他回到主选项\n')
                    if flag not in ['A', 'a']:
                        break
        elif input_str == 'list':
            for key in dict_data:
                data_infomation = dict_data[key].split(',')
                print('用户名：' + key)
                print('年龄：' + data_infomation[0])
                print('联系方式：' + data_infomation[1])
            print('打印完成！\n')
        elif input_str == 'exit':
            print('退出程序！')
            time.sleep(3)
            exit()
    else:
        print('输入命令错误，请重新输入！')