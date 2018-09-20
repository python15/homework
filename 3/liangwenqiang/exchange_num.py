import re
class OutNum(object):
    def __init__(self):
        self.num={'1':"壹", '2':"贰", '3':"叁", '4':"肆", '5':"伍", '6':"陆", '7':"柒", '8':"捌",'9':"玖",'0':"零"}
        self.mul={'1':self.num.get('0'),'10':'拾','100':'佰','1000':'仟'}

    def once(self):
        print(self.num.get(getnum))

    def twice(self):
        self.result = self.num.get(getnum[0])+self.mul.get('10')+\
                      self.num.get(getnum[1])
        print(re.sub(r'零','',self.result))

    def thrice(self):
        self.result = self.num.get(getnum[0])+self.mul.get('100')+\
                      self.num.get(getnum[1])+self.mul.get('10')+\
                      self.num.get(getnum[2])
        print(re.sub(r'零+$','',re.sub(r'零\w?','零',self.result)))

    def quartic(self):
        self.result = self.num.get(getnum[0])+self.mul.get('1000')+\
                      self.num.get(getnum[1])+self.mul.get('100')+\
                      self.num.get(getnum[2])+self.mul.get('10')+\
                      self.num.get(getnum[3])
        print(re.sub(r'零+$','',re.sub(r'零+','零',re.sub(r'零\w?','零',self.result))))

if __name__ == "__main__":
    C = OutNum()
    while True:
        origin = input('number(q to quit)> ')
        if origin == 'q':
            print('quit program...')
            break
        if re.search(r'[^\d]+', origin):
            print('all must num!')
            continue
        if re.search(r'^0+$', origin):
            getnum = '0'
        else:
            getnum = re.sub(r'^0+', '', origin)
        if len(getnum) == 1:
            C.once()
        elif len(getnum) == 2:
            C.twice()
        elif len(getnum) == 3:
            C.thrice()
        elif len(getnum) == 4:
            C.quartic()
        else:
            print('out of length!')


