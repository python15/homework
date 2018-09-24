num = input('>>>').lstrip('0')
a={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒',
  '8':'捌','9':'玖'}
b=len(num)
s=int(num)//10
g=int(num)%10
if b == 5:
    print('壹万')
else:
    if b <= 2:
        if b == 2:
            if g!=0:
                print('{}拾{}'.format(a[str(s)], a[str(g)]))
            elif g==0:
                print('{}拾{'.format(a[str(s)]))

        else:
            print(a[str(num)])
    else:
        c = int(num) // 100
        s = (int(num) % 100) // 10
        g = (int(num) % 100) % 10
        if len(str(c)) == 2:
            if c%10 ==0 and s!=0:
                print('{}仟{}{}拾{}'.format(a[str(c // 10)], a['0'],a[str(s)], a[str(g)]))
            elif s==0 and c%10!=0:
                print('{}仟{}佰{}{}'.format(a[str(c // 10)], a[str(c % 10)],  a['0'],a[str(g)]))
            elif c%10==0 and s==0:
                print('{}仟{}{}'.format(a[str(c // 10)], a['0'], a[str(g)]))
            else:
                print('{}仟{}佰{}拾{}'.format(a[str(c // 10)], a[str(c % 10)], a[str(s)], a[str(g)]) )
        else:
            if s==0:
                print('{}佰{}{}'.format(a[str(c)], a['0'],a[str(g)]))
            else:
                print('{}佰{}拾{}'.format(a[str(c)],a[str(s)], a[str(g)]))
print()