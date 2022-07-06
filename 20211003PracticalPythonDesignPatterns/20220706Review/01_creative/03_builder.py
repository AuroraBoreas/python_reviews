# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Director:
    def __init__(self, b:IBuilder) -> None:
        self._builder = b

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder) -> None:
        self._builder = val
    
    def make_min_feature_product(self) -> None:
        self._builder.add_part_a()

    def make_max_feature_product(self) -> None:
        self._builder.add_part_a()
        self._builder.add_part_b()
        self._builder.add_part_c()

class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None: pass

    @property
    @abstractmethod
    def product(self) -> Product: pass

    @abstractmethod
    def add_part_a(self) -> None: pass

    @abstractmethod
    def add_part_b(self) -> None: pass

    @abstractmethod
    def add_part_c(self) -> None: pass

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

    def add_part_a(self) -> None:
        self._p.add('partA')

    def add_part_b(self) -> None:
        self._p.add('partB')

    def add_part_c(self) -> None:
        self._p.add('partC')

class Product:
    def __init__(self) -> None:
        self._parts:List[str] = []

    def add(self, part:str) -> None:
        self._parts.append(part)

    def list_parts(self) -> str:
        return f'part list: {", ".join(map(str, self._parts))}'

def client_code() -> None:
    p = Product()
    b = Builder(p)
    d = Director(b)
    d.builder = b
    d.make_max_feature_product()
    print(b.product.list_parts())
    d.make_min_feature_product()
    print(b.product.list_parts())

if __name__ == '__main__':
    client_code()