# 

from __future__ import annotations
from typing import List

class Command:
    def __init__(self, receiver:Receiver, request:str) -> None:
        self.receiver = receiver
        self.request  = request

    def execute(self)->None:
        self.receiver.operation(self.request)

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__}: start processing with {request}')


class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command)->None:
        self._commands.append(command)

    def run(self)->None:
        for command in self._commands:
            command.execute()