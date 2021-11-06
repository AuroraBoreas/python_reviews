# director - builder - houses
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class IBuilder:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def product(self)->None:
        pass

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

    ...

class ConcreteBuilder(IBuilder):
    def __init__(self)->None:
        self.reset()

    def reset(self)->None:
        self._product = Product()
        
    @property
    def product(self)->Product:
        p = self._product
        self.reset()
        return p

    def produce_part_a(self) -> None:
        return self._product.add('partA')

    def produce_part_b(self) -> None:
        return self._product.add('partB')

    def produce_part_c(self) -> None:
        return self._product.add('partC')

class Product:
    def __init__(self) -> None:
        self._parts = []

    def add(self, part:str)->None:
        self._parts.append(part)

    def __str__(self)->str:
        return 'Product parts list: {}'.format(', '.join(self._parts), end='')

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

def client_code()->None:
    d = Director()
    b = ConcreteBuilder()
    d.builder = b
    d.make_max_viable_product()
    print(d.builder.product)

    d.make_min_viable_product()
    print(d.builder.product)

if __name__ == '__main__':
    client_code()