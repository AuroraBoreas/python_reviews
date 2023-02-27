# 

from abc import ABC, abstractmethod
import copy
from typing import Self


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError
    
class Concrete(Prototype):
    def clone(self) -> Self:
        return copy.deepcopy(self)
    
class Knight(Concrete):
    def __init__(self) -> None:
        self.vals: list[int] = [0] * 3

    def __getitem__(self, i: int) -> int:
        return self.vals[i]
    
    def __setitem__(self, i: int, what: int) -> int:
        self.vals[i] = what

    def __str__(self) -> str:
        return f"{self.vals}"
    
    def clone(self) -> Self:
        return copy.deepcopy(self)
    
def client_code() -> None:
    k1: Knight = Knight()
    k1[0] = 1
    k2: Knight = k1.clone()
    k1[1] = 3
    k2[1] = 4
    print(k1)
    print(k2)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()