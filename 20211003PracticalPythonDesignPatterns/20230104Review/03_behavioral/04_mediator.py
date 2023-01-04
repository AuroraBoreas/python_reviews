"#" 
from __future__ import annotations

from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class IMediator(ABC):
    @abstractmethod
    def notify(self, sender: IComponent, event: str) -> None:
        raise NotImplementedError()

class Mediator(IMediator):
    def __init__(self, comp1: IComponent, comp2: IComponent) -> None:
        self._comp1: IComponent = comp1
        self._comp1.mediator    = self
        self._comp2: IComponent = comp2
        self._comp2.mediator    = self

    def notify(self, sender: IComponent, event: str) -> None:
        logging.info(f'{self.__class__} received {event} from {sender.__class__}')
        match event:
            case 'A':
                self._comp2.do_c()
            case 'D':
                self._comp1.do_a()
                self._comp1.do_b()
            case _:
                ...

class IComponent(ABC):
    @property
    def mediator(self) -> IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, val: IMediator) -> None:
        self._mediator = val

class ComponentA(IComponent):
    def do_a(self) -> None:
        logging.info(f'{self.__class__} do_a')
        self.mediator.notify(self, 'A')

    def do_b(self) -> None:
        logging.info(f'{self.__class__} do_b')

class ComponentB(IComponent):
    def do_c(self) -> None:
        logging.info(f'{self.__class__} do_c')

    def do_d(self) -> None:
        logging.info(f'{self.__class__} do_d')
        self.mediator.notify(self, 'D')

def main() -> None:
    ca: ComponentA = ComponentA()
    cb: ComponentB = ComponentB()
    m: Mediator = Mediator(ca, cb)
    ca.do_a()
    cb.do_d()

if __name__ == '__main__':
    main()
