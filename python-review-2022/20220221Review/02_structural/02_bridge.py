# 

from __future__ import annotations
from abc import ABC


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp

    def operation(self)->None:
        print(f'{self.__class__} : operation -> {self._imp.do_this()}')

class ExtendedAbstraction(Abstraction):
    def operation(self) -> None:
        print(f'{self.__class__} : operation -> {self._imp.do_this()}')

class Implementation(ABC):
    def do_this(self)->str: raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : implemented on platformA'

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : implemented on platformB'