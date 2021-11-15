# abc factory: a factory produces a factory that return objects 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbcFactory(ABC):
    @abstractmethod
    def produce_product_a(self)->AbcProductA:
        pass

    @abstractmethod
    def produce_product_b(self)->AbcProductB:
        pass

class ConcreteFactory1(AbcFactory):
    def produce_product_a(self) -> AbcProductA:
        return ConcreteProductA1()

    def produce_product_b(self) -> AbcProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbcFactory):
    def produce_product_a(self) -> AbcProductA:
        return ConcreteProductA2()

    def produce_product_b(self) -> AbcProductB:
        return ConcreteProductB2()

class AbcProduct:
    __metaclass__ = ABCMeta

    pass

class AbcProductA(AbcProduct):
    @abstractmethod
    def do_this(self)->None:
        pass

class AbcProductB(AbcProduct):
    @abstractmethod
    def do_that(self)->None:
        pass

class ConcreteProductA1(AbcProductA):
    def do_this(self) -> None:
        print(f'{self.__class__}: do_this..')

class ConcreteProductA2(AbcProductA):
    def do_this(self) -> None:
        print(f'{self.__class__}: do_this..')

class ConcreteProductB1(AbcProductB):
    def do_that(self) -> None:
        print(f'{self.__class__}: do_this..')

class ConcreteProductB2(AbcProductB):
    def do_that(self) -> None:
        print(f'{self.__class__}: do_this..')

def client_code()->None:
    f = ConcreteFactory1()
    pa = f.produce_product_a()
    pb = ConcreteFactory2().produce_product_b()

    print(f'{pa.do_this()}')
    print(f'{pb.do_that()} collaborates with {pa.do_this()}')
