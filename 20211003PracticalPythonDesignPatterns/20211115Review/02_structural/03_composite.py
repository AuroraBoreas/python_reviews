# tree-like objects 
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

    def add(self, comp:Component)->None:
        pass

    def remove(self, comp:Component)->None:
        pass

    def is_composite()->bool:
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

    def add(self, comp: Component) -> None:
        self._children.append(comp)
        self.parent = self

    def remove(self, comp: Component) -> None:
        self._children.remove(comp)
        self.parent = None

    def is_composite() -> bool:
        return True

    def operation(self) -> str:
        rv = []
        for child in self._children:
            rv.append(child.operation())
        return f'branch({"+".join(rv)})'

def client_code()->None:
    tree = Composite()
    
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print(tree.operation())

if __name__ == '__main__':
    client_code()