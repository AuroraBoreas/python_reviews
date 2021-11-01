# building a house

from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):
    @property
    @abstractmethod
    def product(self): pass

    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def produce_part_a(self): pass

    @abstractmethod
    def produce_part_b(self): pass

    @abstractmethod
    def produce_part_c(self): pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()
    
    @property
    def product(self):
        p = self._product
        self.reset()
        return p

    def produce_part_a(self):
        self._product.add('partA1')

    def produce_part_b(self):
        self._product.add('PartB1')

    def produce_part_c(self):
        self._product.add('PartC1')

class Product:
    def __init__(self)->None:
        self.parts = []

    def add(self, part:str)->None:
        self.parts.append(part)

    def toString(self)->None:
        print(f'Product: {", ".join(self.parts)}', end='')

class Director:
    def __init__(self)->None:
        self._builder = None

    @property
    def builder(self)->Builder:
        return self._builder

    @builder.setter
    def builder(self,builder:Builder)->None:
        self._builder = builder

    def build_min_viable_product(self):
        self._builder.produce_part_a()

    def build_max_viable_product(self):
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

def client_code():
    d = Director()
    b = ConcreteBuilder()
    d.builder = b

    d.build_min_viable_product()
    b.product.toString()
    print()
    d.build_max_viable_product()
    b.product.toString()

if __name__ == '__main__':
    client_code()