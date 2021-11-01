# chain of responsibility
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler:Handler)->Handler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str)->Optional[str]:
        raise NotImplementedError()

class ConcreteHandler(Handler):
    _next_handler:Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class DogHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

def client_code(handler:Handler)->None:
    for food in ['nut', 'meatball', 'coffee']:
        print('\nwho wanna {food}?')
        rv = handler.handle(food)
        if rv:
            print(f'   {rv}', end='')
        else:
            print(f'   {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()

    m.set_next(d).set_next(s)

    client_code(m)