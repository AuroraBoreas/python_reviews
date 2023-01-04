"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler: IHandler) -> IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        raise NotImplementedError()

class Handler(IHandler):
    _handler: IHandler = None
    def set_next(self, handler: IHandler) -> IHandler:
        self._handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._handler:
            return self._handler.handle(request)
        return None

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f"{self.__class__} handle {request}"
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f"{self.__class__} handle {request}"
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f"{self.__class__} handle {request}"
        return super().handle(request)

def client_code(h: IHandler) -> None:
    for item in ['nut', 'meatball', 'coffee']:
        rev: str | None = h.handle(item)
        if rev:
            logging.info(f'{rev}')
        else:
            logging.info(f'{item} was left untouched')

def main() -> None:
    s: SquirrelHandler = SquirrelHandler()
    d: DogHandler = DogHandler()
    m: MonkeyHandler = MonkeyHandler()
    d.set_next(m).set_next(s)
    client_code(d)

if __name__ == '__main__':
    main()
