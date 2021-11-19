# Abstraction - bridge - Implementation 
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self.imp = imp

    def operation(self)->None:
        print(f'{self.__class__} operates: {self.imp.do_this()}')

class ExtendedAbstraction(Abstraction):
    def operation(self) -> None:
        print(f'{self.__class__} operates: {self.imp.do_this()}')

class Implementation(ABC):
    @abstractmethod
    def do_this(self)->str:
        pass

class ImplementationA(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'

class ImplementationB(Implementation):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'
