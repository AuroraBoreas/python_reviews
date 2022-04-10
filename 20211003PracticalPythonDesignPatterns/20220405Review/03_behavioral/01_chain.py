"#" 
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Optional


class IHandler(metaclass=ABCMeta):
    _handler:IHandler = None

    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler:
        pass

    @abstractmethod
    def handle(self, request:str)->Optional[str]:
        pass

class Handler(IHandler):
    def set_next(self, handler: IHandler) -> IHandler:
        self._handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._handler:
            return self._handler.handle(request)
        return None

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__} handle the {request}'
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__} handle the {request}'
        return super().handle(request)

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__} handle the {request}'
        return super().handle(request)

def client_code(handler:IHandler)->None:
    food = ['banana', 'nut', 'coffe']
    for item in food:
        res = handler.handle(item)
        print(f'who will handle the {item}')
        if res:
            print(res)
        else:
            print(f'{item} left untouched')

if __name__ == '__main__':
    d = DogHandler()
    s = SquirrelHandler()
    m = MonkeyHandler()
    d.set_next(m).set_next(s)

    client_code(d)