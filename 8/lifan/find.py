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

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self.fn(*args, **kwargs)
        stop = (datetime.datetime.now() - start).total_seconds()
        print("The function runs at {}".format(stop))
        return ret


@TimeIt
class FileFind:
    argDict = {'f': 'is_file()', 'd': 'is_dir()', 'b': 'is_block_device()', 's': 'is_socket()'}

    def __init__(self, path=None):
        self.path = path
        self.file = []

    def find(self, name=None, type=None, user=None):
        for i in Path(self.path).rglob(name):
            if user is None:
                if i.stat().st_uid >= 0 and eval('i{}'.format(('.' + self.argDict.get(type)) if self.argDict.get(type) else '')):
                    self.file.append(i)
            else:
                user = int(user)
                if i.stat().st_uid == user and eval('i{}'.format(('.' + self.argDict.get(type)) if self.argDict.get(type) else '')):
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
f = FileFind(args.path)
for i in f.find(name=args.name, type=args.type, user=args.user): print(i)

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

localhost:8 Fan$  python3.6  find.py  /tmp/logs/ -name *.log -type f -user 0
The function runs at 1.5e-05
/tmp/logs/ssss.log
/tmp/logs/a.log
/tmp/logs/mmmm.log
'''
