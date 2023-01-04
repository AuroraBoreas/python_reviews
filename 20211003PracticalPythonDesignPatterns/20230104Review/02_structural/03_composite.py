"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class IComponent(ABC):
    def is_composite(self) -> bool:
        return False

    @property
    def parent(self) -> IComponent:
        return self._parent
    
    @parent.setter
    def parent(self, val: IComponent) -> None:
        self._parent = val

    def add(self, item: IComponent) -> None:
        raise NotImplementedError()

    def remove(self, item: IComponent) -> None:
        raise NotImplementedError()

    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(IComponent):
    def operate(self) -> str:
        return 'Leaf'

class Composite(IComponent):
    def __init__(self) -> None:
        self._childrens: list[IComponent] = list()
    
    def add(self, item: IComponent) -> None:
        self._childrens.append(item)
        self.parent = self

    def remove(self, item: IComponent) -> None:
        self._childrens.remove(item)
        self.parent = None
    
    def is_composite(self) -> bool:
        return True

    def operate(self) -> str:
        rev: list[IComponent] = list()
        for child in self._childrens:
            rev.append(child.operate())
        return f"Branch({'+'.join(rev)})"

def main() -> None:
    c: Composite = Composite()
    c.add(Leaf())
    c.add(Leaf())
    c1: Composite = Composite()
    c1.add(Leaf())
    c.add(c1)
    logging.info(c.operate())

if __name__ == '__main__':
    main()