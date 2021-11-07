# context - state
from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    @property
    def context(self)->Context:
        return self._context
    
    @context.setter
    def context(self, val:Context)->None:
        self._context = val

    @abstractmethod
    def handle1(self)->None:
        pass

    @abstractmethod
    def handle2(self)->None:
        pass

class TrafficRed(State):
    def handle1(self) -> None:
        print(f'{self.__class__} handles request1')
        self._context.transition_to(TrafficGreen())

    def handle1(self) -> None:
        print(f'{self.__class__} handles request2')

class TrafficGreen(State):
    def handle1(self) -> None:
        print(f'{self.__class__} handles request1')

    def handle2(self) -> None:
        print(f'{self.__class__} handles request2')
        self._context.transition_to(TrafficRed())
        
class Context:
    _state:State = None

    def __init__(self, state:State) -> None:
        self.transition_to(state)

    def transition_to(self, state:State)->None:
        print(f'{Context: transition to {type(state).__name__}}')
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

def client_code()->None:
    c = Context(TrafficRed())
    c.request1()
    c.request2()

if __name__ == '__main__':
    client_code()