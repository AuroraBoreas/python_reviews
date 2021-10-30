# build house

from __future__ import annotations
from _typeshed import NoneType
from abc import ABCMeta, abstractmethod
from typing import Any

class Builder(metaclass=ABCMeta):
    @property
    @abstractmethod
    def product(self) -> Product: pass

    @abstractmethod
    def reset(self) -> None: pass

    @abstractmethod
    def produce_part_a(self) -> None: pass

    @abstractmethod
    def produce_part_b(self) -> None: pass

    @abstractmethod
    def produce_part_c(self) -> None: pass

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    def produce_part_a(self) -> None:
        self._product.add('partA')

    def produce_part_b(self) -> None:
        self._product.add('partB')

    def produce_part_c(self) -> None:
        self._product.add('partC')

class Product:
    def __init__(self) -> None:
        self.parts = []
    
    def add(self, part:Any) -> None: self.parts.append(part)

    def toString(self) -> None: print(f'Product parts: {", ".join(self.parts)}', end='')

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder: return self._builder

    @builder.setter
    def builder(self, builder:Builder) -> None: self._builder = builder

    def build_min_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_max_viable_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()