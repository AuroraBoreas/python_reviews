"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Director:
    def __init__(self, builder:IBuilder) -> None:
        self._builder = builder
    
    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder) -> None:
        self._builder = val

    def make_min_feature_product(self) -> None:
        self._builder.produce_part_a()

    def make_max_feature_product(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

class IBuilder(ABC):
    @abstractmethod
    @property
    def product(self) -> Product:
        pass

    @abstractmethod
    def reset(self) -> None: pass

    @abstractmethod
    def produce_part_a(self) -> None: raise NotImplementedError()

    @abstractmethod
    def produce_part_b(self) -> None: raise NotImplementedError()

    @abstractmethod
    def produce_part_c(self) -> None: raise NotImplementedError()

class Builder(IBuilder):
    def __init__(self, product:Product) -> None:
        self._product = product
    
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
        self._product.add('partA')
    
    def produce_part_b(self) -> None:
        self._product.add('partB')
    
    def produce_part_c(self) -> None:
        self._product.add('partC')

class Product:
    def __init__(self) -> None:
        self._parts:List[Any] = []
    
    def add(self, part:str) -> None:
        self._parts.append(part)

    def __str__(self) -> str:
        return f'{self.__class__} part lits: {self._parts}'