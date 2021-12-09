# 
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState)->None:
        self._state = state

    def request_01(self)->None:
        self._state.handle01()

    def request_02(self)->None:
        self._state.handle02()

class IState:
    __metaclass__ = ABCMeta

    @property
    def context(self)->Context:
        return self._context

    @context.setter
    def context(self, val:Context)->None:
        self._context = val

    @abstractmethod
    def handle01(self)->None:
        pass

    @abstractmethod
    def handle02(self)->None:
        pass

class TrafficLightRed(IState):
    def handle01(self) -> None:
        print(f'{self.__class__} handle request 01 and wanna change state:')
        self.context.transition_to(TrafficLightGreen())
    
    def handle02(self) -> None:
        print(f'{self.__class__} handle request 02')

class TrafficLightGreen(IState):
    def handle01(self) -> None:
        print(f'{self.__class__} handle request 01')
    
    def handle02(self) -> None:
        print(f'{self.__class__} handle request 02 and wanna change state:')
        self.context.transition_to(TrafficLightGreen())