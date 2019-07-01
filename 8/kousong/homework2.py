#eighth week 优化2
import datetime,argparse,stat,time,datetime
from pathlib import Path


parser = argparse.ArgumentParser(prog='find')  ###创建解析器
parser.add_argument('path',nargs='?',default='.')    ###为解析器增加参数
parser.add_argument('-name',action='store_true')
parser.add_argument('-type',action='store_true')
parser.add_argument('-perm',action='store_true')
parser.add_argument('-mtime',action='store_true')
args = parser.parse_args(('/home/python/kou/project -name -type -perm -mtime'.split()))         ###参数解析

def timeit(cls):
    def wrapper(show_what,arg):
        now = datetime.datetime.now()
        if args.name and show_what == 'show_name':cls(args.path).show_name(arg)
        elif args.type and show_what == 'show_type':cls(args.path).show_type(arg)
        elif args.perm and show_what == 'show_perm':cls(args.path).show_perm(arg)
        elif args.mtime and show_what == 'show_mtime':cls(args.path).show_mtime(arg)

        dlt = str(datetime.datetime.now() - now)
        h,m,s = dlt.split(':')
        h = int(h)
        m = int(m)
        s1,s2 = s.split('.')
        s = int(s1) + int(s2)/1000000
        all_dlt = h*3600 + m*60 + s
        
        print(all_dlt)
    return wrapper 

@timeit  #FM = timeit (FM)
class Find_Method:
    def __init__(self,path='.'):
        self.path=Path(path)
    def show_name(self,showname=None):
            print([showname for file in self.path.iterdir() if file.name == showname])
    def show_perm(self,showperm=None):
        print([file.name for file in sorted(self.path.iterdir()) if oct(file.stat().st_mode)[-3:] == showperm])
    def show_mtime(self,showmtime=None):
        print([file.name for file in sorted(self.path.iterdir()) if time.time() - showmtime*24*3600 >= file.stat().st_mtime])
    def show_type(self,showtype=None):
        if showtype == 'l':print([file.name for file in sorted(self.path.iterdir()) if file.is_symlink()])
        elif showtype=='p':print([file.name for file in sorted(self.path.iterdir()) if file.is_fifo()])
        elif showtype=='s':print([file.name for file in sorted(self.path.iterdir()) if file.is_socket()])
        elif showtype=='d':print([file.name for file in sorted(self.path.iterdir()) if file.is_dir])
        elif showtype=='f':print([file.name for file in sorted(self.path.iterdir()) if file.is_file()])
        elif showtype=='b':print([file.name for file in sorted(self.path.iterdir()) if file.is_block_device()])
        elif showtype=='a':print([file.name for file in sorted(self.path.iterdir()) if file.is_absolute()])
        elif showtype=='c':print([file.name for file in sorted(self.path.iterdir()) if file.is_char_device()])
        elif showtype=='r':print([file.name for file in sorted(self.path.iterdir()) if file.is_reserved()])
        else:print('-')

Find_Method('show_name','pro')           ###带装饰器功能调用 
Find_Method('show_type','f')             ###带装饰器功能调用 
Find_Method('show_perm','775')           ###带装饰器功能调用 
Find_Method('show_mtime',0.05)           ###带装饰器功能调用 （以‘天’作为单位 ）