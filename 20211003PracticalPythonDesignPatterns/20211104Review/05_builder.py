# housing

from abc import ABC, abstractmethod

class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self)->None: pass

    @abstractmethod
    def produce_part_a(self)->None: pass

    @abstractmethod
    def produce_part_b(self)->None: pass

    @abstractmethod
    def produce_part_c(self)->None: pass

class ConcreteBuilder(IBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self) -> None:
        return self._product

    def reset(self)->None:
        self._product = Product()

    def produce_part_a(self) -> None:
        self._product.add('partA1')

    def produce_part_b(self) -> None:
        self._product.add('partB1')

    def produce_part_c(self) -> None:
        self._product.add('partC1')

class Product:
    def __init__(self)->None:
        self._parts = []
    
    def add(self, part:str)->None:
        self._parts.append(part)

    def __str__(self)->str:
        return 'Product parts list: {0}'.format(', '.join(self._parts), end='')

class Director:
    def __init__(self) -> None:
        self._builder:ConcreteBuilder = None

    @property
    def builder(self)->ConcreteBuilder:
        return self._builder

    @builder.setter
    def builder(self, val:ConcreteBuilder)->None:
        self._builder = val

    def make_min_viable_product(self)->None:
        self.builder.produce_part_a()

    def make_max_viable_product(self)->None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

def client_code()->None:
    b = ConcreteBuilder()
    d = Director()
    d.builder = b
    d.make_min_viable_product()
    print(d.builder.product)
    d.make_max_viable_product()
    print(d.builder.product)

if __name__ == '__main__':
    client_code()