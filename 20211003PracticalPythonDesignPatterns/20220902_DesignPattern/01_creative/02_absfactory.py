"#" 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def produce_product_a(self) -> AbsProduct:
        raise NotImplementedError()
    @abstractmethod
    def produce_product_b(self) -> AbsProduct:
        raise NotImplementedError()

class ConcreteFactory1(AbsFactory):
    def produce_product_a(self) -> AbsProduct:
        return ProductA1()
    def produce_product_b(self) -> AbsProduct:
        return ProductB1()

class ConcreteFactory2(AbsFactory):
    def produce_product_a(self) -> AbsProduct:
        return ProductA2()
    def produce_product_b(self) -> AbsProduct:
        return ProductB2()

class AbsProduct:
    __meta__ = ABCMeta
    ...

class AbsProductA(AbsProduct):
    @abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError()
    
class AbsProductB(AbsProduct):
    @abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError()

class ProductA1(AbsProductA):
    def do_this(self) -> None:
        print(f'{self.__class__} do_this..')

class ProductA2(AbsProductA):
    def do_this(self) -> None:
        print(f'{self.__class__} do_this..')

class ProductB1(AbsProductB):
    def do_that(self) -> None:
        print(f'{self.__class__} do_that..')

class ProductB2(AbsProductB):
    def do_that(self) -> None:
        print(f'{self.__class__} do_that..')

def client_code(f:AbsFactory) -> None:
    pa:AbsProductA = f.produce_product_a()
    pa.do_this()
    pb:AbsProductB = f.produce_product_b()
    pb.do_that()

if __name__ == '__main__':
    f1 = ConcreteFactory1()
    f2 = ConcreteFactory2()
    absf = [f1, f2]
    for f in absf:
        client_code(f)