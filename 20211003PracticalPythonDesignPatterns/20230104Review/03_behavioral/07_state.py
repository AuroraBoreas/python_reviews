"#" 
from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

@dataclass
class Context:
    _state: IState = field(default=None)

    def __init__(self, state: IState) -> None:
        self.transmit_to(state)

    def transmit_to(self, state: IState) -> None:
        self._state = state
        self._state.context = self

    def handle_request_01(self) -> None:
        self._state.do_this()

    def handle_request_02(self) -> None:
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
        raise NotImplementedError()

    @abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError()

class TrafficeLightRed(IState):
    def do_this(self) -> None:
        logging.info(f'{self.__class__} do something important and change status')
        self.context.transmit_to(TrafficeLightGreen())

    def do_that(self) -> None:
        logging.info(f'{self.__class__} do something unimportant')

class TrafficeLightGreen(IState):
    def do_this(self) -> None:
        logging.info(f'{self.__class__} do something unimportant')

    def do_that(self) -> None:
        logging.info(f'{self.__class__} do something important and change status')
        self.context.transmit_to(TrafficeLightRed())

def main() -> None:
    c: Context = Context(TrafficeLightGreen())
    c.handle_request_01()
    c.handle_request_02()
    logging.info(c)

if __name__ == '__main__':
    main()