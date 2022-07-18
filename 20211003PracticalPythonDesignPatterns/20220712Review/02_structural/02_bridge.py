"#" 
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstract:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp
    
    def operate(self) -> None:
        print(f'{self.__class__} implemented on platform {self._imp.do_this()}')

class ExtendedAbstract(Abstract):
    def operate(self) -> None:
        print(f'{self.__class__} implemented on platform {self._imp.do_this()}')

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
    