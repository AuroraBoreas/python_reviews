# 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def make_product_a(self) -> AbsProductA:
        raise NotImplementedError()
    @abstractmethod
    def make_product_b(self) -> AbsProductB:
        raise NotImplementedError()

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
        raise NotImplementedError()

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_that(self) -> str:
        raise NotImplementedError()

class ProductA1(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do this'

class ProductA2(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do this'

class ProductB1(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do that'

class ProductB2(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do that'

def client_code(absf:AbsFactory) -> None:
    print(f'{absf.make_product_a().do_this() }')
    print(f'{absf.make_product_b().do_that() }')

def main() -> None:
    for f in [Factory1(), Factory2()]:
        client_code(f)

if __name__ == '__main__':
    main()
