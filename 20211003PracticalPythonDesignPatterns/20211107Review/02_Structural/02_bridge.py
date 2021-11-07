# bridge: abstraction - implementation
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, imp:Implementation) -> None:
        self.imp = imp

    def operation(self)->str:
        return (f'{self.__class__}: Base operation with: \n'
                f'{self.imp.operation_implementation()}')

class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f'{self.__class__}: extended operation with: \n'
                f'{self.imp.operation_implementation()}')

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self)->str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return f'{self.__class__}: here is the result on the platform A'

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return f'{self.__class__}: here is the result on the platform B'

def client_code(abstraction:Abstraction)->None:
    print(abstraction.operation(), end='')

if __name__ == '__main__':
    client_code(Abstraction(ConcreteImplementationB()))
    print('\n')
    client_code(ExtendedAbstraction(ConcreteImplementationA()))