# 
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req

    def execute(self)->None:
        self._rec.operation(self._req)

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__} : handle the {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command)->None:
        self._commands.append(command)

    def run(self)->None:
        for cmd in self._commands:
            cmd.execute()