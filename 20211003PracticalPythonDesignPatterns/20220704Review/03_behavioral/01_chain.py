"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler) -> IHandler:
        pass

    @abstractmethod
    def handle(self, request:str) -> Optional[str]:
        pass

class Handler(IHandler):
    _next_handler:IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

def client_code(handler:Handler) -> None:
    for food in ["nut", "banana", "cup of coffee"]:
        print(f'\nClient: who wanna {food}')
        res = handler.handle(food)
        if res:
            print(f'  {res}', end='')
        else:
            print(f'  {food} was left untouched.', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()
    m.set_next(s).set_next(d)
    client_code(m)