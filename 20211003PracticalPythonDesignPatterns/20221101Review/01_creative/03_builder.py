"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()
    @abstractmethod
    @property
    def Product(self) -> Product:
        raise NotImplementedError()
    @abstractmethod
    def produce_part_a(self) -> None:
        raise NotImplementedError()
    @abstractmethod
    def produce_part_b(self) -> None:
        raise NotImplementedError()
    @abstractmethod
    def produce_part_c(self) -> None:
        raise NotImplementedError()

class Builder1(IBuilder):
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
    def product(self, val:Product) -> None:
        self._product = val
        
    def produce_part_a(self) -> None:
        self._product.add_part('a')
    def produce_part_b(self) -> None:
        self._product.add_part('b')
    def produce_part_c(self) -> None:
        self._product.add_part('c')

class Product:
    def __init__(self) -> None:
        self._parts:List[Any] = []
    def add(self, part:Any) -> None:
        self._parts.append(part)
    def __str__(self) -> str:
        return f'part list : {", ".join(self._parts)}'

class Director:
    def __init__(self, b:IBuilder) -> None:
        self._builder = b

    @property
    def builder(self) -> IBuilder:
        return self._builder
        
    @builder.setter
    def builder(self, val:IBuilder) -> None:
        self._builder = val

    def make_min_viable_product(self) -> None:
        self._builder.produce_part_a()

    def make_max_viable_product(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()