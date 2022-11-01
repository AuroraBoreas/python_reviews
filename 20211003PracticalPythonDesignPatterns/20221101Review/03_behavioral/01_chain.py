"#" 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler) -> IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str) -> Optional[str]:
        raise NotImplementedError()

class Handler(IHandler):
    __handler:IHandler = None
    def set_next(self, handler: IHandler) -> IHandler:
        self.__handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self.__handler:
            return self.__handler.handle(request)
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

def client_code(h:IHandler) -> None:
    for food in ['meatball', 'nut', 'coffee', 'meat', 'banana']:
        res = h.handle(food)
        if not res:
            print(f'   {food} was left untouched')
        else:
            print(f'   {res}')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()
    m.set_next(d).set_next(s)
    client_code(m)