# robot clone 

from abc import abstractmethod, ABCMeta
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self)->object: pass

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets = []

    def clone(self) -> object:
        return deepcopy(self)

    def __str__(self)->str:
        return str(self.assets)

def client_code()->None:
    k1 = Knight()
    k1.assets.append(1)
    print(k1)

    k2 = k1.clone()
    k2.assets.append(2)
    print(k2)
    print(k1)

if __name__ == '__main__':
    client_code()