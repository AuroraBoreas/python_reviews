
from abc import ABC, abstractmethod
from typing import Self


class Component(ABC):
    def is_parent(self) -> bool:
        return False

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError

    @property
    def parent(self) -> Self:
        return self._parent

    @parent.setter
    def parent(self, value: Self) -> None:
        self._parent = value

    def add(self, node: Self) -> None:
        pass

    def remove(self, node: Self) -> None:
        pass

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self.children: list[Component] = list()

    def add(self, node: Self) -> None:
        self.children.append(node)
        self.parent = self

    def remove(self, node: Self) -> None:
        self.children.remove(node)
        self.parent = None

    def is_parent(self) -> bool:
        return True

    def operate(self) -> str:
        rv: list[Component] = []
        for child in self.children:
            rv.append(child.operate())
        return f"Branch({'+'.join(rv)})"
