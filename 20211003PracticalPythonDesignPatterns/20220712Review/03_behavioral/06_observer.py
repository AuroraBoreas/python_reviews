"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class ISubject(ABC):
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def attah(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def detach(self, ob:IObserver) -> None:
        raise NotImplementedError()

class Subject(ISubject):
    _state:int = None
    def __init__(self) -> None:
        self._obserers:List[IObserver] = list()

    def attah(self, ob: IObserver) -> None:
        self._obserers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._obserers.remove(ob)

    def notify(self) -> None:
        for ob in self._obserers:
            ob.react(self)

    def operate(self) -> None:
        self._state = random.randrange(1, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def react(self, sub:ISubject) -> None:
        raise NotImplementedError()

class ObserverA(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted...')

class ObserverB(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted...')