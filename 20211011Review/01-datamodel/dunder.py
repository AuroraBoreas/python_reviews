#Python is a protocol orientated lang; every top-level function has a correspoding dunder method implemented; 

from __future__ import annotations
from typing import Any

class Polynomial:
    def __init__(self, *args:Any)->None:
        self.args = args
        self._price = 42

    def __repr__(self)->str:
        return 'Polynomial{0!r}'.format(self.args)

    def __add__(self, rhs:Polynomial)->Polynomial:
        return Polynomial(*(x+y for x,y in zip(self.args, rhs.args)))

    def __call__(self)->str:
        return 'U call I come'

    @classmethod
    def hello(cls, name:str)->str:
        return 'hello ' + name
    
    @staticmethod
    def say(sth:str)->str:
        return 'say ' + sth

    @property
    def price(self)->int:
        return self._price

    @price.deleter
    def price(self)->None:
        del self._price

    @price.setter
    def price(self, val:int)->None:
        self._price = val

if __name__ == '__main__':
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    print(p1 + p2)