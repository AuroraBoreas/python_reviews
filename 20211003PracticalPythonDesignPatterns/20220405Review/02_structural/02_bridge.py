"#" 
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp
    def implement(self)->None:
        print(f'{self!r}: {self._imp.do_this()}')

class ExtractAbstraction(Abstraction):
    def implement(self) -> None:
        print(f'{self!r}: {self._imp.do_this()}')

class Implementation(ABC):
    @abstractmethod
    def do_this(self)->None: raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> None:
        print(f'{self!r} implemented on platformA')

class ImplementationB(Implementation):
    def do_this(self) -> None:
        print(f'{self!r} implemented on platformB')