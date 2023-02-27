# 
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstract:
    def __init__(self, comp: IComponent) -> None:
        self._comp = comp
    def handle(self) -> None:
        print(f"{self.__class__}: {self._comp.operate()} on platform A")

class ExtendedAbstract(Abstract):
    def handle(self) -> None:
        print(f"{self.__class__}: {self._comp.operate()} on platform B")

class IComponent(ABC):
    @abstractmethod
    def operate(self) -> None:
        raise NotImplementedError

class Component1(IComponent):
    def operate(self) -> None:
        return f"{self.__class__} operates"