"builder: director asks buider to build various houses;" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Director:
    def __init__(self) -> None:
        self._builder:IBuilder = None

    @property
    def builder(self)->IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder)->None:
        self._builder = val
    
    def build_min_viable_product(self)->None:
        self._builder.produce_part_a()

    def build_max_viable_product(self)->None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

class IBuilder(ABC):
    @abstractmethod
    def reset(self)->None: raise NotImplementedError()

    @property
    @abstractmethod
    def product(self)->Product: pass

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

class Builder(IBuilder):
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
        return self._product.add('partA1')

    def produce_part_b(self) -> None:
        return self._product.add('partB1')

    def produce_part_c(self) -> None:
        return self._product.add('partC1')

class Product:
    def __init__(self) -> None:
        self._parts:List[str] = []
    def add(self, part:str)->None:
        self._parts.append(part)
    def __str__(self)->str:
        return f'part list: {self._parts}'