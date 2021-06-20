"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from typing import (Tuple, TypeVar)
T = TypeVar('T', int, float, complex)

class Polynomial:
    __slots__ = ('args', '_price')
    _x = 0
    _y = 0

    def __init__(self, *args: Tuple[T]):
        self.args   = args
        self._price = 42
    def __repr__(self):
        return "Polynomial{!r}".format(self.args)
    
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))
    
    def __call__(self):
        return 'U call I come'
    
    @classmethod
    def hello(cls, name:str):
        return "hello " + name
    
    @staticmethod
    def say(sth:str):
        return "say " + sth
    
    @property
    def price(self):
        return self._price

    @price.deleter
    def price(self):
        del self._price

    @price.setter
    def price(self, val: T):
        self._price = val

if __name__ == "__main__":
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    print(p1 + p2)