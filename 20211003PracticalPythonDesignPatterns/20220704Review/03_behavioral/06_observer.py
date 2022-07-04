"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List


class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject) -> None:
        pass

class Subject(ISubject):
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

    def operation(self) -> None:
        self._state = random.randint(1, 10)
        self.notify()

class Observer1(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted')

class Observer2(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted')

def client_code() -> None:
    ob1 = Observer1()
    ob2 = Observer2()
    sub = Subject()
    sub.attach(ob1)
    sub.attach(ob2)
    for _ in range(5):
        sub.operation()

if __name__ == '__main__':
    client_code()