"#" 

from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Abstract:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp
    def operate(self) -> None:
        print(f'{self._imp.do_this()} on {self.__class__} platform')

class ExtendedAbstract(Abstract):
    def operate(self) -> None:
        print(f'{self._imp.do_this()} on {self.__class__} platform')

class Implementation:
    __metaclass__ = ABCMeta

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
    a:Implementation = ImplementationA()
    b:Implementation = ImplementationB()
    c:Abstract = Abstract(a)
    d:Abstract = ExtendedAbstract(b)
    c.operate()
    d.operate()

if __name__ == '__main__':
    client_code()