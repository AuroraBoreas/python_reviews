from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod

class AbsFactory(ABC):
    @abstractmethod
    def make_productA(self) -> AbsProductA:
        raise NotImplementedError
    @abstractmethod
    def make_productB(self) -> AbsProductB:
        raise NotImplementedError

class Factory1(AbsFactory):
    def make_productA(self) -> AbsProductA:
        return ProductA1()
    def make_productB(self) -> AbsProductB:
        return ProductB1()

class Factory2(AbsFactory):
    def make_productA(self) -> AbsProductA:
        return ProductA2()
    def make_productB(self) -> AbsProductB:
        return ProductB2()

class Factory3(AbsFactory):
    def make_productA(self) -> AbsProductA:
        return ProductA1()
    def make_productB(self) -> AbsProductB:
        return ProductB2()

class AbsProduct:
    __metaclass__ = ABCMeta

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
    a: AbsProductA = f.make_productA()
    b: AbsProductB = f.make_productB()
    print(a.do_this())
    print(b.do_that())

def main() -> None:
    for factory in [
        Factory1(),
        Factory2(),
        Factory3(),
    ]:
        client_code(factory)

if __name__ == '__main__':
    main()
