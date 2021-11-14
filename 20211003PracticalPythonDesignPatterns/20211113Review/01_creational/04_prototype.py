# clone
from copy import deepcopy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self)->object:
        pass

class Concrete(Prototype):
    def clone(self) -> object:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self.assets = []

    def clone(self) -> object:
        return deepcopy(self)
    
    def __str__(self)->str:
        return '{0}'.format(', '.join(map(str, self.assets)), end='')

def client_code()->None:
    k1 = Knight()
    k1.assets.append(1)
    print('k1:', k1)

    k2 = k1.clone()
    k2.assets.append([1, 2])
    print('k2:', k2)
    print('k1:', k1)

if __name__ == '__main__':
    client_code()