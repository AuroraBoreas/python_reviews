from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any

class Product:
    def __init__(self)->None:
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def toString(self)->str:
        return 'Product parts: {}'.format(
            ', '.join(self._parts),
            end=''
        )

class Director:
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder:Builder)->None:
        self._builder = builder

    def build_minimal_viable_product(self)->Any:
        self.builder.produce_part_a()

    def build_full_fledged_product(self)->Any:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class Builder:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def product(self)->None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

class ConcreteBuilder(Builder):
    def __init__(self)->None:
        self.reset()

    def reset(self)->None:
        self._product = Product()

    @property
    def product(self) -> Product:
        p = self._product
        self.reset()
        return p

    def produce_part_a(self) -> None:
        self._product.add('PartA1')

    def produce_part_b(self) -> None:
        self._product.add('PartB1')

    def produce_part_c(self) -> None:
        self._product.add('PartC1')