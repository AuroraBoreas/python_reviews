from __future__ import annotations
from typing import Any, Optional, Union
from abc import ABC, abstractmethod

class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str)->Union[str, None]:
        raise NotImplementedError()

class AbstractHandler(IHandler):
    _next_handler = None
    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request:str)->Union[str, None]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'banana':
            return (f'Monkey, i will eat the {request}')
        return super().handle(request)

class SquirrelHanlder(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'nut':
            return (f'Squirrel, I will eat the {request}')
        return super().handle(request)

class DogHanlder(AbstractHandler):
    def handle(self, request: str) -> Union[str, None]:
        if request == 'meatball':
            return (f'Dog, I will eat the {request}')
        return super().handle(request)

def client_code(handler:IHandler)->Optional[str]:
    foods = ['nut', 'meatball', 'coffee']
    for food in foods:
        print(f'\nwho wants {food}')
        result = handler.handle(food)
        if result:
            print(f'   {result}', end='')
        else:
            print(f'   {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHanlder()
    s = SquirrelHanlder()
    print(m._next_handler)

    s.set_next(d).set_next(m)
    print('chain: squirrel -> dog -> monkey')
    client_code(s)

    print('\n===')
    print('chain: dog -> monkey')
    client_code(d)
