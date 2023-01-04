"#" 
from __future__ import annotations

from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
from dataclasses import dataclass, field
import random

class IObserver(ABC):
    @property
    def subject(self) -> ISubject:
        return self._subject
    
    @subject.setter
    def subject(self, val: ISubject) -> None:
        self._subject= val

    @abstractmethod
    def react(self, subject: ISubject) -> None:
        raise NotImplementedError()

class ISubject(ABC):
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def attach(self, ob: IObserver) -> None:
        raise NotImplementedError()

    @abstractmethod
    def detach(self, ob: IObserver) -> None:
        raise NotImplementedError()

@dataclass
class Subject1(ISubject):
    _state: int = field(default=0)

    def __init__(self) -> None:
        self._observers: list[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self) -> None:
        for ob in self._observers:
            ob.react(self)

    def operate(self) -> None:
        self._state = random.randint(1, 10)
        self.notify()

class Observer1(IObserver):
    def react(self, subject: ISubject) -> None:
        if subject._state >= 5:
            logging.info(f'{self.__class__} reacted')

class Observer2(IObserver):
    def react(self, subject: ISubject) -> None:
        if subject._state <= 5:
            logging.info(f'{self.__class__} reacted')

def client_code() -> None:
    ob1: Observer1 = Observer1()
    ob2: Observer2 = Observer2()
    sub: Subject1 = Subject1()
    sub.attach(ob1)
    sub.attach(ob2)
    for _ in range(5):
        sub.operate()
        logging.info('subject state changed to: {}'.format(sub._state))

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()