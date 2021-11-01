
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Union

class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler) -> IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str)->Union[str, None]:
        raise NotImplementedError()

class AbstractHandler(IHandler):
    _next_handler:IHandler = None
    def set_next(self, handler:IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Union[str, None]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHanlder(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'banana':
            return f'Monkey, I will eat the {request}'
        return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'meatball':
            return f'Dog, I will eat the {request}'
        return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'nut':
            return f'Squirrel, I will eat the {request}'
        return super().handle(request)

def client_code(hanlder:IHandler)->Union[str, None]:
    for food in ['nut', 'meatball', 'banana']:
        print(f'\nwho wanna {food}')
        result = hanlder.handle(food)
        if result:
            print(f'   {result}', end='')
        else:
            print(f'   {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHanlder()
    s = SquirrelHandler()
    d = DogHandler()

    print('\nchain: squirrel > monkey > dog')
    s.set_next(m).set_next(d)
    client_code(s)

    print('\nchain: monkey > dog')
    client_code(m)
