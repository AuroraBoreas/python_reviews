# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def dettach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def notify(self)->None:
        pass

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def dettach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)

    def operation(self)->None:
        self._state = random.randrange(1, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def notify(self, sub:Subject)->None:
        pass

class ObserverA(IObserver):
    def notify(self, sub: Subject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} reacted')

class ObserverB(IObserver):
    def notify(self, sub: Subject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} reacted')