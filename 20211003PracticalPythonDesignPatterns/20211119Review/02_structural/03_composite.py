# tree-like 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Component(ABC):
    @property
    def parent(self)->Component:
        return self._parent

    @parent.setter
    def parent(self, val:Component)->None:
        self._parent = val
    
    def add(self, item:Component)->None:
        pass

    def remove(self, item:Component)->None:
        pass

    def is_composite(self)->bool:
        return False

    @abstractmethod
    def operation(self)->str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = []

    def add(self, item: Component) -> None:
        self._children.append(item)
        self.parent = self

    def remove(self, item: Component) -> None:
        self._children.remove(item)
        self.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        rv = []
        for child in self._children:
            rv.append(child.operation())
        return 'Branch({})'.format('+'.join(rv))

def client_code()->None:
    b1 = Composite()
    b1.add(Leaf())
    b1.add(Leaf())

    b2 = Composite()
    b2.add(Leaf())

    c = Composite()
    c.add(b1)
    c.add(b2)

    print(c.operation())