from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def product(self)->None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self)->None: self._product.add('PartA1')
    def produce_part_b(self)->None: self._product.add('PartB1')
    def produce_part_c(self)->None: self._product.add('PartC1')

class Product:
    def __init__(self)->None:
        self.parts = []
    def add(self, part:Any)->None: self.parts.append(part)
    def tostring(self)->str: return 'Product parts: {}'.format(', '.join(self.parts), end='')

class Diretor:
    def __init__(self): self._builder = None

    @property
    def builder(self)->Builder:
        return self._builder

    @builder.setter
    def builder(self, b:Builder)->None: self._builder = b

    def build_minimal_viable_product(self):
        self._builder.produce_part_a()

    def build_full_featured_product(self):
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()


if __name__ == '__main__':
    d = Diretor()
    b = ConcreteBuilder()
    d.builder = b
    d.build_full_featured_product()
    print(b.product.tostring())