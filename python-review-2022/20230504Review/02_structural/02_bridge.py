"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstract:
    def __init__(self, component: IComponent) -> None:
        self._comp = component

    def apply(self) -> None:
        print(f"{self.__class__}: {self._comp.operate()} on platform A")

class ExtendedAbstract(Abstract):
    def apply(self) -> None:
        print(f"{self.__class__}: {self._comp.operate()} on platform B")

class IComponent(ABC):
    @abstractmethod
    def operate(self) -> str:
        raise NotImplementedError
    
class Component(IComponent):
    def operate(self) -> str:
        return f"{self.__class__} does sth"