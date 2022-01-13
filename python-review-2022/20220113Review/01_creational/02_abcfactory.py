# 
from __future__ import annotations
from abc import ABC, abstractmethod


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

class AbstractProduct(ABC):
    pass

class AbstractProductA(AbstractProduct):
    @abstractmethod
    def operation(self)->str: raise NotImplementedError()

class AbstractProductB(AbstractProduct):
    @abstractmethod
    def operation(self)->str: raise NotImplementedError()

class ProductA1(AbstractProductA):
    def operation(self) -> str:
        return f'{self.__class__} : operation'

class ProductA2(AbstractProductA):
    def operation(self) -> str:
        return f'{self.__class__} : operation'

class ProductB1(AbstractProductB):
    def operation(self) -> str:
        return f'{self.__class__} : operation'

class ProductB2(AbstractProductB):
    def operation(self) -> str:
        return f'{self.__class__} : operation'