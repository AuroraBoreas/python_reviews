from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Union

class IHandler:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str)->Union[None, str]:
        raise NotImplementedError()

class AbstractHandler(IHandler):
    _next_handler:IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Union[None, str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> Union[None, str]:
        if request == 'banana':
            return f'Monkey, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> Union[None, str]:
        if request == 'nut':
            return f'Squirrel, i will eat the {request}'
        return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: str) -> Union[None, str]:
        if request == 'meatball':
            return f'Dog, i will eat the {request}'
        return super().handle(request)

def client_code(handler:IHandler)->Union[str, None]:
    for food in ['meatball', 'nut', 'coffee']:
        print(f'\nwho wanna the {food}')
        rv  = handler.handle(food)
        if rv:
            print(f'    {rv}', end='')
        else:
            print(f'    {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()

    m.set_next(d).set_next(s)

    client_code(m)
    print()
