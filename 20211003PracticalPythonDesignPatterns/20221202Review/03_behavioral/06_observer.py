"#" 
from __future__ import annotations
from abc import abstractmethod
import random
from typing import List


class IObserver:
    @abstractmethod
    def react(self, sub:ISubject) -> None:
        raise NotImplementedError()

class ISubject:
    @abstractmethod
    def attach(self, ob:IObserver) -> None:
        raise NotImplementedError()
    @abstractmethod
    def detach(self, ob:IObserver) -> None:
        raise NotImplementedError()
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()

class Subject(ISubject):
    __state:int = None

    def __init__(self) -> None:
        self._observers:List[IObserver] = list()
        
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)
        
    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)
        
    def notify(self) -> None:
        for ob in self._observers:
            ob.react(self)

    @property
    def state(self) -> int:
        return self.__state

    def operate(self) -> None:
        self.__state = random.randint(1, 10)
        self.notify()

class ObserverA(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state <= 6:
            print(f'{self.__class__} reacted')

class ObserverB(IObserver):
    def react(self, sub: ISubject) -> None:
        if sub.state >= 5:
            print(f'{self.__class__} reacted')

def client_code() -> None:
    s = Subject()
    s.attach(ObserverA())
    s.attach(ObserverB())
    for _ in range(3):
        s.operate()

if __name__ == '__main__':
    client_code()