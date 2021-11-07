# subject - observer
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List
import random

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass
    
    @abstractmethod
    def notify(self)->None:
        pass

class ConcreteSubject(Subject):
    _state:int = None

    def __init__(self)->None:
        self._observers:List[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)

    def some_business_logic(self)->None:
        print(f'{self.__class__} changes state')
        self._state = random.randrange(1, 10)
        self.notify()

class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, sub:Subject)->None:
        pass

class ConcreteObservre1(IObserver):
    def update(self, sub: Subject) -> None:
        if sub._state > 3:
            print(f'{self.__class__} reacted')

class ConcreteObservre2(IObserver):
    def update(self, sub: Subject) -> None:
        if sub._state == 0 or sub._state < 3:
            print(f'{self.__class__} reacted')

def client_code()->None:
    sub = ConcreteSubject()
    ob1 = ConcreteObservre1()
    ob2 = ConcreteObservre2()
    sub.attach(ob1)
    sub.attach(ob2)
    sub.some_business_logic()

if __name__ == '__main__':
    client_code()