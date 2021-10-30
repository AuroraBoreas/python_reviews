# subject <-> observer
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class Subject(ABC):
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
    _state:int = 0
    observers: List[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        self.observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self.observers.remove(ob)

    def notify(self) -> None:
        print('ConcreteSubject state changed..')
        for ob in self.observers:
            ob.update(self)
    
    def some_business_logic(self)->None:
        self._state = random.randrange(0, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ConcreteSubject)->None:
        pass

class ConcreteObserverA(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state > 5:
            print('ConcreteObserverA reacted')

class ConcreteObserverB(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state == 0 or sub._state <= 5:
            print('ConcreteObserverB react')

def client_code()->None:
    oba = ConcreteObserverA()
    obb = ConcreteObserverB()
    sub = ConcreteSubject()
    sub.attach(oba)
    sub.attach(obb)
    sub.some_business_logic()
    print('\n------')
    sub.detach(obb)
    sub.some_business_logic()

if __name__ == '__main__':
    client_code()