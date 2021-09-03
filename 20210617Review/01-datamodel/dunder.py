"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from typing import (Tuple, Any)

class Polynomial:
    __slots__ = ('args', '_price')
    
    def __init__(self, *args: Tuple):
        self.args   = args
        self._price = 42

    def __repr__(self)->str:
        return "Polynomial{!r}".format(self.args)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))

    def __call__(self)->str:
        return 'U call I come'

    @staticmethod
    def hello(name:str)->str:
        return "hello " + name
        
    @classmethod
    def say(cls, sth:str)->str:
        return f"say {sth}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val: Any)->None:
        self._price = val
    
    @price.deleter
    def price(self)->None:
        del self._price

if __name__ == "__main__":
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    print(p1 + p2)