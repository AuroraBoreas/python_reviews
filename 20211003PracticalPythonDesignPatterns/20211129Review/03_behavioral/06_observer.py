# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class ISubject(ABC):
    @abstractmethod
    def add(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def remove(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def notify(self)->None:
        pass

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []

    def add(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def remove(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)

    def some_business_logic(self)->None:
        self._state = random.randrange(1, 10)

    def operation(self)->None:
        self.some_business_logic()
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class ObserverA(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__}: reacated')

class ObserverB(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__}: reacted')