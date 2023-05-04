"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod
import random

class IObserver(ABC):
    @abstractmethod
    def react(self, sub: ISubject) ->None:
        raise NotImplementedError

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob: IObserver) -> None:
        raise NotImplementedError
    @abstractmethod
    def detach(self, ob: IObserver) -> None:
        raise NotImplementedError
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError
    
class Subject1(ISubject):
    state: int = 0

    def __init__(self) -> None:
        self._observers: list[IObserver] = list()

    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)
    
    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.react(self)

    def operate(self) -> None:
        self.state = random.randint(1, 10)
        print(f"{self.__class__.__qualname__} state changed to {self.state}. Who reacted?")
        self.notify()

class Observer1(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state <= 6:
            print(f"{self.__class__.__name__} reacted")

class Observer2(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state >= 4:
            print(f"{self.__class__.__name__} reacted")

def client_code() -> None:
    s: Subject1 = Subject1()
    o1: Observer1 = Observer1()
    o2: Observer2 = Observer2()
    s.attach(o1)
    s.attach(o2)
    for _ in range(10):
        s.operate()

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()