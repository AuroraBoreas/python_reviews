# context - state
from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state:State = None

    def __init__(self, state:State) -> None:
        self.change_state(state)

    def change_state(self, state:State)->None:
        print(f'Context: transition to {type(state).__name__}')
        self._state = state
        self._state.context = self

    def do_this(self)->None:
        self._state.handle1()

    def do_that(self)->None:
        self._state.handle2()

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

class ConcreteStateA(State):
    def handle1(self) -> None:
        print('ConcreteStateA handles request1')
        print('ConcreteStateA wants to change the state of context')
        self.context.change_state(ConcreteStateB())

    def handle2(self) -> None:
        print('ConcreteStateA handles request2')

class ConcreteStateB(State):
    def handle1(self) -> None:
        print('ConcreteStateB handles request1')

    def handle2(self) -> None:
        print('ConcreteStateB handles request2')
        print('ConcreteStateB wants to change the state of context')
        self.context.change_state(ConcreteStateA())

def client_code()->None:
    c = Context(ConcreteStateA())
    c.do_this()
    c.do_that()

if __name__ == '__main__':
    client_code()