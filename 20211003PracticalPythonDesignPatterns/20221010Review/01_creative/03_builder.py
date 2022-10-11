# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Director:
    def __init__(self) -> None:
        self._builder:IBuilder = None

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, b:IBuilder) -> None:
        self._builder = b

    def make_min_feature_product(self) -> None:
        self._builder.product_part_a()

    def make_max_feature_product(self) -> None:
        self._builder.product_part_a()
        self._builder.product_part_b()
        self._builder.product_part_c()

class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def product(self) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def product_part_a(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def product_part_b(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def product_part_c(self) -> None:
        raise NotImplementedError()

class Builder(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        p:Product = self._product
        self.reset()
        return p
    
    @product.setter
    def product(self, p:Product) -> None:
        self._product = p

    def product_part_a(self) -> None:
        self._product.add('partA')

    def product_part_b(self) -> None:
        self._product.add('partB')

    def product_part_c(self) -> None:
        self._product.add('partC')

class Product:
    def __init__(self) -> None:
        self._parts:List[Any] = []

    def add(self, part:Any) -> None:
        self._parts.append(part)

    def __str__(self) -> str:
        return f'part list: {self._parts}'