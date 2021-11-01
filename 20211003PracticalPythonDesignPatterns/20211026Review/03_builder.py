# builder -- director
from __future__ import annotations
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    @property
    def product(self) -> None: pass

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self.product.add('partsA1')

    def produce_part_b(self) -> None:
        self.product.add('partsB1')

    def produce_part_c(self) -> None:
        self.product.add('partsC1')

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part:str)->None:
        self.parts.append(part)

    def __str__(self)->str:
        return 'Product:' + ', '.format(self.parts, end='')

class Director:
    def __init__(self)->None:
        self._builder = None
    
    @property
    def builder(self)->Builder:
        return self._builder

    @builder.setter
    def builder(self, val:Builder)->None:
        self._builder = val

    def build_min_viable_product(self):
        self.builder.produce_part_a()

    def build_max_viable_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

