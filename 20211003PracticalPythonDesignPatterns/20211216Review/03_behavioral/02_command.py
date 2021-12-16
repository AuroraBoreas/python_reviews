# 
from __future__ import annotations
from typing import List


class Commmand:
    def __init__(self, rec:Receiver, request:str) -> None:
        self._rec = rec
        self.request = request

    def execute(self)->None:
        self._rec.operation(self.request)

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__} handle {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Commmand] = []

    def add(self, command:Commmand)->None:
        self._commads.append(command)

    def run(self)->None:
        for command in self._commands:
            command.execute()