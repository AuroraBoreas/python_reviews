# super factory builds factory
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def make_product_a(self) -> AbsProductA:
        raise NotImplementedError()
    @abstractmethod
    def make_product_b(self) -> AbsProductB:
        raise NotImplementedError()

class AbsProduct:
    __metaclass__ = ABCMeta

class AbsProductA(AbsProduct):
    @abstractmethod
    def do_this(self) -> str: pass
    @abstractmethod
    def do_that(self) -> str: pass

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_this(self) -> str: pass
    @abstractmethod
    def do_that(self) -> str: pass

class ProductA1(AbsProductA):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductA2(AbsProductA):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductB1(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

    def do_this(self) -> str:
        return f'{self.__class__} do_this'

class ProductB2(AbsProductB):
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

    def do_this(self) -> str:
        return f'{self.__class__} do_this'