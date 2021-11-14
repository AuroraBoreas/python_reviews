# abcfactory
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def produce_product_a(self)->AbstractProductA:
        pass

    @abstractmethod
    def produce_product_b(self)->AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def produce_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def produce_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class AbstractProduct(ABC):
    pass

class AbstractProductA(AbstractProduct):
    @abstractmethod
    def do_this(self) -> str:
        pass

class AbstractProductB(AbstractProduct):
    @abstractmethod
    def do_that(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ConcreteProductA2(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ConcreteProductB1(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ConcreteProdutB2(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

def client_code(f:ConcreteFactory1)->None:
    pa = f.produce_product_a()
    pb = f.produce_product_b()
    print(pa.do_this())
    print(f'{pb.do_that()} collaborates with {pa.do_this()}')

if __name__ == '__main__':
    client_code(ConcreteFactory1())