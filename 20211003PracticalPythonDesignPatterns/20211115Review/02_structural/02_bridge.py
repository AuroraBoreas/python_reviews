# Abstraction - bridge - Implementation

from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self.imp = imp

    def operation(self)->None:
        self.imp.do_this()
        print(f'{self!r}: implemented on platformA')

class ExtendedAbstraction(Abstraction):
    def operation(self) -> None:
        self.imp.do_that()
        print(f'{self!r}: implemented on platformB')

class Implementation(metaclass=ABCMeta):
    @abstractmethod
    def do_this(self)->None:
        pass

class ImplementationA(Implementation):
    def do_this(self) -> None:
        print(f'{self!r}: do_this')

class ImplementationB(Implementation):
    def do_that(self)->None:
        print(f'{self!r}: do_that')

def client_code()->None:
    ab = Abstraction(ImplementationA())
    ea = ExtendedAbstraction(ImplementationB())
    ab.operation()
    ea.operation()