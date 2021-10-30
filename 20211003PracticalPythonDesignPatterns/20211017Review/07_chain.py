# chain of responsibility
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class IHandler(ABC):
    @abstractmethod
    def set_next(self,handler:IHandler)->IHandler: pass

    @abstractmethod
    def handle(self, request:str)->Optional[str]: pass

class ConcreteHandler(IHandler):
    _next_handler:IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request:str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(ConcreteHandler):
    def handle(self, request:str) -> Optional[str]:
        if request == 'banana':
            return f'Monkey, i will eat the {request}'
        return super().handle(request)

class DogHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'Dog, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'Squirrel, i will eat the {request}'
        return super().handle(request)

def client_code(handler:IHandler)->None:
    for food in ['nut', 'meatball', 'coffee']:
        print(f'\nwho wants {food}')
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