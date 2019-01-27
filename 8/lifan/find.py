'''
本周作业内容：
知识点要求：需要学到35节知识。
用python 简单实现下 linux中的find命令，并且用装饰器加上查询所用的时间：要求类和对象装饰器来实现
'''

from pathlib import Path
import subprocess, argparse, datetime, time
from functools import wraps


class TimeIt:
    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)

    def __get__(self, instance, owner):
        start = datetime.datetime.now()
        ret = self.fn(instance)
        stop = (datetime.datetime.now() - start).total_seconds()
        print("The function runs at {}".format(stop))
        return ret


class FileFind:
    '''
    find directory files
    '''
    argDict = {'f': 'is_file()', 'd': 'is_dir()', 'b': 'is_block_device()', 's': 'is_socket()'}

    def __init__(self, path=None, name=None, type=None, user=None):
        self.path = path
        self.file = []
        self.name = name
        self.type = type
        self.user = user

    @TimeIt
    def find(self):
        time.sleep(3)
        for i in Path(self.path).rglob(self.name):
            if self.user is None:
                if i.stat().st_uid >= 0 and eval('i{}'.format(('.' + self.argDict.get(self.type)) if self.argDict.get(self.type) else '')):
                    self.file.append(i)
            else:
                self.user = int(self.user)
                if i.stat().st_uid == self.user and eval('i{}'.format(('.' + self.argDict.get(self.type)) if self.argDict.get(self.type) else '')):
                    self.file.append(i)
        return self.file


parser = argparse.ArgumentParser(prog='find', add_help=True, description='find directory files')
parser.add_argument('path')
parser.add_argument('-type', help='''
             True if the file is of the specified type.  Possible file types are as follows:
             b: block special,
             s: socket,
             f: file,
             d: directory,
''')
parser.add_argument('-name', default='*')
parser.add_argument('-user')
args = parser.parse_args()
f = FileFind(args.path, name=args.name, type=args.type, user=args.user)
print(f.__doc__)
for i in f.find: print(i)

'''
localhost:8 Fan$ python3.6  find.py  -h
usage: find [-h] [-type TYPE] [-name NAME] [-user USER] path

find directory files

positional arguments:
  path

optional arguments:
  -h, --help  show this help message and exit
  -type TYPE  True if the file is of the specified type. Possible file types
              are as follows: b: block special, s: socket, f: file, d:
              directory,
  -name NAME
  -user USER
  
localhost:8 Fan$ python3.6  find.py /tmp/logs/ -type f -name *log -user 501
The function runs at 3.006335
/tmp/logs/tomcat.log
/tmp/logs/httpd.log
'''
# 可以，结合argparse来做个更好