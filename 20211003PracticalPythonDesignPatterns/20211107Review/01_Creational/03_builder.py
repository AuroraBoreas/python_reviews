# director - builder - product
from __future__ import annotations
from abc import ABC, abstractmethod


class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self)->None: pass

    @abstractmethod
    def product_part_a(self)->None: pass

    @abstractmethod
    def product_part_b(self)->None: pass

    @abstractmethod
    def product_part_c(self)->None: pass

class ConcreteBuilder(IBuilder):
    def __init__(self) -> None:
        self.reset()

    @property
    def product(self) -> Product:
        p = self._product
        self.reset()
        return p

    @product.setter
    def product(self, val:Product)->None:
        self._product = val

    def reset(self)->None:
        self._product = Product()

    def product_part_a(self) -> None:
        self._product.add('partA1')

    def product_part_b(self) -> None:
        self._product.add('partB1')

    def product_part_c(self) -> None:
        self._product.add('partC1')

class Product:
    def __init__(self) -> None:
        self._parts = []

    def add(self, part:str)->None:
        self._parts.append(part)

    def __str__(self)->str:
        return '{}'.format(', '.join(self._parts), end='')


class Diretor:
    def __init__(self):
        self._builder:IBuilder = None
    
    @property
    def builder(self)->IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder)->None:
        self._builder = val

    def make_min_viable_product(self)->None:
        self._builder.product_part_a()

    def make_max_viable_product(self)->None:
        self._builder.product_part_a()
        self._builder.product_part_b()
        self._builder.product_part_c()

def client_code()->None:
    d = Diretor()
    b = ConcreteBuilder()
    d.builder = b
    d.make_min_viable_product()
    print(d.builder.product)

    d.make_max_viable_product()
    print(d.builder.product)

if __name__ == '__main__':
    client_code()