# 
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AbstractFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_product_a(self)->AbstractProductA: pass

    @abstractmethod
    def make_product_b(self)->AbstractProductB: pass

class Factory(AbstractFactory):
    def make_product_a(self) -> AbstractProductA:
        return ProductA1()

    def make_product_b(self) -> AbstractProductB:
        return ProductB1()

class AbstractProduct(metaclass=ABCMeta):
    pass

class AbstractProductA(AbstractProduct):
    @abstractmethod
    def do_this(self)->str: pass

class AbstractProductB(AbstractProduct):
    @abstractmethod
    def do_that(self)->str: pass

class ProductA1(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductA2(AbstractProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductB1(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ProductB2(AbstractProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'