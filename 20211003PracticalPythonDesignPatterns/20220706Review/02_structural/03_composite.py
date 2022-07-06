# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    def is_composite(self) -> bool:
        return False

    def add(self, comp:Component) -> None:
        pass

    def remove(self, comp:Component) -> None:
        pass

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, val:Component) -> None:
        self._parent = val

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = []
    
    def add(self, comp:Component) -> None:
        self._children.append(comp)
        self.parent = self
    
    def remove(self, comp:Component) -> None:
        self._children.remove(comp)
        self.parent = None

    def operate(self) -> str:
        rv:List[Component] = []
        for child in self._children:
            rv.append(child.operate())
        return f'Branch({"+".join(map(str, rv))})'