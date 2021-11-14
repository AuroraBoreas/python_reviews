# Abstraction - bridge - Implementation 
from __future__ import annotations
from abc import ABC


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self.imp = imp
    
    def operation(self)->None:
        print(f'{self!r}: {self.imp.do()}')

class ExtendedAbstraction(Abstraction):
    def operation(self):
        print(f'{self!r}: {self.imp.do()}')

class Implementation(ABC):
    def do(self)->str:
        pass

class ConcreteImplementationA(Implementation):
    def do(self)->str:
        return f'{self!r} implemented on platformA'

class ConcreteImplementationB(Implementation):
    def do(self)->str:
        return f'{self!r} implemented on platformB'

def client_code()->None:
    a1 = Abstraction(ConcreteImplementationA())
    a2 = ExtendedAbstraction(ConcreteImplementationB())
    a1.operation()
    a2.operation()

if __name__ == '__main__':
    client_code()
