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
    _handler:IHandler = None
    def set_next(self, handler: IHandler) -> IHandler:
        self._handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._handler:
            return self._handler.handle(request)
        return

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__} handle {request}'
        return super().handle(request)

def client_code(handler:IHandler) -> None:
    for item in ['nut', 'coffe','banana']:
        print(f'\nwho handles {item}?')
        res = handler.handle(item)
        if not res:
            print(f'  {item} was left untouched')
        else:
            print(f'  {res}')

if __name__ == '__main__':
    m = MonkeyHandler()
    s = SquirrelHandler()
    d = DogHandler()
    d.set_next(s).set_next(m)
    client_code(d)