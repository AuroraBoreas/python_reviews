# 
from __future__ import annotations
from abc import ABC, abstractmethod
from random import random
from typing import List


class ISubject(ABC):
    @abstractmethod
    def add(self, ob:IObserver)->None: pass
    
    @abstractmethod
    def remove(self, ob:IObserver)->None: pass

    @abstractmethod
    def notify(self)->None: pass

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = []
    
    def add(self, ob: IObserver) -> None:
        return super().add(ob)

    def remove(self, ob: IObserver) -> None:
        return super().remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.update(self)

    def operation(self)->None:
        self._state = random.randrang(1, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class ObserverA(IObserver):
    def update(self, sub:ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__}: reacted')

class ObserverB(IObserver):
    def update(self, sub:ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__}: reacted')