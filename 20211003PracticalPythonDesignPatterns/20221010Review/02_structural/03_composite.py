#
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Node(ABC):
    def add(self, node:Node) -> None:
        pass
    
    def remove(self, node:Node) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @property
    def parent(self) -> None:
        self._parent = self
    
    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError()

class Leaf(Node):
    def operate(self) -> str:
        return 'Leaf'

class Composite(Node):
    def __init__(self) -> None:
        self._children:List[Node] = []
    
    def add(self, node: Node) -> None:
        self._children.append(node)
        self._parent = self

    def remove(self, node: Node) -> None:
        self._children.remove(node)
        self._parent = None

    def is_composite(self) -> bool:
        return True

    def operate(self) -> str:
        res:List[Any] = list()
        for child in self._children:
            res.append(child.operate())
        return f'{self.__class__} : {res}'
