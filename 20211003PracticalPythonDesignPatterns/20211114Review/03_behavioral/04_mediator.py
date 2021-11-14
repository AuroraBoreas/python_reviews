# components - mediator - components
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, sender:BaseComponent, event:str)->None:
        pass

class ConcreteMediator(IMediator):
    def __init__(self, comp1:ComponentA, comp2:ComponentB) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self
        
    def notify(self, sender: BaseComponent, event: str) -> None:
        print(f'sender: {sender.__class__}')
        if event == 'A':
            print(f'{self.__class__}: i wanna do the following operation:')
            self._comp1.do_b()
        elif event == 'D':
            print(f'{self.__class__}: i wanna do the following operation:')
            self._comp1.do_b()
            self._comp2.do_d()

class BaseComponent:
    def __init__(self) -> None:
        self._mediator:IMediator = None

    @property
    def mediator(self)->IMediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, val:IMediator)->None:
        self._mediator = val

class ComponentA(BaseComponent):
    def do_a(self)->None:
        print(f'{self.__class__} do_a')
        self._mediator.notify(self, 'A')

    def do_b(self)->None:
        print(f'{self.__class__} do_b')
        # self._mediator.notify(self, 'A')

class ComponentB(BaseComponent):
    def do_c(self)->None:
        print(f'{self.__class__} do_c')
        self._mediator.notify(self, 'C')

    def do_d(self)->None:
        print(f'{self.__class__} do_d')
        # self._mediator.notify(self, 'D')

def client_code()->None:
    ca = ComponentA()
    cb = ComponentB()
    me = ConcreteMediator(ca, cb)
    
    ca.do_a()

    print()

    cb.do_d()

if __name__ == '__main__':
    client_code()