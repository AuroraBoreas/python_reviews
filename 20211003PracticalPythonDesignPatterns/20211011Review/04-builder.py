from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
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
    def __init__(self)->None: self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self)->Product:
        p = self._product
        self.reset()
        return p

    def produce_part_a(self): self._product.add('partA1')
    def produce_part_b(self): self._product.add('partB1')
    def produce_part_c(self): self._product.add('partC1')
    
class Product:
    def __init__(self): self.parts = []
    def add(self, part:Any): self.parts.append(part)
    def tostring(self): return 'Product parts: {}'.format(', '.join(self.parts), end='')

class Director:
    def __init__(self): self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder:Builder): self._builder = builder

    def build_minimal_viable_product(self): self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == '__main__':
    d = Director()
    b = ConcreteBuilder()
    d.builder = b

    d.build_minimal_viable_product()
    print(b.product.tostring())

    d.build_full_featured_product()
    print(b.product.tostring())