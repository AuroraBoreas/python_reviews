"#" 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
from typing import Optional


class AbsFactory(ABC):
    @abstractmethod
    def produce_product_a(self) -> AbsProductA:
        raise NotImplementedError()
    @abstractmethod
    def produce_product_b(self) -> AbsProductB:
        raise NotImplementedError()

class Factory1(AbsFactory):
    def produce_product_a(self) -> AbsProductA:
        return ProductA1()
    def produce_product_b(self) -> AbsProductB:
        return ProductB1()

class Factory2(AbsFactory):
    def produce_product_a(self) -> AbsProductA:
        return ProductA2()
    def produce_product_b(self) -> AbsProductB:
        return ProductB2()

class AbsProduct:
    __metaclass__ = ABCMeta
    pass

class AbsProductA(AbsProduct):
    @abstractmethod
    def do_this(self) -> Optional[str]:
        raise NotImplementedError()

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_that(self) -> Optional[str]:
        raise NotImplementedError()

class ProductA1(AbsProductA):
    def do_this(self) -> Optional[str]:
        return f'{self.__class__} do_this'

class ProductA2(AbsProductA):
    def do_this(self) -> Optional[str]:
        return f'{self.__class__} do_this'

class ProductB1(AbsProductB):
    def do_that(self) -> Optional[str]:
        return f'{self.__class__} do_that'

class ProductB2(AbsProductB):
    def do_that(self) -> Optional[str]:
        return f'{self.__class__} do_that'

def client_code(f:AbsFactory) -> None:
    pa:AbsProductA = f.produce_product_a()
    pb:AbsProductB = f.produce_product_b()
    print(pa.do_this())
    print(pb.do_that())

def main() -> None:
    for f in [
        Factory1(),
        Factory2(),
    ]:
        client_code(f)

if __name__ == '__main__':
    main()