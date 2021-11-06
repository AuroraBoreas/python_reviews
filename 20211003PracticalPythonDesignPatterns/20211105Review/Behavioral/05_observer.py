# Subject - Observer
from __future__ import annotations
from abc import ABCMeta, abstractmethod
import random
from typing import List

class ISubject(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def attach(self, ob:IObserver)->None:
        pass

    @abstractmethod
    def detach(self, ob:IObserver)->None:
        pass

class ConcreteSubject(ISubject):
    _state:int = None 
    _observers:List[IObserver] = []
    
    def attach(self, ob: IObserver) -> None:
        self._observers.append(ob)

    def detach(self, ob: IObserver) -> None:
        self._observers.remove(ob)

    def notify(self)->None:
        for ob in self._observers:
            ob.update(self)

    def some_business_logic(self)->None:
        print(f'{self.__class__}, changes state')
        self._state = random.randrange(0, 10)
        self.notify()

class IObserver:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self, sub:ConcreteSubject)->None:
        pass

class ObserverA(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state >= 3:
            print(f'{self.__class__}, reacted')

class ObserverB(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state == 0 or sub._state > 3:
            print(f'{self.__class__}, reacted')

def client_code()->None:
    oba = ObserverA()
    obb = ObserverB()
    sub = ConcreteSubject()
    sub.attach(oba)
    sub.attach(obb)
    sub.some_business_logic()

if __name__ == '__main__':
    client_code()