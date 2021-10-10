# from __future__ import annotations: Python>=3.7
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def product(self)->None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_a(self)->None: raise NotImplementedError()

    @abstractmethod
    def produce_part_b(self)->None: raise NotImplementedError()

    @abstractmethod
    def produce_part_c(self)->None: raise NotImplementedError()

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self): self._product.add('PartA1')
    def produce_part_b(self): self._product.add('PartB1')
    def produce_part_c(self): self._product.add('PartC1')

class Product1:
    def __init__(self): self.parts = []
    def add(self, part:Any): self.parts.append(part)
    def tostring(self): return 'Product parts: {}'.format(', '.join(self.parts), end='')

class Director:
    def __init__(self): self._builder = None
    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder:Builder): self._builder = builder

    def build_minimmal_viable_product(self): self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == '__main__':
    d = Director()
    b = ConcreteBuilder1()
    d.builder = b

    print("standard basic product: ")
    d.build_minimmal_viable_product()
    print(b.product.tostring())

    print()

    print("standard full featured product: ")
    d.build_full_featured_product()
    print(b.product.tostring())

    print()

    print("Custom product: ")
    b.produce_part_a()
    b.produce_part_b()
    b.produce_part_c()
    print(b.product.tostring())

