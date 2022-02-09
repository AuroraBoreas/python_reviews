# 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def make_product_a(self)->AbstractProductA:
        pass

    @abstractmethod
    def make_product_b(self)->AbstractProductB:
        pass

class Factory1(AbstractFactory):
    def make_product_a(self) -> AbstractProductA:
        return ProductA1()

    def make_product_b(self) -> AbstractProductB:
        return ProductB1()

class Factory2(AbstractFactory):
    def make_product_a(self) -> AbstractProductA:
        return ProductA2()

    def make_product_b(self) -> AbstractProductB:
        return ProductB2()

class AbstractProduct:
    __metaclass__ = ABCMeta

class AbstractProductA(AbstractProduct):
    @abstractmethod
    def do_this(self)->str: pass

class ProductA1(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'

class ProductA2(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} : do_this'

class AbstractProductB(AbstractProduct):
    @abstractmethod
    def do_that(self)->str: pass

class ProductB1(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} : do_that'

class ProductB2(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} : do_that'