"#" 
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req
    
    def operate(self) -> None:
        return self._rec.handle(self._req)

class Receiver:
    def handle(self, req:str) -> str:
        return f'{self.__class__} handle {req}'

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = list()

    def add(self, cmd:Command) -> None:
        self._commands.append(cmd)

    def remove(self, cmd:Command) -> None:
        self._commands.remove(cmd)

    def run(self) -> None:
        for cmd in self._commands:
            print(cmd.operate())