
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
        self._values: list[int] = list()

    def add(self, item: int) -> None:
        self._values.append(item)

    def clone(self) -> Self:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"values: {', '.join(map(str,self._values))}"

def client_code() -> None:
    k1: Knight = Knight()
    k1.add(1)
    print(f"{k1=}")
    k2: Knight = k1.clone()
    k2.add(2)
    print(f"{k1=}")
    print(f"{k2=}")

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
