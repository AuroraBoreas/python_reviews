"#" 

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Optional


class IHandler(metaclass=ABCMeta):
    @abstractmethod
    def next_handler(self, handler:IHandler) -> IHandler:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request:str) -> Optional[str]:
        raise NotImplementedError()

class Handler(IHandler):
    _handler:IHandler = None

    def next_handler(self, handler: IHandler) -> IHandler:
        self._handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._handler:
            return self._handler.handle(request) 
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
    for item in ['meatball', 'nut', 'coffee']:
        res = h.handle(item)
        if res:
            print(f'  {res}')
        else:
            print(f'  {item} was left untouched')

if __name__ == '__main__':
    mh:IHandler = MonkeyHandler()
    sh:IHandler = SquirrelHandler()
    dh:IHandler = DogHandler()
    mh.next_handler(dh).next_handler(sh)
    client_code(mh)