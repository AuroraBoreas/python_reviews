"#" 
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:IComponent, event:str)->None:
        pass

class IComponent(ABC):
    @property
    def mediator(self)->IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:IMediator)->None:
        self._mediator = val

class Mediator(IMediator):
    def __init__(self, comp1:IComponent, comp2:IComponent) -> None:
        self._comp1          = comp1
        self._comp1.mediator = self
        self._comp2          = comp2
        self._comp2.mediator = self

    def notify(self, sender: IComponent, event: str) -> None:
        print(f'sender: {sender.__class__}')
        if event == 'a':
            print(f'{self.__class__} do something important')
            self._comp2.do_d()
        elif event == 'd':
            print(f'{self.__class__} do another important thing')
            self._comp1.do_b()
            self._comp2.do_c()

class ComponentA(IComponent):
    def do_a(self)->None:
        print(f'{self!r} do_a')
        self.mediator.notify(self, 'a')

    def do_b(self)->None:
        print(f'{self!r} do_b')

class ComponentB(IComponent):
    def do_c(self)->None:
        print(f'{self!r} do_c')

    def do_d(self)->None:
        print(f'{self!r} do_d')
        self.mediator.notify(self, 'd')