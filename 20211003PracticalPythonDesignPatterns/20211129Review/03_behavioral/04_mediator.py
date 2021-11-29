# 
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:Component, event:str)->None:
        pass

class Mediator(IMediator):
    def __init__(self, comp1:Component, comp2:Component) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self

    def notify(self, sender: Component, event: str) -> None:
        print(f'sender: {sender.__class__}:')
        if event == 'A':
            print(f'{self.__class__} : reacted to event({event})')
        elif event == 'D':
            print(f'{self.__class__} : reacted to event({event})')

class Component(ABC):
    @property
    def mediator(self)->Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:Mediator)->None:
        self._mediator = val

class ComponentA(Component):
    def do_a(self)->None:
        print(f'{self.__class__} do_a')
        self.mediator.notify(self, 'A')

    def do_b(self)->None:
        print(f'{self.__class__} do_b')

class ComponentB(Component):
    def do_c(self)->None:
        print(f'{self.__class__} do_c')

    def do_d(self)->None:
        print(f'{self.__class__} do_d')
        self.mediator.notify(self, 'D')