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

    def add(self, item:Component) -> Component:
        raise NotImplementedError()
    
    def remove(self, item:Component) -> Component:
        raise NotImplementedError()

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Component):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = list()

    def add(self, item: Component) -> Component:
        self._children.append(item)
        self.parent = self
        return self

    def remove(self, item: Component) -> Component:
        self._children.remove(item)
        self.parent = None
        return self

    def is_composite(self) -> bool:
        return True   

    def operate(self) -> str:
        result:List = []
        for child in self._children:
            result.append(child.operate())
        return f'Branch({"+".join(map(str, result))})'


def client_code() -> None:
    c1:Composite = Composite()
    c1.add(Leaf())
    c1.add(Composite().add(Leaf()))
    print(c1.operate())

if __name__ == '__main__':
    client_code()