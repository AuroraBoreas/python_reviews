# 
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:Component, event:str) -> str:
        pass

class Mediator(IMediator):
    def __init__(self, comp1:Component, comp2:Component) -> None:
        self._comp1          = comp1
        self._comp1.mediator = self
        self._comp2          = comp2
        self._comp2.mediator = self

    def notify(self, sender: Component, event: str) -> str:
        print(f'\nsender: {sender.__class__}')
        if event == 'A':
            print(f'{self.__class__} received event {event}')
            self._comp1.do_b()
        if event == 'D':
            print(f'{self.__class__} received event {event}')
            self._comp2.do_c()
        
class Component(ABC):
    @property
    def mediator(self) -> IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:IMediator) -> None:
        self._mediator = val

class ComponentA(Component):
    def do_a(self) -> None:
        print(f'{self.__class__} do_a')
        self._mediator.notify(self, 'A')

    def do_b(self) -> None:
        print(f'{self.__class__} do_b')

class ComponentB(Component):
    def do_c(self) -> None:
        print(f'{self.__class__} do_c')

    def do_d(self) -> None:
        print(f'{self.__class__} do_d')
        self._mediator.notify(self, 'D')

def client_code() -> None:
    c1 = ComponentA()
    c2 = ComponentB()
    m = Mediator(c1, c2)
    c1.do_a()
    c2.do_d()

if __name__ == '__main__':
    client_code()