"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Director:
    def __init__(self, b:IBuilder) -> None:
        self._builder = b
    
    @property
    def builder(self) -> IBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, val:IBuilder) -> None:
        self._builder = val

    def produce_min_feature_product(self) -> None:
        self.builder.produce_part_a()

    def produce_full_fledge_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class IBuilder(ABC):
    @property
    @abstractmethod
    def part(self) -> Part:
        raise NotImplementedError()

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_a(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_b(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def produce_part_c(self) -> None:
        raise NotImplementedError()

class Builder1(IBuilder):
    def __init__(self, p:Part) -> None:
        self._p = p
    
    def reset(self) -> None:
        self._p = Part()

    @property
    def part(self) -> Part:
        p = self._p
        self.reset()
        return p

    @part.setter
    def part(self, val:Part) -> None:
        self._p = val

    def produce_part_a(self) -> None:
        self._p.add('partA')

    def produce_part_b(self) -> None:
        self._p.add('partB')

    def produce_part_c(self) -> None:
        self._p.add('partC')

class Part:
    def __init__(self) -> None:
        self._parts = list()
    
    def add(self, p:Any) -> None:
        self._parts.append(p)

    def __str__(self) -> str:
        return f'part list: {self._parts}'

def client_code(d:Director) -> Optional[None]:
    d.produce_min_feature_product()
    print(d.builder.part)
    d.produce_full_fledge_product()
    print(d.builder.part)

def main() -> None:
    b = Builder1(Part())
    d = Director(b)
    client_code(d)

if __name__ == '__main__':
    main()