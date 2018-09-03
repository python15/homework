import pickle
user_table = {}
db = 'user_table.db'
choices = ('list','delete','update','find')
try:
    f = open(db,'rb')
except Exception as e:
    f = open(db,'wb')
    pickle.dump(user_table,f)
finally:
    f.close()


def chk_name():
    name = input('input user name: ')
    return name


while True:
    opt = input('chk_user > ')
    if opt == 'exit':
        print('exit program.')
        break
    elif opt not in choices:
        print('choice from {}: '.format(choices))
    elif opt == 'find':
        name = chk_name()
        with open(db,'rb') as f:
            deal = pickle.load(f)
            if not deal.get(name):
                print('no such user: "{}" ,you can add it'.format(name))
            else:
                for k,v in deal.items():
                    print('user: {}\tsalary: {}'.format(k,v.get('salary')))
    elif opt == 'update':
        name = chk_name()
        salary = input('input {} salary: '.format(name))
        with open(db,'rb') as f:
            deal = pickle.load(f)
            deal[name] = {'salary':salary}
            with open(db,'wb') as f:
                pickle.dump(deal,f)
                print('save success')
    elif opt == 'list':
        with open(db,'rb') as f:
            for k,v in pickle.load(f).items():
                print('user: {}\tsalary: {}'.format(k,v.get('salary')))
    elif opt == 'delete':
        name = chk_name()
        with open(db,'rb') as f:
            table = pickle.load(f)
            if not table.get(name):
                print('no such user: {}'.format(name))
            else:
                del table[name]
                with open(db,'wb') as f:
                    pickle.dump(table,f)
                print('delete user: {} success'.format(name))



# 看着代码没有什么问题，不过能不能chk_user的时候，提示下用户，有哪些操作呢？