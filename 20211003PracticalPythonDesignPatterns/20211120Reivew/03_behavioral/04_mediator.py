from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:BaseComponent, event:str)->None:
        pass

class Mediator(IMediator):
    def __init__(self, comp1:BaseComponent, comp2:BaseComponent) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self

    def notify(self, sender: BaseComponent, event: str) -> None:
        print(f'sender: {sender.__class__}')
        if event == 'A':
            print(f'{self.__class__}: received {event}')
            self._comp2.do_c()
        elif event == 'D':
            print(f'{self.__class__}: received {event}')
            self._comp1.do_a()
            self._comp2.do_b()

class BaseComponent(ABC):
    @property
    def mediator(self)->IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:IMediator)->None:
        self._mediator = val

class ComponentA(BaseComponent):
    def do_a(self) -> None:
        print(f'{self.__class__} : do_a;')
        self._mediator.notify(self, 'A')

    def do_b(self) -> None:
        print(f'{self.__class__} : do_b;')

class ComponentB(BaseComponent):
    def do_c(self) -> None:
        print(f'{self.__class__} : do_c;')

    def do_d(self) -> None:
        print(f'{self.__class__} : do_d;')
        self._mediator.notify(self, 'D')

