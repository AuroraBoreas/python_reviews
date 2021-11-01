# housing
from __future__ import annotations
from abc import abstractmethod

class Director:
    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self)->Builder:
        return self._builder

    @builder.setter
    def builder(self, val:Builder)->None:
        self._builder = val

    def build_min_viable_product(self)->None:
        self.builder.produce_part_a()

    def build_max_viable_product(self)->None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class Builder:
    @property
    @abstractmethod
    def product(self)->None: pass

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

class ConcreteBuilder(Builder):
    def __init__(self)->None:
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self)->Product:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add('partA1')

    def produce_part_b(self) -> None:
        self._product.add('partB1')

    def produce_part_c(self) -> None:
        self._product.add('partC1')

class Product:
    def __init__(self) -> None:
        self._parts = []

    def add(self, part:str)->None:
        self._parts.append(part)

    def __str__(self)->str:
        return 'Product parts: {}'.format(", ".join(self._parts), end='')

if __name__ == '__main__':
    d = Director()
    b = ConcreteBuilder()
    d.builder = b
    d.build_min_viable_product()
    print(d.builder.product)
    d.build_max_viable_product()
    print(d.builder.product)