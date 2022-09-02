"#" 

from __future__ import annotations
from abc import abstractmethod
from typing import List

class Component:
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, val:Component) -> None:
        self._parent = val

    def is_composite(self) -> bool:
        return False

    def add(self, item:Component) -> None: pass
    def remove(self, item:Component) -> None: pass

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = []

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
        return 'Branch({})'.format("+".join(map(str, res)))

def client_code() -> None:
    c:Composite = Composite()
    c.add(Leaf())
    c.add(Leaf())
    print(c.operate())

if __name__ == '__main__':
    client_code()