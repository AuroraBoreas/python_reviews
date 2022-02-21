# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


class IHandler(ABC):
    @abstractmethod
    def set_next(self, handler:IHandler)->IHandler:
        pass

    @abstractmethod
    def handle(self, request:str)->Optional[str]:
        pass

class Handler(IHandler):
    _next_handler:IHandler = None
    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__} : handle the {request}'
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__} : handle the {request}'
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__} : handle the {request}'
        return super().handle(request)

def client_code(handle:IHandler)->None:
    foods:List[str] = ['meatball' , 'nut', 'coffee']
    for food in foods:
        rv = handle.handle(food)
        if not rv:
            print('\n{rv}')
        else:
            print(f'{food} was left untouched')