# abstract factory: a factory creates abstract factories
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from types import coroutine


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_abstract_product_a(self)->AbstractProductA:
        pass
    @abstractmethod
    def make_abstract_product_b(self)->AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def make_abstract_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def make_abstract_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def make_abstract_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def make_abstract_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

class AbstractProduct:
    __metaclass__ = ABCMeta

class AbstractProductA(AbstractProduct):
    @abstractmethod
    def make_product_a(self)->str: pass

class AbstractProductB(AbstractProduct):
    @abstractmethod
    def make_product_b(self)->str: pass

    @abstractmethod
    def collaborate(self, collaborator:AbstractProductA)->str: pass

class ConcreteProductA1(AbstractProductA):
    def make_product_a(self) -> str:
        return f'the result of {self.__class__}'

class ConcreteProductA2(AbstractProductA):
    def make_product_a(self) -> str:
        return f'the result of {self.__class__}'

class ConcreteProductB1(AbstractProductB):
    def make_product_b(self) -> str:
        return f'the result of {self.__class__}'

    def collaborate(self, collaborator: AbstractProductA) -> str:
        result = collaborator.make_product_a()
        return f'the result of the {self.__class__} collaborating with the ({result})'

class ConcreteProductB2(AbstractProductB):
    def make_product_b(self) -> str:
        return f'the result of {self.__class__}'
    
    def collaborate(self, collaborator: AbstractProductA) -> str:
        result = collaborator.make_product_a()
        return f'the result of the {self.__class__} collaborating with the ({result})'

def client_code(f:AbstractFactory)->None:
    pa = f.make_abstract_product_a()
    pb = f.make_abstract_product_b()

    print(f'{pb.make_product_b()}')
    print(f'{pb.collaborate(pa)}')

if __name__ == '__main__':
    print('client: tesing client code with the first factory type1:')
    client_code(ConcreteFactory1())

    print('\nclient: tesing client code with the first factory type2:')
    client_code(ConcreteFactory2())
