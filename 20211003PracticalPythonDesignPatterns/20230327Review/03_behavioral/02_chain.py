# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class IHandler(ABC):
    @abstractmethod
    def next(self, handler: IHandler) -> IHandler:
        raise NotImplementedError
    
    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        raise NotImplementedError

class Handler(IHandler):
    _handler: IHandler = None

    def next(self, handler: IHandler) -> IHandler:
        self._handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if not self._handler:
            return
        return self._handler.handle(request)
    
class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f'{self.__class__} handles {request}'
        return super().handle(request)
    
class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f'{self.__class__} handles {request}'
        return super().handle(request)
    
class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f'{self.__class__} handles {request}'
        return super().handle(request)
