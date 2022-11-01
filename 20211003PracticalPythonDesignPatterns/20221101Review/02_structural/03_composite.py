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
    
    def add(self, item:Component) -> None:
        raise NotImplementedError()

    def remove(self, item:Component) -> None:
        raise NotImplementedError()

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = list()

    def is_composite(self) -> bool:
        return True

    def add(self, item: Component) -> None:
        self._children.append(item)
        self.parent = self

    def remove(self, item: Component) -> None:
        self._children.remove(item)
        self.parent = None

    def operate(self) -> str:
        res:List[Component] = list()
        for child in self._children:
            res.append(child.operate())
        return f'Branch({"+".join(map(str, res))})'

def client_code() -> None:
    c1:Composite = Composite()
    c2:Composite = Composite()
    c2.add(Leaf())
    c2.add(Leaf())
    c1.add(c2)
    c1.add(Leaf())
    print(c1.operate())
    c1.remove(c2)
    print(c1.operate())

if __name__ == '__main__':
    client_code()