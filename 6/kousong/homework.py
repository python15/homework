#sixth week
class A:
    data = {('tom','cha'):'100',('tom','eng'):'60',('jerry','cha'):'80'}
    def __init__(self):
        self.data = A.data

    def add (self,name,sub,grace):
        self.data[(name,sub)]=grace
        """
        这里的A换成self 试试
        """
        
    def ave(self,name):
        sum = 0
        num = 0
        for i in self.data.keys():
            keyname = i[0]
            if keyname == name:
                self.data[i] = int(self.data[i])
                sum +=self.data[i]
                num +=1
        if num:
            print(sum/num)
        else:
            print('no this student')

while True:
    
    han = input('han please:')
    if han=='add':
        a=input('name please')
        b=input('sub please')
        c=input('grace please')
        A().add(a,b,c)
        
    elif han=='ave':
        a=input('name please')
        A().ave(a)
    else:
        print('no this han')
