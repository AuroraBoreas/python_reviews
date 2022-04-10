"#" 
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

class Command:
    def __init__(self, rev:Receiver, req:str) -> None:
        self._rev = rev
        self._req = req
    
    def execute(self)->None:
        self._rev.operation(self._req)

class Receiver:
    def operation(self, request:str) -> None:
        print(f'{self.__class__} handle the {request}')