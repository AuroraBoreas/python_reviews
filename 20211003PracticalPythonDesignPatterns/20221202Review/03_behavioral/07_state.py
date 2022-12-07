"#" 
from __future__ import annotations
from abc import ABC


class IState(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, val:Context) -> None:
        self._context = val

class Context:
    __state:IState = None
    def __init__(self, state:IState) -> None:
        self.transit(state)
        
    def transit(self, state:IState) -> None:
        self.__state = state
        self.__state.context = self
        
    def handle_request_01(self) -> None:
        self.__state.do_this()

    def handle_request_02(self) -> None:
        self.__state.do_that()

class TrafficLightRed(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} do something crucial, and change state')
        self.context.transit(TrafficLightGreen())
    def do_that(self) -> None:
        print(f'{self.__class__} do nothing')

class TrafficLightGreen(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} do nothing')
    def do_that(self) -> None:
        print(f'{self.__class__} do something crucial, and change state')
        self.context.transit(TrafficLightBlue())

class TrafficLightBlue(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} do something crucial, and change state')
        self.context.transit(TrafficLightRed())
    def do_that(self) -> None:
        print(f'{self.__class__} do nothing')

def client_code() -> None:
    c = Context(TrafficLightRed())
    c.handle_request_01()
    c.handle_request_02()

if __name__ == '__main__':
    client_code()