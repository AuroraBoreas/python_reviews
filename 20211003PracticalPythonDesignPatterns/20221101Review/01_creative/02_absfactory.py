"#" 
from __future__ import annotations
from abc import ABC, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def make_product_a(self) -> AbsProductA:
        raise NotImplementedError()
    @abstractmethod
    def make_product_b(self) -> AbsProductB:
        raise NotImplementedError()

class AbsProduct(ABC):
    pass

class AbsProductA(AbsProduct):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError()
    @abstractmethod
    def do_that(self) -> str:
        raise NotImplementedError()

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError()
    @abstractmethod
    def do_that(self) -> str:
        raise NotImplementedError()

class ProductA1(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
    def do_that(self) -> str:
        return f'{self.__class__} do_this'

class ProductA2(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
    def do_that(self) -> str:
        return f'{self.__class__} do_this'

class ProductB1(AbsProductB):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
    def do_that(self) -> str:
        return f'{self.__class__} do_this'

class ProductB2(AbsProductB):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
    def do_that(self) -> str:
        return f'{self.__class__} do_this'

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

def client_code(f:AbsFactory) -> None:
    p1 = f.make_product_a()
    p2 = f.make_product_b()
    print(p1.do_this())
    print(p2.do_that())