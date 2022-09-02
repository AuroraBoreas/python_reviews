"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class IObserver(ABC):
    @abstractmethod
    def react(self, sub:ISubject) -> None:
        raise NotImplementedError()

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def detach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __update(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def __update(self) -> None:
        for ob in self._observers:
            ob.react(self)

    def notify(self) -> None:
        self._state = random.randint(1, 10)
        self.update()

class ObserverA(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted..')

class ObserverB(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted..')

def client_code() -> None:
    sub = Subject()
    sub.attach(ObserverA())
    sub.attach(ObserverB())
    sub.notify()

if __name__ == '__main__':
    for _ in range(5):
        print('first time?')
        client_code()