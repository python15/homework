"""
用python 简单实现下 linux中的find命令，并且用装饰器加上查询所用的时间：要求类和对象装饰器来实现
"""


import argparse
from pathlib import Path
import datetime
import time
from functools import wraps

parser = argparse.ArgumentParser(prog='find',add_help=False)
parser.add_argument('path',nargs='?',default='.',help="path_help")
parser.add_argument('-name',action='store_true',help='use a long listing format')
parser.add_argument('-type',action='store_true',help='use a long listing format')
parser.add_argument('filename',nargs='?',default=None,)
parser.add_argument('tp',nargs='?',help="find the file with the name")



# def wrapper(fn):
#     def _wrapper(*args,**kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args,**kwargs)
#         time.sleep(0.5)
#         deltime=(datetime.datetime.now()-start).total_seconds()
#         print(deltime)
#         return ret
#     return _wrapper

class timeIt:
    def __init__(self,fn):
        self._fn = fn
        wraps(fn)(self)
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self._fn(*args,**kwargs)
        time.sleep(0.5)
        deltime = (datetime.datetime.now()-start).total_seconds()
        print(deltime)
        return ret

@timeIt
class find:
    def __init__(self,path,flname,tp,name=False,type=False):
        self.path = path
        self.filename = flname
        self.type = tp
        self.tp1 = type
        self.name = name
        self._find()
        print('type',self.type)
        print('tp1', self.tp1)
    def _find(self):
        print('find',self.name)
        if not self.name and not self.tp1:
            self.findall(self.path)
        elif self.name:
            self.findfile(self.path)
        elif self.tp1:
            self.find_type(self.path)

    def findall(self,path):
        print('all')
        p = Path(path)
        for i in p.iterdir():
            if i.is_dir():
                print(i)
                #yield (i)
                try:
                    self.findall(i)
                except Exception as e:
                    print(e)
            else:
                pass
                #yield (i)

    def findfile(self,path):
        p = Path(path)
        if self.filename is not None:
            for i in p.iterdir():
                if i.name == self.filename:
                    print(i)

    def find_type(self,path):
        tp_list = ['b','d','c','p','l','f']
        p = Path(path)
        if self.type is not None and self.type in tp_list:
            for i in p.iterdir():
                if self.type == 'b' and i.is_block_device():
                    print(i)
                if self.type == 'd' and i.is_dir():
                    print(i)
                if self.type == 'c' and i.is_char_device():
                    print(i)
                if self.type == 'l' and i.is_symlink():
                    print(i)
                if self.type == 'f' and i.is_file():
                    print(i)

if __name__ == "__main__":
    args = parser.parse_args('-type c:/ vms f '.split())
    print(args)
    f = find(args.path,args.filename,args.tp,args.name,args.type)
    #f.find_type(args.path)
    #f.findall(args.path)

# 不错！可以加个自动判断系统的，linux和windows