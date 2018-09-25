import re,readline
class SwNum(object):
    def __init__(self):
        self.num={'1':"壹", '2':"贰", '3':"叁", '4':"肆", '5':"伍", '6':"陆", '7':"柒", '8':"捌",'9':"玖",'0':"零"}
        self.mul={'10':'拾','100':'佰','1000':'仟'}

    def once(self):
        print(self.num.get(n))

    def double(self):
        self.result = self.num.get(n[0])+self.mul.get('10')+\
                      self.num.get(n[1])
        print(re.sub(r'零','',self.result))

    def thrice(self):
        self.result = self.num.get(n[0])+self.mul.get('100')+\
                      self.num.get(n[1])+self.mul.get('10')+\
                      self.num.get(n[2])
        print(re.sub(r'零+$','',re.sub(r'零\w?','零',self.result)))

    def quartic(self):
        self.result = self.num.get(n[0])+self.mul.get('1000')+\
                      self.num.get(n[1])+self.mul.get('100')+\
                      self.num.get(n[2])+self.mul.get('10')+\
                      self.num.get(n[3])
        print(re.sub(r'零+$','',re.sub(r'零+','零',re.sub(r'零\w?','零',self.result))))


if __name__ == "__main__":
    sw = SwNum()
    while True:
        get = input('GET("q" to quit)> ')
        if get == 'q':
            print('quit program...')
            break
        if re.search(r'[^\d]+', get) or get == "":
            print('all must num!')
            continue
        if re.search(r'^0+$', get):
            n = '0'
        else:
            n = re.sub(r'^0+', '', get)
        if len(n) == 1:
            sw.once()
        elif len(n) == 2:
            sw.double()
        elif len(n) == 3:
            sw.thrice()
        elif len(n) == 4:
            sw.quartic()
        else:
            print('out of length!')


# 写的真不错！用正则来实现，可以让大家参考下你的，