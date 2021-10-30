# state: traffic R G B

from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState)->None:
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class IState(ABC):
    @property
    def context(self)->Context:
        return self._context

    @context.setter
    def context(self, val:Context)->None:
        self._context = val

    @abstractmethod
    def handle1(self)->None: pass

    @abstractmethod
    def handle2(self)->None: pass

class ConcreteStateA(IState):
    def handle1(self) -> None:
        print(f'{self.__class__}, handles request1')
        print(f'{self.__class__}, wanna changee the state of the context')
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print(f'{self.__class__}, handles request2')

class ConcreteStateB(IState):
    def handle1(self) -> None:
        print(f'{self.__class__}, handles request2')

    def handle2(self) -> None:
        print(f'{self.__class__}, handles request')
        print(f'{self.__class__}, wanna changee the state of the context')
        self.context.transition_to(ConcreteStateA())

def client_code():
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()

if __name__ == '__main__':
    client_code()