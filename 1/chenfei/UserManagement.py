Information = {
    'lebron': {'age': 33,'tel': '231231'},
    'wade': {'age': 35,'tel': '123523'},
    'paul': {'age': 32,'tel': '124712'}
}


def Format(name,age,tel, s='def_action'):
    '''格式化输出'''
    s = Act
    print('{:#^30}'.format(s))
    print('Name: {}\nAge: {}\nTel: {}\n'.format(name,age,tel))


flag = False
while not flag:
    Act = input('Action(delete|update|find|list|exit): ')
    if Act == 'exit':
        break
    elif Act == 'list':
        for k, v in Information.items():
            Format(k,v['age'],v['tel'])
    else:
        Name = input('username: '.strip())
        if Name in Information:
            if Act == 'delete':
                Information.pop(Name)
                print('{} is deleted.'.format(Name)) if Name not in Information else print('Faild to delete.')
            elif Act == 'update':
                Age = int(input('Age: '))
                Tel = input('Tel: ')
                Information.update({Name:{'age': Age,'tel': Tel}})
                Format(Name,Age,Tel)
            elif Act == 'find':
                Format(Name,Information[Name]['age'],Information[Name]['tel'])
            elif Act == 'exit':
                flag = True
            elif Act == 'list':
                continue
        else:
            print('{} is not in Information,Repeat it!'.format(Name))


# Format 这个函数里面的参数 s='def_action' 好像没有用上，还有能不能把delete|update|find|list|exit做成独立的函数呢，最好在加个add的操作