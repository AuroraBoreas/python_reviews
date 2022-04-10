"#" 
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
import random
from typing import List


class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def notify(self)->None:
        pass

class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def subscribe(self, subject:ISubject)->None:
        pass

class Subject(ISubject):
    _state: int = None
    def __init__(self) -> None:
        self._obs:List[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        return self._obs.append(ob)

    def detach(self, ob: IObserver) -> None:
        return self._obs.remove(ob)
    
    def notify(self) -> None:
        for ob in self._obs:
            ob.subscribe(self)
    
    def operation(self)->None:
        self._state = random.randint(1, 10)
        self.notify()

class ObserverA(IObserver):
    def subscribe(self, subject: ISubject) -> None:
        if subject._state > 7:
            print(f'{self.__class__} reacted..')

class ObserverB(IObserver):
    def subscribe(self, subject: ISubject) -> None:
        if subject._state < 3:
            print(f'{self.__class__} reacted..')

class ObserverC(IObserver):
    def subscribe(self, subject: ISubject) -> None:
        if 3 <= subject._state <= 7:
            print(f'{self.__class__} reacted..')