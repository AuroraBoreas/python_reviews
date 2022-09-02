"#" 

from __future__ import annotations
from abc import ABC, abstractmethod

class IMediator(ABC):
    @abstractmethod
    def signal(self, sender:IComponent, event:str) -> None:
        raise NotImplementedError()

class Mediator(IMediator):
    def __init__(self, c1:IComponent, c2:IComponent) -> None:
        self._c1          = c1
        self._c1.mediator = self
        self._c2          = c2
        self._c2.mediator = self

    def signal(self, sender: IComponent, event: str) -> None:
        print(f'{self.__class__} received event {event}, sender: {sender.__class__}')
        if event == 'A':
            self._c2.do_c()
            self._c2.do_d()
        if event == 'D':
            self._c1.do_b()

class IComponent(ABC):
    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:Mediator) -> None:
        self._mediator = val

class ComponentA(IComponent):
    def do_a(self) -> None:
        print(f'{self.__class__} do_a')
        self.mediator.signal(self, 'A')

    def do_b(self) -> None:
        print(f'{self.__class__} do_b')

class ComponentB(IComponent):
    def do_c(self) -> None:
        print(f'{self.__class__} do_c')
    
    def do_d(self) -> None:
        print(f'{self.__class__} do_d')
        self.mediator.signal(self, 'D')

def client_code() -> None:
    ca = ComponentA()
    cb = ComponentB()
    m = Mediator(ca, cb)
    ca.do_a()
    cb.do_d()

if __name__ == '__main__':
    client_code()