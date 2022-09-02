"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Director:
    def __init__(self, builder:IBuilder) -> None:
        self._builder = builder

    @property
    def builder(self) -> IBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, val:IBuilder) -> None:
        self._builder = val

    def build_min_feature_product(self) -> None:
        self._builder.build_part_a()

    def build_max_feature_product(self) -> None:
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()

class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def part(self) -> Part:
        raise NotImplementedError()

    @abstractmethod
    def build_part_a(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def build_part_b(self) -> None:
        raise NotImplementedError()
        
    @abstractmethod
    def build_part_c(self) -> None:
        raise NotImplementedError()

class Builder(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._part = Part()

    @property
    def part(self) -> Part:
        p = self._part
        self.reset()
        return p

    @part.setter
    def part(self, val:Part) -> None:
        self._part = val

    def build_part_a(self) -> None:
        self._part.add('partA')

    def build_part_b(self) -> None:
        self._part.add('partB')

    def build_part_c(self) -> None:
        self._part.add('partC')

class Part:
    def __init__(self) -> None:
        self._parts:List[str] = []

    def add(self, item:str) -> None:
        self._parts.append(item)

    def __str__(self) -> str:
        return f'part lits: {self._parts}'

def client_code() -> None:
    b1 = Builder()
    d1 = Director(b1)
    d1.builder = b1
    d1.build_min_feature_product()
    print(d1.builder.part)
    d1.build_max_feature_product()
    print(d1.builder.part)

if __name__ == '__main__':
    client_code()