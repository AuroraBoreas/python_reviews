# invoker - receiver - command 
from __future__ import annotations
from typing import List


class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command)->None:
        self._commands.append(command)

    def run(self)->None:
        for command in self._commands:
            command.execute()

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__} : received {request}')

class Command:
    def __init__(self, receiver:Receiver, msg:str) -> None:
        self.receiver = receiver
        self.msg = msg
    
    def execute(self)->None:
        self.receiver.operation(self.msg)
