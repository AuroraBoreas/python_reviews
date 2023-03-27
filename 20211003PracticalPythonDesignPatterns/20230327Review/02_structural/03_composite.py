# 
from __future__ import annotations
from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def is_composite(self) -> bool:
        return False
    
    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError

    @property
    def parent(self) -> IComponent:
        return self._parent
    
    def add(self, item: IComponent) -> None:
        raise NotImplementedError
    
    def remove(self, item: IComponent) -> None:
        raise NotImplementedError
    
class Leaf(IComponent):
    def operate(self) -> str:
        return 'Leaf'
    
class Composite(IComponent):
    def __init__(self) -> None:
        self._children: list[IComponent] = list()

    def is_composite(self) -> bool:
        return True
    
    def add(self, item: IComponent) -> None:
        self._children.append(item)
        self.parent = self

    def remove(self, item: IComponent) -> None:
        self._children.remove(item)
        self.parent = None

    def operate(self) -> str:
        res: list[IComponent] = list()
        for child in self._children:
            res.append(child.operate())
        return f'Branch({"".join(map(str, res))})'