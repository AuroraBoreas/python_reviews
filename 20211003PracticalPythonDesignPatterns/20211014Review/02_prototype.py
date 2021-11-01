
#~ prototype

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self): pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self): pass

    def clone(self):
        return deepcopy(self)
