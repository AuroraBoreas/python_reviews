# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def product(self) -> Product:
        raise NotImplementedError
    
    @abstractmethod
    def produce_part_a(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def produce_part_b(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def produce_part_c(self) -> None:
        raise NotImplementedError

class Builder1(IBuilder):
    def __init__(self, p: Product) -> None:
        self._p = p

    def reset(self) -> None:
        self._p = Product()

    @property
    def product(self) -> Product:
        p = self._p
        self.reset()
        return p
    
    @product.setter
    def product(self, p: Product) -> None:
        self._p = p

    def produce_part_a(self) -> None:
        self.product.add('partA')

    def produce_part_b(self) -> None:
        self.product.add('partB')

    def produce_part_c(self) -> None:
        self.product.add('partC')

class Director:
    def __init__(self, b: IBuilder) -> None:
        self._builder = b

    @property
    def builder(self) -> IBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, b: IBuilder) -> None:
        self._builder = b

    def make_min_available_product(self) -> None:
        self.builder.produce_part_a()

    def make_max_available_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class Product:
    def __init__(self) -> None:
        self._parts: list[Any] = []

    def add(self, item: Any) -> None:
        self._parts.append(item)

    def __str__(self) -> str:
        return f'part list: {"m".join(map(str, self._parts))}'