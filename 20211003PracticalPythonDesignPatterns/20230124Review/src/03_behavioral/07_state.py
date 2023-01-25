from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    state: IState = None

    def __init__(self, state: IState) -> None:
        self.transition(state)

    def transition(self, state: IState) -> None:
        self.state = state
        self.state.context = self

    def handle_request_01(self) -> None:
        self.state.do_this()

    def handle_request_02(self) -> None:
        self.state.do_that()

class IState(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, value: Context) -> None:
        self._context = value

    @abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError

class TrafficlightRed(IState):
    def do_this(self) -> None:
        print(f"{self.__class__} does someting important(do_this) and change state")
        self.context.transition(TrafficlightGreen())

    def do_that(self) -> None:
        print(f"{self.__class__} does someting important(do_that)")

class TrafficlightGreen(IState):
    def do_this(self) -> None:
        print(f"{self.__class__} does someting important(do_this) and change state")

    def do_that(self) -> None:
        print(f"{self.__class__} does someting important(do_that)")
        self.context.transition(TrafficlightRed())
