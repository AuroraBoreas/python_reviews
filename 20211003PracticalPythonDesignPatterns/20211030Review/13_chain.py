# chain of responsibility
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Optional

class IHandler(metaclass=ABCMeta):
    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler:
        pass

    @abstractmethod
    def handle(self, request:str)->Optional[str]:
        pass

class ConcreteHandler(IHandler):
    _next_handler:ConcreteHandler = None
    
    def set_next(self, handler: ConcreteHandler) -> ConcreteHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

    def __str__(self)->str:
        return '{0!r}'.format(self._next_handler)

class MonkeyHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

class DogHandler(ConcreteHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__}, i will eat the {request}'
        return super().handle(request)

def client_code(handler:ConcreteHandler)->None:
    for food in ['nut', 'meatball', 'coffee']:
        print(f'\nwho wanna {food}')
        rv = handler.handle(food)
        if rv:
            print(f'  {rv}', end='')
        else:
            print(f'  {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    s = SquirrelHandler()
    d = DogHandler()
    s.set_next(m).set_next(d)
    print(s.set_next(m) == m)
    client_code(s)