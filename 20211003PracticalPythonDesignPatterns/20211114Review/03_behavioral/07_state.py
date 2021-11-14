# context - state

from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition_to(state)

    def transition_to(self, state:IState)->None:
        self._state = state
        self._state.context = self    

    def do_request1(self)->None:
        self._state.handle1()

    def do_request2(self)->None:
        self._state.handle2()

class IState(metaclass=ABCMeta):
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

class TrafficLightRed(IState):
    def handle1(self) -> None:
        print(f'{self.__class__} handles request1')
        self._context.transition_to(TrafficLightGreen())
    
    def handle2(self) -> None:
        print(f'{self.__class__} handles request2')

class TrafficLightGreen(IState):
    def handle1(self) -> None:
        print(f'{self.__class__} handles request1')

    def handle2(self) -> None:
        print(f'{self.__class__} handles request2')
        self._context.transition_to(TrafficLightRed())

def client_code()->None:
    c = Context(TrafficLightRed())
    c.do_request1()
    c.do_request2()

if __name__ == '__main__':
    client_code()