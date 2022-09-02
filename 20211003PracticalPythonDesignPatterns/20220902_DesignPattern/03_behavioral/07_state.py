"#" 
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState) -> None:
        self._state = state
        self._state.context = self

    def handle_request_01(self) -> None:
        self._state.do_this()

    def handle_request_02(self) -> None:
        self._state.do_that()

class IState(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, val:Context) -> None:
        self._context = val
    
    @abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError()
    
class RedLight(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} do something important and change state')
        self.context.transition_to(GreenLight())

    def do_that(self) -> None:
        print(f'{self.__class__} do another important thing')
    
class GreenLight(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} do another important thing')

    def do_that(self) -> None:
        print(f'{self.__class__} do something important and change state')
        self.context.transition_to(RedLight())

def client_code() -> None:
    c = Context(RedLight())
    c.handle_request_01()
    c.handle_request_02()

if __name__ == '__main__':
    client_code()
