# prototype

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from typing import Any

class Prototype:
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self): raise NotImplementedError()


class Concrete(Prototype):
    def clone(self) -> Any:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self):
        self.assets = []

    def __str__(self) -> str: return '{0!r} {1}'.format(self, self.assets)

    def clone(self) -> Any:
        return deepcopy(self)


if __name__ == '__main__':
    k1 = Knight()
    k2 = k1.clone()
    print(k1)
    print(k2)
    print(k1 == k2)
    print(k1 is k2)