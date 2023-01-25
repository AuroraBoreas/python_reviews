from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def part(self) -> Part:
        pass

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
    def __init__(self) -> None:
        self._part: Part = Part()

    @property
    def part(self) -> Part:
        p: Part = self._part
        self.reset()
        return p

    @part.setter
    def part(self, value: Part) -> None:
        self._part = value

    def reset(self) -> None:
        self._part = Part()

    def make_part_a(self) -> None:
        self._part.add('partA')

    def make_part_b(self) -> None:
        self._part.add('partB')

    def make_part_c(self) -> None:
        self._part.add('partC')

class Part:
    def __init__(self) -> None:
        self._children: list[Any] = list()

    def add(self, item: Any) -> None:
        self._children.append(item)

    def remove(self, item: Any) -> None:
        self._children.remove(item)

    def __str__(self) -> str:
        return f"part list: {', '.join(map(str, self._children))}"

class Director:
    def __init__(self, b: IBuilder) -> None:
        self._builder: IBuilder = b

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, value: IBuilder) -> None:
        self._builder = value

    def produce_min_feature_product(self) -> None:
        self.builder.make_part_a()

    def produce_max_feature_product(self) -> None:
        self.builder.make_part_a()
        self.builder.make_part_b()
        self.builder.make_part_c()

def client_code(d: Director) -> None:
    d.produce_max_feature_product()
    print(d.builder.part)
    d.builder.reset()
    d.produce_min_feature_product()
    print(d.builder.part)

def main() -> None:
    d: Director = Director(Builder1())
    client_code(d)

if __name__ == '__main__':
    main()
