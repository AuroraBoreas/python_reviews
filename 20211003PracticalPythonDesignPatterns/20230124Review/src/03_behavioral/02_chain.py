from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Self


class IHandler(ABC):
    @abstractmethod
    def next(self, handler: IHandler) -> IHandler:
        raise NotImplementedError

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        raise NotImplementedError

class Handler(IHandler):
    handler: IHandler = None
    def next(self, handler: Self) -> Self:
        self.handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self.handler:
            return self.handler.handle(request)
        return

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f"{self.__class__} handles {request}"
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f"{self.__class__} handles {request}"
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meatball':
            return f"{self.__class__} handles {request}"
        return super().handle(request)
