# 

from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState)->None:
        self._state = state
        self._state.context = self

    def required_01(self)->None:
        self._state.handle_01()

    def required_02(self)->None:
        self._state.handle_02()

class IState(ABC):
    @property
    def context(self)->Context:
        return self._context

    @context.setter
    def context(self, val:Context)->None:
        self._context = val

    @abstractmethod
    def handle_01(self)->None: pass

    @abstractmethod
    def handle_02(self)->None: pass

class TrafficLightRed(IState):
    def handle_01(self) -> None:
        print(f'{self.__class__} : handle the request 01 and chanage state')
        self._context.transition_to(TrafficLightGreen())

    def handle_02(self) -> None:
        print(f'{self.__class__} : handle the request 02')

class TrafficLightGreen(IState):
    def handle_01(self) -> None:
        print(f'{self.__class__} : handle the request 01')

    def handle_02(self) -> None:
        print(f'{self.__class__} : handle the request 02 and chanage state')
        self._context.transition_to(TrafficLightRed())
