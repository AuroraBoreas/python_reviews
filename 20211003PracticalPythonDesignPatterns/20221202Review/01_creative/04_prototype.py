"#" 

from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> object:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> object:
        return copy.deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._data = []
    def clone(self) -> object:
        return copy.deepcopy(self)
    def __str__(self) -> str:
        return f'{self._data}'

def client_code() -> None:
    k1 = Knight()
    k1._data.append(1)
    print(k1)
    k2 = k1.clone()
    k1._data.append(2)
    print(k1)
    print(k2)

if __name__ == '__main__':
    client_code()