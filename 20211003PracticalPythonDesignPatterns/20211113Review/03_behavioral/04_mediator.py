# mediator
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:object, event:str)->None:
        pass

class ConcreteMediator(IMediator):
    def __init__(self, comp1:ComponentA, comp2:ComponentB)->None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        print(f'  sender: {sender.__class__}')
        if event == 'A':
            print('  Mediator reacts on A and triggers following operations:')
            self._comp2.do_c()
        elif event == 'D':
            print('  Mediator reacts on D and triggers following operations:')
            self._comp1.do_b()
            self._comp2.do_c()

class BaseComponent:
    def __init__(self, mediator:IMediator=None) -> None:
        self._mediator:IMediator = mediator

    @property
    def mediator(self)->IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:IMediator)->None:
        self._mediator = val

class ComponentA(BaseComponent):
    def do_a(self)->None:
        print(f'\n{self.__class__} does a')
        self.mediator.notify(self, 'A')

    def do_b(self)->None:
        print(f'\n{self.__class__} does b')
        self.mediator.notify(self, 'B')

class ComponentB(BaseComponent):
    def do_c(self)->None:
        print(f'\n{self.__class__} does C')
        self.mediator.notify(self, 'C')
    
    def do_d(self)->None:
        print(f'\n{self.__class__} does D')
        self.mediator.notify(self, 'D')

def client_code()->None:
    c1 = ComponentA()
    c2 = ComponentB()
    m  = ConcreteMediator(c1, c2)

    c1.do_a()

    c2.do_d()

if __name__ == '__main__':
    client_code()