from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def handle(self, comp: IComponent, event: str) -> None:
        pass

class Mediator1(IMediator):
    def __init__(self, comp1: IComponent, comp2: IComponent) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self

    def handle(self, comp: IComponent, event: str) -> None:
        print(f"{self.__class__} handles {comp.__class__}")
        match (event):
            case 'A':
                self._com1.do_b()
            case 'D':
                self._comp1.do_a()
                self._comp2.do_d()

class IComponent(ABC):
    @property
    def mediator(self) -> IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, value: IMediator) -> None:
        self._mediator = value

class ComponentA(IComponent):
    def do_a(self) -> None:
        print(f"{self.__class__} does something important")
        self.mediator.handle(self, "A")

    def do_b(self) -> None:
        print(f"{self.__class__} does another thing(b)")

class ComponentB(IComponent):
    def do_c(self) -> None:
        print(f"{self.__class__} does another thing(c)")

    def do_d(self) -> None:
        print(f"{self.__class__} does something important")
        self.mediator.handle(self, "D")
