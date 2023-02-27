# 
from __future__ import annotations
from abc import ABC, abstractmethod
import random


class IObserver(ABC):
    @abstractmethod
    def react(self, sub: ISubject) -> None:
        raise NotImplementedError

class Observer1(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f"{self.__class__} reacted")

class Observer2(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f"{self.__class__} reacted")

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
    
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError
    
class Subject1(ISubject):
    _state: int = None

    def __init__(self) -> None:
        self._observers: list[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def operate(self) -> None:
        self._state = random.randint(1, 10)
        self.notify()

    def notify(self) -> None:
        for ob in self._observers:
            ob.react(self)

def client_code() -> None:
    ob1: IObserver = Observer1()
    ob2: IObserver = Observer2()
    sub: ISubject  = Subject1()
    sub.attach(ob1)
    sub.attach(ob2)
    for _ in range(10):
        sub.operate()
        print(''.join(['-'] * 10))

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
