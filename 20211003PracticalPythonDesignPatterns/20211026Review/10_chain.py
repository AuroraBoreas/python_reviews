# chain of responsibility

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union, Any

class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler: pass

    @abstractmethod
    def handle(self, request:str)->Union[str, None]: pass


class ConcreteHandler(IHandler):
    _next_handler:IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Union[str, None]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(ConcreteHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'banana':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(ConcreteHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'nut':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class DogHandler(ConcreteHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'meatball':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

def client_code(handler:IHandler)->None:
    for request in ['meatball', 'nut', 'coffee']:
        print(f'\nwho wants the {request}?')
        rv = handler.handle(request)
        if rv:
            print(f'  {rv}', end='')
        else:
            print(f'  {request} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()

    m.set_next(d).set_next(s)    
    client_code(m)