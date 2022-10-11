#
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self._imp = imp
    def operate(self) -> None:
        return f'{self.__class__} : implemented in platform A {self._imp.do_this()}'

class ExtendedAbstraction(Abstraction):
    def operate(self) -> None:
        return f'{self.__class__} : implemented in platform B {self._imp.do_this()}'

class Implementation(ABC):
    @abstractmethod
    def do_this(self) -> Optional[str]:
        raise NotImplementedError()

class ImplementationA(Implementation):
    def do_this(self) -> Optional[str]:
        return f'{self.__class__} : do_this'

class ImplementationB(Implementation):
    def do_this(self) -> Optional[str]:
        return f'{self.__class__} : do_this'