# state: finite-state-machine

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

class TrafficLightRed(State):
    def handle1(self) -> None:
        print('TrafficLightRed handles request1.')
        print('TrafficLightRed wants to change to the state of the context.')
        self._context.transition_to(TrafficLightGreen())

    def handle2(self) -> None:
        print('TrafficLightRed handles request2.')

class TrafficLightGreen(State):
    def handle1(self) -> None:
        print('TrafficLightRed handles request1.')

    def handle2(self) -> None:
        print('TrafficLightGreen handles request2.')
        print('TrafficLightGreen wants to change to the state of the context.')
        self._context.transition_to(TrafficLightRed())

class Context:
    _state: State = None

    def __init__(self, state:State)->None:
        self.transition_to(state)

    def transition_to(self, state:State)->None:
        self._state = state
        self._state.context = self

    def do_this(self)->None:
        self._state.handle1()

    def do_that(self)->None:
        self._state.handle2()

def client_code():
    c = Context(TrafficLightRed())
    c.do_this()
    c.do_that()

if __name__ == '__main__':
    client_code()
