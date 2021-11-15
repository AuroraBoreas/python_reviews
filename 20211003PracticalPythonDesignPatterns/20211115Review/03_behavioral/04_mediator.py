# components - mediator - components 
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:IComponent, event:str)->None:
        pass

class Mediator(IMediator):
    def __init__(self, comp1:ConcreteComponent, comp2:ConcreteComponent) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self
        
    def notify(self, sender: IComponent, event: str) -> None:
        if event == 'A':
            print(f'{self.__class__}: i will do the following operation:')
            self._comp2.do_c()
        elif event == 'D':
            print(f'{self.__class__}: i will do the following operation:')
            self._comp1.do_b()
            self._comp2.do_c()

class IComponent(ABC):
    @property
    def mediator(self)->IMediator:
        pass

    @mediator.setter
    def mediator(self, val:IMediator)->None:
        pass

class ConcreteComponent(IComponent):
    @property
    def mediator(self) -> IMediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, val:IMediator) -> None:
        self._mediator = val

class ComponentA(ConcreteComponent):
    def do_a(self)->None:
        print(f'{self.__class__}: do_a')
        self.mediator.notify(self, 'A')

    def do_b(self)->None:
        print(f'{self.__class__}: do_b')

class ComponentB(ConcreteComponent):
    def do_c(self)->None:
        print(f'{self.__class__}: do_c')

    def do_d(self)->None:
        print(f'{self.__class__}: do_d')
        self.mediator.notify(self, 'D')

def client_code()->None:
    c1 = ComponentA()
    c2 = ComponentB()
    me = Mediator(c1, c2)

    c1.do_a()
    c2.do_d()