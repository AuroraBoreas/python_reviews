# 

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstract:
    def __init__(self, comp1: IComponent) -> None:
        self._comp1 = comp1

    def operate(self) -> None:
        print(f'{self.__class__} : {self._comp1.do_this()} implemented on platform A')

class ExtendedAbstract(Abstract):
    def operate(self) -> None:
        print(f'{self.__class__} : {self._comp1.do_this()} implemented on platform B')

class IComponent(ABC):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError

class ComponentA(IComponent):
    def do_this(self) -> str:
        return f'{self.__class__} do this'

class ComponentB(IComponent):
    def do_this(self) -> str:
        return f'{self.__class__} do this'