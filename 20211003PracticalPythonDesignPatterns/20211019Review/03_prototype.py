# prototype

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype:
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self): 
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)


class Knight(Concrete):
    def __init__(self):
        self.assets = [[]]
    
    def clone(self):
        return deepcopy(self)

if __name__ == '__main__':
    k1 = Knight()
    k2 = k1.clone()
    assert k1 == k2, 'k1 neq k2'
    assert k1 is k2, 'k1 is not k2'