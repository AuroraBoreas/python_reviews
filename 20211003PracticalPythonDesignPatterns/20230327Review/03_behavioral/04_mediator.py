# 
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, comp: IComponent, event: str) -> None:
        raise NotImplementedError

class Mediator(IMediator):
    def __init__(self, comp1: IComponent, comp2: IComponent) -> None:
        self._comp1          = comp1
        self._comp1.mediator = self
        self._comp2          = comp2
        self._comp2.mediator = self
    
    def notify(self, comp: IComponent, event: str) -> None:
        print(f'{self.__class__}: received {event} from {comp.__class__.__name__}')
        if event == 'A':
            self._comp2.do_c()
            self._comp2.do_d()
        elif event == 'D':
            self._comp1.do_b()

class IComponent(ABC):
    @property
    def mediator(self) -> IMediator:
        return self._mediator

class ComponentA(IComponent):
    def do_a(self) -> None:
        print(f'{self.__class__} : do_a')
        self.mediator.notify(self, "A")
        
    def do_b(self) -> None:
        print(f'{self.__class__} : do_b')

class ComponentB(IComponent):
    def do_c(self) -> None:
        print(f'{self.__class__} : do_c')

    def do_d(self) -> None:
        print(f'{self.__class__} : do_d')
        self.mediator.notify(self, "D")