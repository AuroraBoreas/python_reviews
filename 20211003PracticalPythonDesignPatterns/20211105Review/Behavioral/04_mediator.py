# mediator: signal tower
from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender:object, event:str)->None: pass


class ConcreteMediator(IMediator):
    def __init__(self, component1:Component1, component2:Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        print(sender)
        if event == 'A':
            print('Mediator reacts on A and triggers following  operation:'); self._component2.do_c()
        elif event == 'D': 
            print('Mediator reacts on D and triggers following  operation:')
            self._component1.do_b(); self._component2.do_c()
            
class BaseComponent:
    def __init__(self, mediator:IMediator=None) -> None:
        self._mediator = mediator

    @property
    def mediator(self)->IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:IMediator)->None:
        self._mediator = val

class Component1(BaseComponent):
    def do_a(self)->None:
        print('Component 1 does A')
        self.mediator.notify(self, 'A')
    
    def do_b(self)->None:
        print('Component 1 does B')
        self.mediator.notify(self, 'B')
    
class Component2(BaseComponent):
    def do_c(self)->None:
        print('Component 2 does C')
        self.mediator.notify(self, 'C')

    def do_d(self)->None:
        print('Component 2 does D')
        self.mediator.notify(self, 'D')

def client_code()->None:
    c1 = Component1()
    c2 = Component2()
    me = ConcreteMediator(c1, c2)

    print('Client triggers operation A')
    c1.do_a()

    print('\n', end='')

    print('client triggers operation D')
    c2.do_d()

if __name__ == '__main__':
    client_code()