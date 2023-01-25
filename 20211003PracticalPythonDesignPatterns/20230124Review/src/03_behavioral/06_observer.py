from __future__ import annotations
from abc import ABC, abstractmethod
import random

class IObserver:
    @abstractmethod
    def react(self, sub: ISubject) -> None:
        raise NotImplementedError

class ObserverA(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state <= 5:
            print(f"{self.__class__} reacted")

class ObserverB(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state >= 4:
            print(f"{self.__class__} reacted")

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def detach(self, ob: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify(self, ob: IObserver) -> None:
        raise NotImplementedError

class Subject1(ISubject):
    state: int = None

    def __init__(self) -> None:
        self._observers: list[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self, ob: IObserver) -> None:
        self.state = random.randint(1, 10)
        for ob in self._observers:
            ob.react(self)
