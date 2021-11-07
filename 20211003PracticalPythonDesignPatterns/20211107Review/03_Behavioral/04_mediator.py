# segregate objects, objects contact via medidator
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, sender:object, event:str)->None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, comp1:Component1, comp2:Component2) -> None:
        self._comp1 = comp1
        self._comp1.mediator = self
        self._comp2 = comp2
        self._comp2.mediator = self
    
    def notify(self, sender: object, event: str) -> None:
        if event == 'A':
            print(f'{self.__class__} reacts on {event} and triggers following operations:')
            self._comp2.do_c()
        elif event == 'D':
            print(f'{self.__class__} reacts on {event} and triggers following operation:')
            self._comp1.do_b()
            self._comp2.do_c()

class BaseComponent:
    def __init__(self, mediator:Mediator=None) -> None:
        self._mediator = mediator

    @property
    def mediator(self)->Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val:Mediator)->None:
        self._mediator = val

class Component1(BaseComponent):
    def do_a(self)->None:
        print(f'{self.__class__} do A')
        self.mediator.notify(self, 'A')

    def do_b(self)->None:
        print(f'{self.__class__} do B')
        self.mediator.notify(self, 'B')

class Component2(BaseComponent):
    def do_c(self)->None:
        print(f'{self.__class__} do C')
        self.mediator.notify(self, 'C')

    def do_d(self)->None:
        print(f'{self.__class__} do D')
        self.mediator.notify(self, 'D')

def client_code()->None:
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print('Client triggers operation A.')
    c1.do_a()

    print('\n')
    print('Client triggers operation D..')
    c2.do_d()

if __name__ == '__main__':
    client_code()
