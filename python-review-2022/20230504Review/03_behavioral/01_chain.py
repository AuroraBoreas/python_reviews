"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Self


class IHandler(ABC):
    @abstractmethod
    def next(self, handler: IHandler) -> IHandler:
        raise NotImplementedError
    
    @abstractmethod
    def handle(self, request: str) -> Optional[None]:
        raise NotImplementedError
    
class Handler1(IHandler):
    __handler: IHandler = None
    def next(self, handler: IHandler) -> IHandler:
        self.__handler = handler
        return handler
    @abstractmethod
    def handle(self, request: str) -> Optional[None]:
        if self.__handler:
            return self.__handler.handle(request)
        return None
    
class MonkeyHandler(Handler1):
    def handle(self, request: str) -> None:
        if request == 'banana':
            return f"{self.__class__.__name__} handles {request}"
        return super().handle(request)
    
class SquirrelHandler(Handler1):
    def handle(self, request: str) -> None:
        if request == 'nut':
            return f"{self.__class__.__name__} handles {request}"
        return super().handle(request)
    
class DogHandler(Handler1):
    def handle(self, request: str) -> None:
        if request == 'meatball':
            return f"{self.__class__.__name__} handles {request}"
        return super().handle(request)

def client_code(handler: IHandler) -> None:
    for item in ['meatball', 'nut', 'coffee']:
        res = handler.handle(item)
        print(f"who handles {item}?")
        if res:
            print(f'  {item} -> {res}')
        else:
            print(f'  {item} was left untouched')

def main() -> None:
    d: DogHandler = DogHandler()
    m: MonkeyHandler = MonkeyHandler()
    s: SquirrelHandler = SquirrelHandler()
    m.next(s).next(d)
    client_code(m)

if __name__ == '__main__':
    main()