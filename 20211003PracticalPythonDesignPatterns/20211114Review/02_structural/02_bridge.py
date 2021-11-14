# Abstraction - bridge - Implementation
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self.imp = imp

    def operation(self)->None:
        self.imp.do_this()
        print(f'{self!r}: implemented in platformA')

class ExtendedAbstraction(Abstraction):
    def __init__(self, imp: Implementation) -> None:
        super().__init__(imp)

    def operation(self) -> None:
        self.imp.do_this()
        print(f'{self!r}: implemented in platformB')

class Implementation(ABC):
    @abstractmethod
    def do_this(self)->None: pass

class ImplementationA(Implementation):
    def do_this(self) -> None:
        print(f'{self!r}: im doing something important A')

class ImplementationB(Implementation):
    def do_this(self) -> None:
        print(f'{self!r}: im doing something important B')

def client_code()->None:
    ai = Abstraction(ImplementationA())
    ai.operation()

    bi = ExtendedAbstraction(ImplementationB())
    bi.operation()

if __name__ == '__main__':
    client_code()