# 
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState)->None:
        self._state = state

    def request01(self)->None:
        self._state.handle1()

    def request02(self)->None:
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

class TrafficLightRed(IState):
    def handle1(self) -> None:
        print(f'{self.__class__} handle request 1 and change state:')
        self.context.transition_to(TrafficLightGreen())

    def handle2(self) -> None:
        print(f'{self.__class__} handle request 2')

class TrafficLightGreen(IState):
    def handle1(self) -> None:
        print(f'{self.__class__} handle request 1')

    def handle2(self) -> None:
        print(f'{self.__class__} handle request 2 and change state:')
        self.context.transition_to(TrafficLightRed())