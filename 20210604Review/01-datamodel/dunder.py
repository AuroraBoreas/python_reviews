"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import typing
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

T = typing.TypeVar("T", int, float)
List = typing.List

class Polynomial:
    __slots__ = ['x', 'y']

    x = 42
    y = 69

    def __init__(self, *args: T)->None:
        self.args  = args
        self._price = 1

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
    def say(self, seq: List[T])->None:
        logging.debug(repr(seq))
    
    @property
    def price(self)->str:
        return self._price
    @price.setter
    def price(self, val)->None:
        self._price = val
    @price.deleter
    def price(self)->None:
        del self._price

if __name__ == "__main__":
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(1, 2, 3)
    logging.debug(p1 + p2)
