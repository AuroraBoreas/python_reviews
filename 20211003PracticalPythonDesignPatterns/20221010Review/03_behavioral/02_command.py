#
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req

    def operate(self) -> None:
        self._rec.handle(self._req)

class Receiver:
    def handle(self, request:str) -> None:
        print(f'{self.__class__} handle {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = list()
        
    def add(self, command:Command) -> None:
        self._commands.append(command)
        
    def remove(self, command:Command) -> None:
        self._commands.remove(command)
        
    def run(self) -> None:
        for cmd in self._commands:
            cmd.operate()