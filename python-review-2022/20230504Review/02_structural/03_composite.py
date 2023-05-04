"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Self

class Component(ABC):
    def is_composite(self) -> bool:
        return False
    
    @property
    def parent(self) -> Self:
        return self._parent
    
    @parent.setter
    def parent(self, val: Component) -> None:
        self._parent = val

    def add(self, node: Component) -> None:
        raise NotImplementedError
    
    def remove(self, node: Component) -> None:
        raise NotImplementedError

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError
    
class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'
    
class Composite(Component):
    def __init__(self) -> None:
        self._children: list[Component] = list()

    def is_composite(self) -> bool:
        return True
    
    def add(self, node: Component) -> None:
        self._children.append(node)
        self.parent = self

    def remove(self, node: Component) -> None:
        self._children.remove(node)
        self.parent = None

    def operate(self) -> str:
        res: list[Component] = list()
        for child in self._children:
            res.append(child.operate())
        return f"Branch({'+'.join(map(str, res))})"

def client_code() -> None:
    c: Composite = Composite()
    c.add(Leaf())
    node: Composite = Composite()
    node.add(Leaf())
    node.add(Leaf())
    c.add(node)
    print(c.operate())

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()