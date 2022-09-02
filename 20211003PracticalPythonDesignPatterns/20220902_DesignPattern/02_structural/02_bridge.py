"#" 
from __future__ import annotations
from abc import ABC, abstractmethod

class Abstract:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp
    
    def fuckit(self) -> None:
        print(f'{self.__class__} implemented on platform A -> {self._imp.do_this()}')

class ExtendedAbstract(Abstract):    
    def fuckit(self) -> None:
        print(f'{self.__class__} implemented on platform B -> {self._imp.do_this()}')

class Implementation(ABC):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

def client_code() -> None:
    i1:Implementation = ImplementationA()
    i2:Implementation = ImplementationB()
    a1:Abstract = Abstract(i1)
    a2:Abstract = ExtendedAbstract(i2)
    a1.fuckit()
    a2.fuckit()

if __name__ == '__main__':
    client_code()