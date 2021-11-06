# abstract factory -> factory

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self)->AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self)->AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self)->str:
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'the result of the product A1'

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'the result of the product A1'

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self)->str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator:AbstractProductA)->None:
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'the result of the product B1'

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        rv = collaborator.useful_function_a()
        return f'the result of the B1 collaborating with the ({rv})'

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'the result of the product B2'
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        rv = collaborator.useful_function_a()
        return f'the result of the B2 collaborating with the ({rv})'

def client_code(factory:AbstractFactory)->None:
    pa = factory.create_product_a()
    pb = factory.create_product_b()

    print(f'{pb.useful_function_b()}')
    print(f'{pb.another_useful_function_b(pa)}')

if __name__ == '__main__':
    print('client: i want factory type a:')
    client_code(ConcreteFactory1())

    print('client: i want factory tpye b:')
    client_code(ConcreteFactory2())
