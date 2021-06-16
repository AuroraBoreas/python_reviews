"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from typing import (Tuple, Any)

class Polynomial:
    __slots__ = ('args', '_status')

    def __init__(self, *args: Tuple):
        self.args = args
        self._status = 404
    
    def __repr__(self):
        return "Polynomial{!r}".format(self.args)
    
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))
    
    def __call__(self)->str:
        return 'U call I come'

    @staticmethod
    def hello(name: str)->str:
        return "hello " + name
    
    @classmethod
    def say(cls, sth: str)->str:
        return "say " + sth
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, val: Any):
        self._status = val
    
    @status.deleter
    def status(self):
        del self._status

if __name__ == "__main__":
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    print(p1 + p2)