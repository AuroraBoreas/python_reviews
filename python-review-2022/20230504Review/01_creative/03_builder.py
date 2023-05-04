"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod


class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError
    @property
    @abstractmethod
    def part(self) -> Part:
        raise NotImplementedError
    @abstractmethod
    def make_part_a(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def make_part_b(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def make_part_c(self) -> None:
        raise NotImplementedError
    
class Builder1(IBuilder):
    def __init__(self, part: Part) -> None:
        self._part = part

    def reset(self) -> None:
        self._part = Part()
    
    @property
    def part(self) -> Part:
        p: Part = self._part
        self.reset()
        return p
    
    @part.setter
    def part(self, val: Part) -> None:
        self._part = val

    def make_part_a(self) -> None:
        self._part.add("partA")

    def make_part_b(self) -> None:
        self._part.add("partB")

    def make_part_c(self) -> None:
        self._part.add("partC")

class Director:
    def __init__(self, builder: IBuilder) -> None:
        self._builder = builder

    @property
    def builder(self) -> IBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, val: IBuilder) -> None:
        self._builder = val

    def make_min_feature_product(self) -> None:
        self.builder.make_part_a()

    def make_full_fledged_product(self) -> None:
        self.builder.make_part_a()
        self.builder.make_part_b()
        self.builder.make_part_c()

class Part:
    def __init__(self) -> None:
        self._parts = list()

    def add(self, part: str) -> None:
        self._parts.append(part)

    def remove(self, part: str) -> None:
        self._parts.remove(part)

    def __str__(self) -> str:
        return f"part list: {', '.join(map(str, self._parts))}"

def client_code() -> None:
    p: Part = Part()
    b: IBuilder = Builder1(p)
    d: Director = Director(b)
    d.make_full_fledged_product()
    print(d.builder.part)
    d.make_min_feature_product()
    print(d.builder.part)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()