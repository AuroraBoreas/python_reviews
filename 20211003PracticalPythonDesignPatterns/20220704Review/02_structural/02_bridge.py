"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Abstract:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp

    def operation(self) -> str:
        return f'{self.__class__} : operation -> ({self._imp.do_this()})'

class ExtendedAbstract(Abstract):
    def operation(self) -> str:
        return f'{self.__class__} : operation -> ({self._imp.do_this})'

class Implementation(metaclass=ABCMeta):
    @abstractmethod
    def do_this(self) -> str: raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'
    