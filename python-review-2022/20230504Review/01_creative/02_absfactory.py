"Python is a protocol orientated language; every top-level function implements its dunder method;" 
from __future__ import annotations
from abc import ABC, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def make_product_a(self) -> AbsProductA:
        raise NotImplementedError
    
    @abstractmethod
    def make_product_b(self) -> AbsProductB:
        raise NotImplementedError
    
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
    
class AbsProduct(ABC):
    pass

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
        return f"{self.__class__} do_this balabala"

class ProductB1(AbsProductB):
    def do_that(self) -> str:
        return f"{self.__class__} do_that balabala"
    
class ProductB2(AbsProductB):
    def do_that(self) -> str:
        return f"{self.__class__} do_that"
    
def client_code(f: AbsFactory) -> None:
    a: AbsProduct = f.make_product_a()
    b: AbsProduct = f.make_product_b()
    print(a.do_this())
    print(b.do_that())

def main() -> None:
    for f in [
        Factory1(),
        Factory2(),
    ]:
        client_code(f)

if __name__ == '__main__':
    main()