# 
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp

    def operation(self)->None:
        print(f'{self.__class__}: {self._imp.do_this()}')

class ExtendedAbstraction(Abstraction):
    def operation(self) -> None:
        print(f'{self.__class__}: {self._imp.do_this()}')


class Implementation(ABC):
    @abstractmethod
    def do_this(self)->str:
        pass

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this on platformA'

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this on platformB'