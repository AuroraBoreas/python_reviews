"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Abstract:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp

    def operate(self) -> str:
        return f'{self.__class__} : {self._imp.do_this()} on platform A'

class ExtendedAbstract(Abstract):
    def operate(self) -> str:
        return f'{self.__class__} : {self._imp.do_this()} on platform B'

class Implementation(ABC):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} implemented on this'

def client_code() -> Optional[str]:
    a1:Abstract = Abstract(ImplementationA())
    a1.operate()
    e1:ExtendedAbstract = ExtendedAbstract(ImplementationA())
    e1.operate()

if __name__ == '__main__':
    client_code()