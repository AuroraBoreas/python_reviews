"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC

class IState(ABC):
    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, val: Context) -> None:
        self._context = val

class Context:
    state: IState = None

    def __init__(self, state: IState) -> None:
        self.transition_to(state)

    def transition_to(self, state: IState) -> None:
        self.state = state
        self.state.context = self

    def handle_request_01(self) -> None:
        self.state.do_this()

    def handle_request_02(self) -> None:
        self.state.do_that()

class TrafficLightRed(IState):
    def do_this(self) -> None:
        print(f"{self.__class__.__qualname__} : do something important and change state")
        self.context.transition_to(TrafficLightGreen())
    
    def do_that(self) -> None:
        print(f"{self.__class__.__qualname__} : do another important something")

class TrafficLightGreen(IState):
    def do_this(self) -> None:
        print(f"{self.__class__.__qualname__} : do another important something")
    
    def do_that(self) -> None:
        print(f"{self.__class__.__qualname__} : do something important and change state")
        self.context.transition_to(TrafficLightGreen())