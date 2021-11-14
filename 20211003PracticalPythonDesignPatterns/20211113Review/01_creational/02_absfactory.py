# abstract factory makes factories 
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def product_product_a(self)->AbstractProductA:
        pass

    @abstractmethod
    def product_product_b(self)->AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def product_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def product_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

class AbstractProductA:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_this(self) -> None:
        pass

class ConcreteProductA1(AbstractProductA):
    def do_this(self) -> None:
        print(f'{self.__class__} do this')

class ConcreteProductA2(AbstractProductA):
    def do_this(self) -> None:
        print(f'{self.__class__} do this')

class AbstractProductB:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_that(self)->None:
        pass

class ConcreteProductB1(AbstractProductB):
    def do_that(self) -> None:
        print(f'{self.__class__} do that')

class ConcreteProductB2(AbstractProductB):
    def do_that(self) -> None:
        print(f'{self.__class__} do that')

def client_code(f: ConcreteFactory1)->None:
    pa = f.product_product_a()
    pb = f.product_product_b()

    pa.do_this()
    pb.do_that()

if __name__ == '__main__':
    client_code(ConcreteFactory1())