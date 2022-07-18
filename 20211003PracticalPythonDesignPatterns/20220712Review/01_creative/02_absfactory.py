"#" 

from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AbsFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_product_a(self) -> AbsProductA: pass

    @abstractmethod
    def make_product_b(self) -> AbsProductB: pass

class Factory1(AbsFactory):
    def make_product_a(self) -> AbsProductA:
        return ProductA1()

    def make_product_b(self) -> AbsProductB:
        return ProductB2()

class AbsProduct:
    __metaclass__ = ABCMeta

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
        return f'{self.__class__} do_this'

class ProductA2(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductB1(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ProductB2(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'
