"#" 
from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class IState(ABC):
    @abstractproperty
    def context(self) -> Context:
        raise NotImplementedError()

    @abstractmethod
    def handle_request_01(self) -> None:
        pass

    @abstractmethod
    def handle_request_02(self) -> None:
        pass

class Context:
    _state:IState = None

    def __init__(self, state:IState) -> None:
        self.transition(state)

    def transition(self, state:IState) -> None:
        self._state = state

    def reqest_01(self) -> None:
        self._state.handle_request_01()

    def reqest_02(self) -> None:
        self._state.handle_request_01()

class TrafficLightRed(IState):
    def handle_request_01(self) -> None:
        print(f'{self.__class__} handle the request 01 and change state')
        self.context.transition(TrafficLightGreen())

    def handle_request_02(self) -> None:
        print(f'{self.__class__} handle the request 02')

class TrafficLightGreen(IState):
    def handle_request_01(self) -> None:
        print(f'{self.__class__} handle the request 01')

    def handle_request_02(self) -> None:
        print(f'{self.__class__} handle the request 02 and change state')
        self.context.transition(TrafficLightGreen())