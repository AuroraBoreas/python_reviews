#
from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List


class IObserver(ABC):
    @abstractmethod
    def react(self, sender:ISubject) -> None:
        raise NotImplementedError()

    @property
    def subject(self) -> ISubject:
        return self._subject

    @subject.setter
    def subject(self, val:ISubject) -> None:
        self._subject = val

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def detach(self, ob:IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def operate(self) -> None:
        raise NotImplementedError()

class Subject(ISubject):
    _state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = list()

    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def operate(self) -> None:
        self._state = random.randint(1, 10)

    def announce(self) -> None:
        self.operate()
        for ob in self._observers:
            ob.react(self)

class ObserverA(IObserver):
    def react(self, sender: ISubject) -> None:
        if sender._state <= 5:
            print(f'{self.__class__} reacted')

class ObserverB(IObserver):
    def react(self, sender: ISubject) -> None:
        if sender._state >= 5:
            print(f'{self.__class__} reacted')

def client_code() -> None:
    sub = Subject()
    sub.attach(ObserverA())
    sub.attach(ObserverB())
    sub.announce()
    print('---')

def main() -> None:
    for _ in range(5):
        client_code()

if __name__ == '__main__':
    main()