"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
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
    def do_this(self) -> str: pass
    
    @abstractmethod
    def do_that(self) -> str: pass

class AbsProductB(AbsProduct):
    @abstractmethod
    def do_that(self) -> str: pass

    @abstractmethod
    def do_that(self) -> str: pass

class ProductA1(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
        
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ProductA2(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'
        
    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ProductB1(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

    def do_that(self) -> str:
        return f'{self.__class__} do_that'

class ProductB2(AbsProductA):
    def do_this(self) -> str:
        return f'{self.__class__} do_this'

    def do_that(self) -> str:
        return f'{self.__class__} do_that'
