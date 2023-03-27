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
    def product_part_a(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def product_part_b(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def product_part_c(self) -> None:
        raise NotImplementedError

class Builder1(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._p = Product()
    
    @property
    def product(self) -> Product:
        p = self._p
        self.reset()
        return p
    
    @product.setter
    def product(self, val: Product) -> None:
        self._p = val

    def product_part_a(self) -> None:
        self._p.add('partA')

    def product_part_b(self) -> None:
        self._p.add('partB')

    def product_part_c(self) -> None:
        self._p.add('partC')

class Director:
    def __init__(self, b: IBuilder) -> None:
        self._builder = b

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val: IBuilder) -> None:
        self._builder = val

    def make_min_feature_product(self) -> None:
        self.builder.product_part_a()
    
    def make_max_feature_product(self) -> None:
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()

class Product:
    def __init__(self) -> None:
        self._parts: list[Any] = list()

    def add(self, part: Any) -> None:
        self._parts.append(part)

    def remove(self, part: Any) -> None:
        self._parts.remove(part)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}, part list: {", ".join(self._parts)}'

def client_code() -> None:
    b = Builder1()
    d = Director(b)
    d.make_min_feature_product()
    print(d.builder.product)
    d.builder = Builder1()
    d.make_max_feature_product()
    print(d.builder.product)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()