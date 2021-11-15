# subject - observer 
from __future__ import annotations
from abc import ABC, abstractmethod
from random import random
from typing import List


class ISubject(ABC):
    @abstractmethod
    def notify(self)->None:
        pass

    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass

class ConcreteSubject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)
        
    def some_business_logic(self)->None:
        self._state = random.randrange(1, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class ObserverA(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__}: reacted')

class ObserverB(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__}: reacted')

def client_code()->None:
    sub = ConcreteSubject()
    ob1 = ObserverA()
    ob2 = ObserverB()
    sub.attach(ob1)
    sub.attach(ob2)

    sub.some_business_logic()