"#" 
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
    def builder(self, val:IBuilder) -> None:
        self._builder = val

    def make_min_viable_product(self) -> None:
        self._builder.produce_part_a()

    def make_max_viable_product(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class Product:
    def __init__(self) -> None:
        self._parts:List[Any] = []

    def add(self, part:Any) -> None:
        self._parts.append(part)

    def list_part(self) -> str:
        return f'part list: {", ".join(map(str, self._parts))}'

class Builder(IBuilder):
    def __init__(self, p:Product) -> None:
        self._p = p
    
    def reset(self) -> None:
        self._p = Product()

    @property
    def product(self) -> Product:
        p = self._p
        self.reset()
        return p

    @product.setter
    def product(self, val:Product) -> None:
        self._p = val

    def produce_part_a(self) -> None:
        return self._p.add('partA1')

    def produce_part_b(self) -> None:
        return self._p.add('partB1')

    def produce_part_c(self) -> None:
        return self._p.add('partC1')
    
