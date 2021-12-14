# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Director:
    pass

class IBuilder(ABC):
    @abstractmethod
    def reset(self)->None: pass

    @abstractmethod
    @property
    def product(self)->Product:
        pass

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
    def product(self)->Product:
        return self._product
    
    @product.setter
    def product(self, val:Product) -> None:
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

    def __str__(self) -> str:
        return f'Product parts: {", ".join(map(str, self._parts), end="")}'