#
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class IHandler(ABC):
    @abstractmethod
    def set_handler(self, handler:IHandler) -> IHandler:
        raise NotImplementedError()
    @abstractmethod
    def handle(self, request:str) -> Optional[str]:
        raise NotImplementedError()

class Handler(IHandler):
    handler:IHandler = None
    def set_handler(self, handler: IHandler) -> IHandler:
        self.handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if not self.handler:
            return None
        return self.handler.handle(request)

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

def client_code(h:Handler) -> None:
    for item in ['meatball', 'banana', 'coffee']:
        res = h.handle(item)
        if not res:
            print(f'  {item} was left untouched')
        else:
            print(f'  {res}')

def main() -> None:
    d = DogHandler()
    m = MonkeyHandler()
    s = SquirrelHandler()
    m.set_handler(d).set_handler(s)
    client_code(m)

if __name__ == '__main__':
    main()






