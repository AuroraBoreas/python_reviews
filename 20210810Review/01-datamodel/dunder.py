"Python is a protocol orientated language, every top-level function has a corresponding dunder method" 

from typing import TypeVar
T = TypeVar('T', int, float, complex)

class Polynomial:
    __slots__ = ('args', '_price')
    x = y =  0
    def __init__(self, *args: T):
        self.args   = args
        self._price = 42

    def __repr__(self):
        return 'Polynomial{!r}'.format(self.args)
    
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))
    
    def __sub__(self, other):
        return Polynomial(*(x - y for x, y in zip(self.args, other.args)))
    
    @classmethod
    def hello(cls, name:str)->str:
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
        del self._price    
    
if __name__ == '__main__':
    p1 = Polynomial(1,2,3)
    p2 = Polynomial(4,5,6)
    print(p1 - p2)