"#" 

from __future__ import annotations
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
from abc import ABC, abstractmethod
from typing import Any

class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def part(self) -> Part:
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

class Director:
    def __init__(self, b: IBuilder) -> None:
        self._b = b

    @property
    def builder(self) -> IBuilder:
        return self._b

    @builder.setter
    def builder(self, val: IBuilder) -> None:
        self._b = val

    def make_min_feature_product(self) -> None:
        self.builder.product_part_a()

    def make_max_feature_product(self) -> None:
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()

class Builder1(IBuilder):
    def __init__(self, p: Part) -> None:
        self._p = p

    def reset(self) -> None:
        self._p = Part()
    
    @property
    def part(self) -> Part:
        p: Part = self._p
        self.reset()
        return p

    @part.setter
    def part(self, val: Part) -> None:
        self._p = val

    def product_part_a(self) -> None:
        self._p.add('partA')

    def product_part_b(self) -> None:
        self._p.add('partB')

    def product_part_c(self) -> None:
        self._p.add('partC')

class Part:
    def __init__(self) -> None:
        self._parts: list[Any] = list()
    
    def add(self, item: Any) -> None:
        self._parts.append(item)

    def __str__(self) -> str:
        return f"part list: {self._parts}"

def client_code(d: Director) -> None:
    d.make_min_feature_product()
    logging.info(d.builder.part)
    d.make_max_feature_product()
    logging.info(d.builder.part)

def main() -> None:
    d: Director = Director(Builder1(Part()))
    client_code(d)
    d.builder.reset()
    client_code(d)

if __name__ == '__main__':
    main()
