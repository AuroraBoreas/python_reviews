# observer, delegate -> synchronous -> asyn && await

from __future__ import annotations
from abc import ABC, abstractmethod
import random

class ISubject(ABC):
    @abstractmethod
    def attach(self, ob:IObserver)->None: pass

    @abstractmethod
    def detach(self, ob:IObserver)->None: pass

    @abstractmethod
    def notify(self)->None: pass

class IObserver(ABC):
    @abstractmethod
    def update(self, sub:ConcreteSubject)->None: pass

class ConcreteSubject(ISubject):
    _state:int = 0
    _observers:list[IObserver] = []

    def attach(self, ob: IObserver) -> None:
        print(f'Subject: attached an observer -> {ob.__class__}')
        self._observers.append(ob)
        
    def detach(self, ob: IObserver) -> None:
        print(f'Subject: deattaced an observer -> {ob.__class__}')
        self._observers.remove(ob)

    def notify(self) -> None:
        print('Subject: notifying observers..')
        for ob in self._observers:
            ob.update(self)

    def some_business_logic(self)->None:
        print('Subject: im doing something important.')
        self._state = random.randrange(0, 10)
        print(f'Subject: my state just changed to: {self._state}')
        self.notify()

class ConcreteObserverA(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state < 3:
            print(f'{self.__class__} : reacted to the event')

class ConcreteObserverB(IObserver):
    def update(self, sub: ConcreteSubject) -> None:
        if sub._state == 0 or sub._state >= 2:
            print(f'{self.__class__} : reacted to the event')

def client_code():
    sub = ConcreteSubject()
    ob1 = ConcreteObserverA()
    ob2 = ConcreteObserverB()
    sub.attach(ob1)
    sub.attach(ob2)

    print('\nob1, ob2 sub\'ed!')
    for _ in range(3):
        sub.some_business_logic()
        sub.some_business_logic()

    print('\nob1 sub\'ed!')
    sub.detach(ob1)
    for _ in range(3):
        sub.some_business_logic()

if __name__ == '__main__':
    client_code()