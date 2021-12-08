# 
from __future__ import annotations
from typing import List

class Command:
    def __init__(self, rev:Receiver, request:str) -> None:
        self.rev = rev
        self.request = request

    def execute(self)->None:
        self.rev.operation(self.request)

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__} handles {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command)->None:
        self._commands.append(command)

    def run(self)->None:
        for command in self._commands:
            command.execute()