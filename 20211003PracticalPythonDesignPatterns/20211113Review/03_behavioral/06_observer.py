# Subject - Observer
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List
import random

class ISubject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, ob:IObserver)->None:
        pass
    
    @abstractmethod
    def remove(self, ob:IObserver)->None:
        pass
    
    @abstractmethod
    def notify(self)->None:
        pass

class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class ConcreteSubject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []

    def add(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def remove(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)

    def some_business_logic(self)->None:
        print(f'{self!r} changes state')
        self._state = random.randrange(1, 10)
        self.notify()

class ObserverA(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self!r} reacted')

class ObserverB(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self!r} reacted')
    
def client_code()->None:
    sub = ConcreteSubject()
    ob1 = ObserverA()
    ob2 = ObserverB()
    sub.add(ob1)
    sub.add(ob2)
    for _ in range(3):
        sub.some_business_logic()

if __name__ == '__main__':
    client_code()