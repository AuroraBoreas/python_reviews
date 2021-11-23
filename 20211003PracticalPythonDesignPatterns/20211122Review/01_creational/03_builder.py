# 
from __future__ import annotations
from abc import ABC, abstractmethod
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

class IBuilder(ABC):
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

class Builder1(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def builder(self)->IBuilder:
        p = self._product
        self.reset()
        return p

    @builder.setter
    def builder(self, val:Product)->None:
        self._product = val
    
    def produce_part_a(self) -> None:
        self._product.add('partA1')

    def produce_part_b(self) -> None:
        self._product.add('partB1')

    def produce_part_c(self) -> None:
        self._product.add('partC1')
        
class Product:
    def __init__(self) -> None:
        self._assets:List[Any] = []

    def __str__(self) -> str:
        return '{}'.format(', '.join(self._assets), end='')

    def add(self, part:str)->None:
        self._assets.append(part)