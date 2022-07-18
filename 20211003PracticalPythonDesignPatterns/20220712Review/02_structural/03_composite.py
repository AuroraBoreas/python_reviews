"#" 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, val:Component) -> None:
        self._parent = val

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def add(self, item:Component) -> None:
        pass

    @abstractmethod
    def remove(self, item:Component) -> None:
        pass

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = list()

    def add(self, item: Component) -> None:
        self._children.append(item)
        self._parent = self

    def remove(self, item: Component) -> None:
        self._children.remove(item)
        self._parent = None

    def operate(self) -> str:
        rv = list()
        for child in self._children:
            rv.append(child.operate())
        return f'Branch({"+".join(map(str, self._children))})'