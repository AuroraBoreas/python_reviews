"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def dettach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()

class IObserver(ABC):
    @abstractmethod
    def react(self, sub:ISubject) -> None:
        raise NotImplementedError()

class Subject(ISubject):
    _state:int = None
    def __init__(self) -> None:
        self._observers:List[IObserver] = list()
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def dettach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def act(self) -> None:
        self._state = random.randint(1, 10)
        self.notify()

    def notify(self) -> None:
        for ob in self._observers:
            ob.react(self)

class Observer1(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted')

class Observer2(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted')

class Observer3(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state >= 8:
            print(f'{self.__class__} reacted')

def client_code() -> None:
    ob1 = Observer1()
    ob2 = Observer2()
    ob3 = Observer3()
    sub = Subject()
    sub.attach(ob1)
    sub.attach(ob2)
    sub.attach(ob3)
    sub.act()

if __name__ == '__main__':
    for _ in range(10):
        print('=========')
        client_code()