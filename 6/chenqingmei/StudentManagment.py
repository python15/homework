#!/bin/python3.6

from week6.Student import Student
from week6.Gradebook import Gradebook

def getname():
      return input('input student name >>')

def getnewCh():
      return int(input('input new Chinese grade >>'))

def getnewMath():
      return int(input('input new Math grade >>'))

def getnewEn():
      return int(input('input new English grade >>'))

s1 = Student('Li', 60, 70, 80)
s2 = Student('Geo', 70, 80, 90)
s3 = Student('He', 88, 90, 85)

commands = ['add', 'delete', 'average', 'show', 'showAll',
            'changeCh', 'changeMath', 'changeEn', 'batchChange', 'changeName',
            'exit']
#commands register
add = Gradebook.add
delete = Gradebook.remove
average = Gradebook.average
show = Gradebook.show
showAll = Gradebook.showAll
changeCh = Gradebook.changeCh
changeMath = Gradebook.changeMath
changeEn = Gradebook.changeEn
batchChange = Gradebook.batchChange
changeName = Gradebook.changeName

#init dict
add(s1)
add(s2)
add(s3)

#command declare
print('In this program, the follow commands can be supported:\n'
      'add         ------ add student information,\n'
      'delete      ------ delete student information\n'
      'average     ------ get the average of one student\n'
      'show        ------ print grade information of one student\n'
      'showAll     ------ print all the grade information\n'
      'changeCh    ------ modify the Chinese grade of one student\n'
      'changeMath  ------ modify the Math of one student\n'
      'changeEn    ------ modify the English grade of one student\n'
      'batchChange ------ modify the grade of the three subjects\n'
      'changeName  ------ modify the name of one student\n'
      'exit        ------ exit the program')

while True:
      cmd = input('>>>')
      if cmd not in commands:
            print('Invalid command!')
            continue
      #add
      if cmd == commands[0]:
            name = getname()
            ch = int(input('input Chinese grade >>'))
            math = int(input('input Math grade >>'))
            en = int(input('input English grade >>'))
            add(Student(name, ch, math, en))
            print('finished!')
            continue
      #delete
      if cmd == commands[1]:
            name = getname()
            delete(name)
            print('finished!')
            continue
      #average
      if cmd == commands[2]:
            name = getname()
            print(*average(name))
            continue
      #show
      if cmd == commands[3]:
            name = getname()
            show(name)
            continue

      #showAll
      if cmd == commands[4]:
            showAll()
            continue

      #changeCh
      if cmd == commands[5]:
            name = getname()
            ch = getnewCh()
            changeCh(name, ch)
            print('finished!')
            continue

      #changeMath
      if cmd == commands[6]:
            name = getname()
            math = getnewMath()
            changeMath(name, math)
            print('finished!')
            continue

      #changeEn
      if cmd == commands[7]:
            name = getname()
            en = getnewEn()
            changeEn(name, en)
            print('finished!')
            continue

      #batchChange
      if cmd == commands[8]:
            name = getname()
            ch = getnewCh()
            math = getnewMath()
            en = getnewEn()
            batchChange(name, ch, math, en)
            print('finished!')
            continue

      #changeName
      if cmd == commands[9]:
            oldname = input('input old name >>')
            newname = input('input new name >>')
            changeName(oldname, newname)
            print('finished!')
            continue

      #exit
      if cmd == commands[10]:
            exit()

