# housing
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    @property
    @abstractmethod
    def product(self)->None: pass

    @abstractmethod
    def reset(self)->None: pass

    @abstractmethod
    def produce_part_a(self): pass

    @abstractmethod
    def produce_part_b(self): pass

    @abstractmethod
    def produce_part_c(self): pass

class ConcreteBuilder(IBuilder):
    def __init__(self)->None:
        self.reset()

    @property
    def product(self)->Product:
        p = self._product
        self.reset()
        return p
    
    def reset(self)->None:
        self._product = Product()

    def produce_part_a(self):
        self._product.add('partA1')

    def produce_part_b(self):
        self._product.add('partB1')

    def produce_part_c(self):
        self._product.add('partC1')
    

class Product:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part:str)->None:
        self.parts.append(part)

    def __str__(self)->str:
        return 'Product list : {}'.format(', '.join(self.parts), end='')

class Director:
    def __init__(self) -> None:
        self._builder:IBuilder = None

    @property
    def builder(self)->IBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:IBuilder)->None:
        self._builder = val

    def make_min_viable_product(self)->None:
        self._builder.produce_part_a()

    def make_max_viable_product(self)->None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

def client_code():
    d = Director()
    b = ConcreteBuilder()
    d.builder = b
    d.make_min_viable_product()
    print(d.builder.product)
    d.make_max_viable_product()
    print(d.builder.product)

if __name__ == '__main__':
    client_code()