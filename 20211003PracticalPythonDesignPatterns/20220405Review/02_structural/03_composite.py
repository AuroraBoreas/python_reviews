"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    def is_composite(self)->bool: return False

    @property
    def parent(self)->Node:
        return self._parent

    @parent.setter
    def parent(self, val:Node)->None:
        self._parent = val

    @abstractmethod
    def operation(self)->str:
        raise NotImplementedError()

class Leaf(Node):
    def operation(self) -> str:
        return 'Leaf'

class Composite(Node):
    def __init__(self) -> None:
        self.children:List[Node] = []
    
    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        rv = []
        for child in self.children:
            rv.append(child.operation())
        return 'Branch({})'.format('+'.join(map(str, rv)))