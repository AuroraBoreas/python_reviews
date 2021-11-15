# bridge

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation:Implementation)->None:
        self.implementation = implementation

    def operation(self)->str:
        return (f'Abstraction: Base operation with:\n'
                f'{self.implementation.operation_implementation()}')


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f'ExtendedAbstraction: Extended operation with"\n'
                f'{self.implementation.operation_implementation()}')

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self)->str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return 'ConcreteImplementation: Here is the result on the platform A.'

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return 'ConcreteImplementation: Here is the result on the platform B.'

def client_code(abstraction:Abstraction)->None:
    print(abstraction.operation(), end='')


if __name__ == '__main__':
    imp = ConcreteImplementationA()
    abt = Abstraction(imp)
    client_code(abt)

    print('\n')

    imp = ConcreteImplementationB()
    abt = ExtendedAbstraction(imp)
    client_code(abt)