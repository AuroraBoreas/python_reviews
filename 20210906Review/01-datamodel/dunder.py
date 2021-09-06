"Python is a protocol orientated lang; every top-level function has a dunder method implemented;" 

from typing import Any, TypeVar
T = TypeVar('T', int, float, complex)

class Polynomial:
    __slots__ = ('args', '_price')
    x = y = 0

    def __init__(self, *args:Any):
        self.args   = args
        self._price = 42

    def __repr__(self):
        return 'Polynomial{!r}'.format(self.args)

    def __add__(self, other):
        return Polynomial(*(x+y for x,y in zip(self.args, other.args)))

    def __call__(self):
        return 'U call I come'

    @classmethod
    def hello(cls, name:str):
        return 'hello ' + name

    @staticmethod
    def say(sth:str)->str:
        return 'say ' + sth

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val:T):
        self._price = val

    @price.deleter
    def price(self):
        del self._1price

if __name__ == '__main__':
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    print(p1 + p2)