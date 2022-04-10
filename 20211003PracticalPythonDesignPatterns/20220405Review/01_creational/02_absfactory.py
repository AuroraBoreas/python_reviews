"abstract factory: a factory returns a sub-factory;" 
from __future__ import annotations
from abc import ABC


class AbstractFactory(ABC):
    def produce_productA(self)->AbstractProductA:
        raise NotImplementedError()
    def produce_productB(self)->AbstractProductB:
        raise NotImplementedError()

class Factory1(AbstractFactory):
    def produce_productA(self) -> AbstractProductA:
        return ProductA1()
    def produce_productB(self) -> AbstractProductB:
        return ProductB1()

class Factory2(AbstractFactory):
    def produce_productA(self) -> AbstractProductA:
        return ProductA2()
    def produce_productB(self) -> AbstractProductB:
        return ProductB2()

class AbstractProduct(ABC):
    pass

class AbstractProductA(AbstractProduct):
    def do_this(self)->str:
        raise NotImplementedError()

class AbstractProductB(AbstractProduct):
    def do_that(self)->str:
        raise NotImplementedError()

class ProductA1(AbstractProductA):
    def do_this(self) -> str:
        return f"{self!r} do_this.."

class ProductA2(AbstractProductA):
    def do_this(self) -> str:
        return f"{self!r} do_this.."

class ProductB1(AbstractProductB):
    def do_that(self) -> str:
        return f"{self!r} do_that.."

class ProductB2(AbstractProductB):
    def do_that(self) -> str:
        return f"{self!r} do_that.."