import json
user_table = {}
db = 'pas.db'
choices = ('list','delete','update','find','add','exit')
try:
    f = open(db,'r')
    json.load(f)
except Exception as e:
    f = open(db,'w')
    json.dump(user_table,f)
finally:
    f.close()

def input_name():
    name = input('input user name: ')
    return name
def chk_name(name,user):
    if not user:
        print('no such user: "{}" ,you can add it'.format(name))
        return False

def chk_user():
    with open(db,'r') as f:
        deal = json.load(f)
        name = input_name()
        user = deal.get(name)
    return deal,name,user

def save_data(deal):
    with open(db, 'w') as f:
        json.dump(deal, f)
    print('save success')

def input_data():
    age = input('>> input {} age: '.format(name))
    tel = input('>> input {} tel: '.format(name))
    pas = str(input('>> input {} pass: '.format(name)))
    deal[name] = {'age': age, 'tel': tel, 'pas': pas}
    return deal

while True:
    opt = input('cmd > ')
    if opt == 'exit':
        print('exit program.')
        break

    elif opt=="" or opt not in choices:
        print('choice from {}: '.format(choices))

    elif opt == 'find':
        deal,name,user = chk_user()
        if not user:
            print('no such user: "{}" ,you can add it'.format(name))
            continue
        print('user: {}\tage: {}\ttel: {}\tpass: {}'.format(name,user.get('age'),user.get('tel'),'*'*len(user.get('pas'))))

    elif opt == 'add':
        deal,name, user = chk_user()
        if user:
            print('error, {} info already exists!'.format(name))
            continue
        save_data(input_data())

    elif opt == 'update':
        deal, name, user = chk_user()
        if not user:
            print('no such user: "{}" ,you can add it'.format(name))
            continue
        getpas = input('check {} pass: '.format(name))
        if getpas != user.get('pas'):
            print('{} auth error!'.format(name))
            continue
        save_data(input_data())

    elif opt == 'list':
        with open(db,'r') as f:
            t=[]
            mod = input('sort mod,choice from "name,age,tel",default: "name": ')
            for k,v in json.load(f).items():
                t.append((k,v.get('age'),v.get('tel'),'*'*len(v.get('pas'))))
            if mod in ["","name"]:
                [print(i) for i in sorted(t,key=lambda x:x[0],reverse=True)]
            elif mod == "age":
                [print(i) for i in sorted(t,key=lambda x:x[1],reverse=True)]
            elif mod == "tel":
                [print(i) for i in sorted(t,key=lambda x:x[2],reverse=True)]

    elif opt == 'delete':
        deal, name, user = chk_user()
        if not user:
            print('no such user: {}'.format(name))
            continue
        getpas = input('check {} pass: '.format(name))
        if getpas != user.get('pas'):
            print('{} auth error!'.format(name))
            continue
        del deal[name]
        save_data(deal)


