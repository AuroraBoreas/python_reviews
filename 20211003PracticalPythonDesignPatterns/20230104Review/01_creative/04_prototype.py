"#" 

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Self

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError()

class Concrete(Prototype):
    def clone(self) -> Self:
        return deepcopy(self)

class Knight(Concrete):
    def __init__(self) -> None:
        self._vals: list[int] = list()

    def clone(self) -> Self:
        return deepcopy(self)
    
    def add(self, item: int) -> None:
        self._vals.append(item)

    def __str__(self) -> str:
        return f"{self.__class__} : {self._vals}"

def client_code(k: Knight) -> None:
    logging.info("before clone")
    logging.info(k)
    k1: Knight = k.clone()
    k.add(1)
    logging.info("after clone")
    logging.info(k)
    logging.info(k1)

def main() -> None:
    k: Knight = Knight()
    k.add(0)
    client_code(k)

if __name__ == '__main__':
    main()