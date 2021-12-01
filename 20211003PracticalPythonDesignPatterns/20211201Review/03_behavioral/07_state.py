# 
from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    def __init__(self) -> None:
        pass

    def transition_to(self, state:IState)->None:
        pass

    def do_request_01(self)->None:
        pass

    def do_request_02(self)->None:
        pass

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
        print(f'{self.__class__}: handle request1, and change state')
        self.context.transition_to(TrafficLightGreen())

    def handle2(self) -> None:
        print(f'{self.__class__}: handle request2')

class TrafficLightGreen(IState):
    def handle1(self) -> None:
        print(f'{self.__class__}: handle request1')

    def handle2(self) -> None:
        print(f'{self.__class__}: handle request2, and change state')
        self.context.transition_to(TrafficLightRed())