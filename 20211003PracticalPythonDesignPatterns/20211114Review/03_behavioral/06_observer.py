# subject - oberver 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
import random
from typing import List


class ISubject(metaclass=ABCMeta):
    @abstractmethod
    def notify(self)->None:
        pass

    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass
    
    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class ConcreteSubject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self.observers:List[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self.observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self.observers.remove(ob)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)

    def some_business_logic(self)->None:
        print(f'{self.__class__}: i wanna change my state:')
        self._state = random.randrange(1, 10)
        self.notify()

class ConcreteObserver1(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted')

class ConcreteObserver2(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted')

def client_code()->None:
    sub = ConcreteSubject()
    ob1 = ConcreteObserver1()
    ob2 = ConcreteObserver2()
    sub.attach(ob1)
    sub.attach(ob2)
    for _ in range(3):
        sub.some_business_logic()
