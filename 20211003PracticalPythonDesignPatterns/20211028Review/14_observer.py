# subject - observer
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
import random

class ISubject(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass
    
    @abstractmethod
    def notify(self)->None:
        pass

class ConcreteSubject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self.observers = []

    def attach(self, ob: IObserver) -> None:
        self.observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self.observers.remove(ob)

    def notify(self) -> None:
        for ob in self.observers:
            ob.update(self)

    def some_business_logic(self)->None:
        print(f'{self.__class__} changed state')
        self._state = random.randrange(0, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ConcreteSubject)->None:
        pass

class ObserverA(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state > 3:
            print(f'{self.__class__} reacted')

class ObserverB(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state == 0 or sub._state <=3:
            print(f'{self.__class__} reacted')

def client_code():
    sub = ConcreteSubject()
    ob1 = ObserverA()
    ob2 = ObserverB()
    sub.attach(ob1)
    sub.attach(ob2)
    sub.some_business_logic()


if __name__ == '__main__':
    client_code()