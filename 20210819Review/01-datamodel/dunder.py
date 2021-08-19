#"Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented" 

"""

>>> p1 = Polynomial(1, 2, 3)
>>> p2 = Polynomial(1, 2, 3)
>>> print(p1 + p2)
>>> assert str(p1+p2)=='Polynomial(2, 4, 6)'
>>> assert p1.price != 42 # error
>>> p2.price = 24
>>> assert p2.price == 24

"""
from typing import TypeVar
T = TypeVar('T', int, float, complex)

class Polynomial:
    __slots__ = ('args', '_price')
    x = y = 42

    def __init__(self, *args: T):
        self.args = args
        self._price = 42

    def __repr__(self):
        return 'Polynomial{!r}'.format(*self.args)

    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.args, other.args)))

    def __call__(self):
        return 'U call I come'

    @staticmethod
    def buff(name:str)->str:
        return 'buff me pls!'
    
    @classmethod
    def read(cls, name:str)->str:
        return 'read ' + name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val:T):
        self._price = val
    
    @price.deleter
    def price(self):
        del self._price

if __name__ == '__main__':
    import doctest
    doctest.testmod()