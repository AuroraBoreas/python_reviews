"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender: IComponent, event: str) -> None:
        raise NotImplementedError

class Mediator1(IMediator):
    def __init__(self, comp1: IComponent, comp2: IComponent) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self

    def notify(self, sender: IComponent, event: str) -> None:
        print(f"{sender.__class__.__name__} sent the request")
        match event:
            case 'A':
                self._comp2.do_c()
            case 'D':
                self._comp1.do_a()
                self._comp1.do_b()
            case _:
                pass

class IComponent(ABC):
    @property
    def mediator(self) -> IMediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, val: IMediator) -> None:
        self._mediator = val

class ComponentA(IComponent):
    def do_a(self) -> None:
        print(f'{self.__class__.__name__} do_a')
        self.mediator.notify(self, 'A')

    def do_b(self) -> None:
        print(f'{self.__class__.__name__} do_b')

class ComponentB(IComponent):
    def do_c(self) -> None:
        print(f'{self.__class__.__name__} do_c')

    def do_d(self) -> None:
        print(f'{self.__class__.__name__} do_d')
        self.mediator.notify(self, 'D')

def client_code() -> None:
    c1: IComponent = ComponentA()
    c2: IComponent = ComponentB()
    m1: Mediator1 = Mediator1(c1, c2)
    c1.do_a()
    c2.do_d()

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()