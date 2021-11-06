# tree - node
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self)->Component:
        return self._parent

    @parent.setter
    def parent(self, val:Component)->None:
        self._parent = val

    def add(self, component:Component)->None:
        pass

    def remove(self, component:Component)->None:
        pass

    def is_composite(self)->bool:
        return False

    @abstractmethod
    def operation(self)->str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return 'Leaf'

class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        self.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        self.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f'Brach({"+".join(results)})'

def client_code(component:Component)->None:
    print(f'RESULT: {component.operation()}', end='')

def client_code2(component1:Component, component2:Component)->None:
    if component1.is_composite():
        component1.add(component2)
    print(f'RESULT: {component1.operation()}', end='')

if __name__ == '__main__':
    simple = Leaf()
    print('Client: i have got a simple component')
    client_code(simple)
    print('\n')

    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print('Client: now i have got a composite tree:')
    client_code(tree)
    print('\n')

    print('Client: i dont need to check the components classes even when managing the tree!')
    client_code2(tree, simple)
