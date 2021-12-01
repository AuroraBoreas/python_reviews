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

    @property
    def builder(self, val:IBuilder)->None:
        self._builder = val

    def make_min_viable_product(self)->None:
        self._builder.product_part_a()

    def make_max_viable_product(self)->None:
        self._builder.product_part_a()
        self._builder.product_part_b()
        self._builder.product_part_c()

class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self)->Product:
        pass

    @property
    def product(self, val:Product)->None:
        pass

    @abstractmethod
    def reset(self)->None:
        pass

    @abstractmethod
    def product_part_a(self)->None: pass

    @abstractmethod
    def product_part_b(self)->None: pass

    @abstractmethod
    def product_part_c(self)->None: pass

class Builder(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    @abstractmethod
    def product(self)->Product:
        p = self._product
        self._product = Product()
        return p

    @property
    def product(self, val:Product)->None:
        self._product = val

    def product_part_a(self) -> None:
        self._product.add('partA1')

    def product_part_b(self) -> None:
        self._product.add('partB1')

    def product_part_c(self) -> None:
        self._product.add('partC1')

class Product:
    def __init__(self) -> None:
        self._assets:List[Any] = []

    def add(self, item:Any)->None:
        self._assets.append(item)

    def __str__(self) -> str:
        return f'Product parts: {"+".join(self._assets)}'