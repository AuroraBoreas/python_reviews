# director - builder - house
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any, List


class Director:
    def __init__(self) -> None:
        self._builder:IBuilder = None

    @property
    def builder(self)->IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder)->None:
        self._builder = val

    def make_min_viable_product(self)->None:
        self._builder.produce_part_a()

    def make_max_viable_product(self)->None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

class IBuilder:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def product(self)->Product:
        pass

    @product.setter
    def product(self, val:Product)->None:
        pass

    @abstractmethod
    def reset(self)->None:
        pass

    @abstractmethod
    def produce_part_a(self)->None:
        pass

    @abstractmethod
    def produce_part_b(self)->None:
        pass

    @abstractmethod
    def produce_part_c(self)->None:
        pass

class ConcreteBuilder1(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        p = self._product
        self.reset()
        return p

    @product.setter
    def product(self, val:product) -> Product:
        self._product = val

    def produce_part_a(self) -> None:
        self._product.add('partA1')

    def produce_part_b(self) -> None:
        self._product.add('partB1')

    def produce_part_c(self) -> None:
        self._product.add('partC1')

class Product:
    def __init__(self) -> None:
        self._parts:List[Any] = []

    def add(self, part:str)->None:
        self._parts.append(part)
    
    def __str__(self)->str:
        return 'Product part list: {}'.format(', '.join(self._parts), end='')

def client_code()->None:
    d = Director()
    b = ConcreteBuilder1()
    d.builder = b

    d.make_max_viable_product()
    print(b.product)

    d.make_min_viable_product()
    print(b.product)

if __name__ == '__main__':
    client_code()