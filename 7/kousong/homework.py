#seventh week
import pickle
import json


class Mixin:
    def __init__(self,d):
        self.d = d

    def to_dict(self):
        d=self.__dict__

        pick=pickle.dumps(d)
        p=pickle.loads(pick)
        print('pickle          ',pick,p)

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')

        jas=json.dumps(d)
        j=json.loads(jas)
        print('jason           ',jas,j)

class A(Mixin):
    pass


a=A(True)
a.to_dict()
“”“”
mixin比较简单的
“”“”
