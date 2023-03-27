# 
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state: IState = None

    def __init__(self, state: IState) -> None:
        self.transmit_to(state)

    def transmit_to(self, state: IState) -> None:
        self._state = state
        self._state.context = self

    def handle_request01(self) -> None:
        self._state.do_this()

    def handle_request02(self) -> None:
        self._state.do_that()

class IState(ABC):
    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, val: Context) -> None:
        self._context = val

    @abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError

class TrafficLightRed(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} : do something important and change state')
        self.context.transmit_to(TrafficLightGreen())

    def do_that(self) -> None:
        print(f'{self.__class__} : do another important thing')

class TrafficLightGreen(IState):
    def do_this(self) -> None:
        print(f'{self.__class__} : do another important thing')

    def do_that(self) -> None:
        print(f'{self.__class__} : do something important and change state')
        self.context.transmit_to(TrafficLightRed())