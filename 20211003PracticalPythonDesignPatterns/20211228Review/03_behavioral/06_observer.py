# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class ISubject(ABC):
    @abstractmethod
    def notify(self)->None: pass

    @abstractmethod
    def attach(self, ob:IObserver)->None: pass

    @abstractmethod
    def dettach(self, ob:IObserver)->None: pass

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._obersers:List[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        self._obersers.append(ob)

    def dettach(self, ob: IObserver) -> None:
        self._obersers.remove(ob)

    def notify(self) -> None:
        for ob in self._obersers:
            ob.update(self)

    def operation(self)->None:
        self._state = random.randrange(1, 10)
        self.notify()

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ISubject)->None:
        pass

class OberserA(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state >= 5:
            print(f'{self.__class__} : reacted')

class OberserB(IObserver):
    def update(self, sub: ISubject) -> None:
        if sub._state <= 5:
            print(f'{self.__class__} : reacted')