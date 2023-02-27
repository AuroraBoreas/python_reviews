# 
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AbsFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_product_a(self) -> AbsProductA: raise NotImplementedError
    @abstractmethod
    def make_product_b(self) -> AbsProductB: raise NotImplementedError

class Factory1(AbsFactory):
    def make_product_a(self) -> AbsProductA:
        return ProductA1()
    def make_product_b(self) -> AbsProductB:
        return ProductB1()

class Factory2(AbsFactory):
    def make_product_a(self) -> AbsProductA:
        return ProductA2()
    def make_product_b(self) -> AbsProductB:
        return ProductB2()
    
class AbsProduct:
    __metaclass__ = ABCMeta
    ...

class AbsProductA(AbsProduct):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_that(self) -> str:
        raise NotImplementedError
    
class ProductA1(AbsProductA):
    def do_this(self) -> str:
        return f"{self.__class__} do_this"
    
class ProductA2(AbsProductA):
    def do_this(self) -> str:
        return f"{self.__class__} do_this"
    
class ProductB1(AbsProductB):
    def do_that(self) -> str:
        return f"{self.__class__} do_that"
    
class ProductB2(AbsProductB):
    def do_that(self) -> str:
        return f"{self.__class__} do_that"
    
def client_code(f: AbsFactory) -> None:
    p1 = f.make_product_a()
    p2 = f.make_product_b()
    print(p1.do_this())
    print(p2.do_that())

def main() -> None:
    for f in [
        Factory1(),
        Factory2(),
    ]:
        client_code(f)

if __name__ == '__main__':
    main()