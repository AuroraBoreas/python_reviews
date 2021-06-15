"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from typing import (AnyStr, TypeVar, Tuple)

T = TypeVar('T', int, float)

class Polynomial:
    __slots__ = ('_price')

    def __init__(self, *args: Tuple):
        self.args = args
        self._price = 42

    def __repr__(self)->str:
        return "Polynomial{!r}".format(self.args)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))

    def __call__(self)->str:
        return 'U call I come'

    @staticmethod
    def hello(name: str)->str:
        return "hello " + name
    
    @classmethod
    def say(cls, sth: AnyStr)->AnyStr:
        return "say " + sth
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val: T):
        self._price = val

    @price.deleter
    def price(self):
        del self._price
