# 
from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    def is_composite(self) -> bool:
        return False
    
    def add(self, item: Component) -> None:
        pass

    def remove(self, item: Component) -> None:
        pass

    @property
    def parent(self) -> Component:
        return self._parent
    
    @parent.setter
    def parent(self, val: Component) -> None:
        self._parent = val

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

    def add(self, item: Component) -> None:
        self._children.append(item)
        self.parent = self
    
    def remove(self, item: Component) -> None:
        self._children.remove(item)
        self.parent = None
    
    def operate(self) -> str:
        rv: list[str] = []
        for child in self._children:
            rv.append(child.operate())
        return f"Branch({'+'.join(map(str, rv))})"

def client_code() -> None:
    c: Composite = Composite()
    d: Composite = Composite()
    d.add(Leaf())
    d.add(Leaf())
    c.add(Leaf())
    c.add(d)
    print(c.operate())

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()