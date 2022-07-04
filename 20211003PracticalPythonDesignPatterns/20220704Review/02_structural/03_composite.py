"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List


class Component:
    __metaclass__ = ABCMeta

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
    def operation(self) -> str: raise NotImplementedError()

class Leaf(Component):
    def operation(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children:List[Component] = []
    
    def is_composite(self) -> bool:
        return True
    
    def add(self, item: Component) -> None:
        self._children.append(item)
        self._parent = self

    def remove(self, item: Component) -> None:
        self._children.remove(item)
        self._parent = None

    def operation(self) -> str:
        rv = []
        for child in self._children:
            rv.append(child.operation())
        return f'Branch({"+".join(map(str, rv))})'